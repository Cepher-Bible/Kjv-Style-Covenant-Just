#!/usr/bin/env python3
"""
KJV 1611 vs 1769 Blayney Revision Comparison
Comprehensive word-level analysis with theological term tracking
"""

import csv
import re
from difflib import SequenceMatcher
from collections import defaultdict

# Theological terms to track (subset - expand with your Covenant Anchor locks)
LOCKED_TERMS = {
    'atonement', 'propitiation', 'covenant', 'testament', 'baptize', 'baptism',
    'repent', 'repentance', 'justify', 'justification', 'sanctify', 'sanctification',
    'grace', 'faith', 'salvation', 'redemption', 'reconciliation', 'blood',
    'sacrifice', 'priest', 'altar', 'sabbath', 'lord', 'god', 'christ', 'spirit'
}

def parse_bible_text(filename):
    """Parse Bible text into structured dict with full metadata."""
    bible_data = {}
    line_count = 0
    error_count = 0
    
    print(f"Parsing {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line_count += 1
                line = line.strip()
                if not line:
                    continue
                
                # Try multiple formats
                # Format 1: "Book Chapter:Verse text"
                match = re.match(r'^(.*?)\s+(\d+):(\d+)\s+(.*)$', line)
                
                # Format 2: "Book.Chapter.Verse text"
                if not match:
                    match = re.match(r'^(.*?)\.(\d+)\.(\d+)\s+(.*)$', line)
                
                if match:
                    book = match.group(1).strip().replace(' ', '_')
                    chapter = match.group(2)
                    verse = match.group(3)
                    text = match.group(4)
                    ref = f"{book}.{chapter}.{verse}"
                    
                    # Extract words with metadata
                    words = []
                    for word_match in re.finditer(r'\b(\w+)\b', text):
                        word = word_match.group(1)
                        words.append({
                            'original': word,
                            'clean': word.lower().strip('.,;:!?\'"'),
                            'has_capital': word[0].isupper() if word else False,
                            'all_caps': word.isupper(),
                            'position': word_match.start()
                        })
                    
                    bible_data[ref] = {
                        'words': words,
                        'raw_text': text,
                        'word_count': len(words),
                        'punctuation': re.findall(r'[.,;:!?]', text)
                    }
                else:
                    error_count += 1
                    if error_count <= 5:  # Only show first 5 errors
                        print(f"  Warning: Line {line_num} format unknown: {line[:60]}...")
    
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found!")
        return {}
    
    print(f"  Loaded {len(bible_data)} verses from {line_count} lines ({error_count} unparseable)")
    return bible_data

def classify_difference(w1_orig, w2_orig, similarity):
    """Enhanced classification for translation analysis."""
    w1 = w1_orig.lower()
    w2 = w2_orig.lower()
    
    if similarity == 0 or not w1 or not w2:
        return 'complete_replacement'
    elif similarity < 0.3:
        return 'major_revision'
    elif similarity < 0.6:
        return 'moderate_change'
    
    # Check specific historical patterns
    if w1.replace('u', 'v') == w2.replace('u', 'v'):
        return 'u_v_substitution'
    elif w1.replace('i', 'j') == w2.replace('i', 'j'):
        return 'i_j_substitution'
    elif 'vv' in w1 and 'w' in w2:
        return 'vv_to_w_modernization'
    elif w1.endswith('eth') and w2.endswith('s'):
        return 'verb_ending_modernization'
    elif similarity < 0.85:
        return 'spelling_modernization'
    else:
        return 'minor_orthography'

def compare_verses(ref, verse_1611, verse_1769):
    """Compare two verses and return all differences."""
    words_1611 = verse_1611['words']
    words_1769 = verse_1769['words']
    differences = []
    
    # Word-by-word comparison
    max_len = max(len(words_1611), len(words_1769))
    for i in range(max_len):
        w1 = words_1611[i] if i < len(words_1611) else None
        w2 = words_1769[i] if i < len(words_1769) else None
        
        if w1 and w2:
            if w1['clean'] != w2['clean']:
                similarity = SequenceMatcher(None, w1['original'], w2['original']).ratio()
                diff_type = classify_difference(w1['original'], w2['original'], similarity)
                
                # Check if locked term affected
                is_locked = (w1['clean'] in LOCKED_TERMS or w2['clean'] in LOCKED_TERMS)
                
                differences.append({
                    'reference': ref,
                    'word_position': i + 1,
                    'word_1611': w1['original'],
                    'word_1769': w2['original'],
                    'diff_type': diff_type,
                    'similarity': round(similarity, 3),
                    'locked_term': 'YES' if is_locked else 'NO',
                    'capitalization_change': 'YES' if w1['has_capital'] != w2['has_capital'] else 'NO'
                })
        elif w1 and not w2:
            # Word in 1611 but not 1769
            is_locked = w1['clean'] in LOCKED_TERMS
            differences.append({
                'reference': ref,
                'word_position': i + 1,
                'word_1611': w1['original'],
                'word_1769': '[OMITTED]',
                'diff_type': 'omission_in_1769',
                'similarity': 0.0,
                'locked_term': 'YES' if is_locked else 'NO',
                'capitalization_change': 'N/A'
            })
        elif w2 and not w1:
            # Word in 1769 but not 1611
            is_locked = w2['clean'] in LOCKED_TERMS
            differences.append({
                'reference': ref,
                'word_position': i + 1,
                'word_1611': '[OMITTED]',
                'word_1769': w2['original'],
                'diff_type': 'addition_in_1769',
                'similarity': 0.0,
                'locked_term': 'YES' if is_locked else 'NO',
                'capitalization_change': 'N/A'
            })
    
    # Punctuation comparison
    if verse_1611['punctuation'] != verse_1769['punctuation']:
        punct_1611 = ''.join(verse_1611['punctuation'])
        punct_1769 = ''.join(verse_1769['punctuation'])
        differences.append({
            'reference': ref,
            'word_position': 0,
            'word_1611': f'[PUNCT: {punct_1611}]',
            'word_1769': f'[PUNCT: {punct_1769}]',
            'diff_type': 'punctuation_change',
            'similarity': 0.0,
            'locked_term': 'NO',
            'capitalization_change': 'N/A'
        })
    
    return differences

def generate_statistics(differences):
    """Generate summary statistics."""
    stats = {
        'total_differences': len(differences),
        'locked_term_changes': sum(1 for d in differences if d['locked_term'] == 'YES'),
        'diff_type_counts': defaultdict(int),
        'verses_affected': len(set(d['reference'] for d in differences))
    }
    
    for diff in differences:
        stats['diff_type_counts'][diff['diff_type']] += 1
    
    return stats

def main():
    print("=" * 70)
    print("KJV 1611 vs 1769 Blayney Revision - Comprehensive Comparison")
    print("=" * 70)
    print()
    
    # Load texts
    data_1611 = parse_bible_text('1611.txt')
    data_1769 = parse_bible_text('1769.txt')
    
    if not data_1611 or not data_1769:
        print("\nERROR: Could not load Bible texts. Please ensure:")
        print("  - 1611.txt exists in the current directory")
        print("  - 1769.txt exists in the current directory")
        print("  - Files are formatted as: Book Chapter:Verse text")
        return
    
    # Find verses present in both
    common_refs = sorted(set(data_1611.keys()) & set(data_1769.keys()))
    only_1611 = sorted(set(data_1611.keys()) - set(data_1769.keys()))
    only_1769 = sorted(set(data_1769.keys()) - set(data_1611.keys()))
    
    print(f"\nDataset Analysis:")
    print(f"  Verses in both editions: {len(common_refs)}")
    print(f"  Verses only in 1611: {len(only_1611)}")
    print(f"  Verses only in 1769: {len(only_1769)}")
    print()
    
    # Compare all common verses
    print("Comparing verses...")
    all_differences = []
    
    for i, ref in enumerate(common_refs, 1):
        if i % 1000 == 0:
            print(f"  Processed {i}/{len(common_refs)} verses...")
        
        diffs = compare_verses(ref, data_1611[ref], data_1769[ref])
        all_differences.extend(diffs)
    
    print(f"  Complete! Found {len(all_differences)} differences.")
    print()
    
    # Generate statistics
    stats = generate_statistics(all_differences)
    
    print("Summary Statistics:")
    print(f"  Total differences: {stats['total_differences']}")
    print(f"  Locked term changes: {stats['locked_term_changes']}")
    print(f"  Verses affected: {stats['verses_affected']}")
    print(f"\n  Difference types:")
    for diff_type, count in sorted(stats['diff_type_counts'].items(), key=lambda x: -x[1]):
        print(f"    {diff_type}: {count}")
    print()
    
    # Write main CSV
    csv_filename = 'kjv_1611_vs_1769_differences.csv'
    headers = ['Reference', 'Word_Position', '1611_Word', '1769_Word', 
               'Diff_Type', 'Similarity_Score', 'Locked_Term', 'Capitalization_Change']
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
            'reference', 'word_position', 'word_1611', 'word_1769',
            'diff_type', 'similarity', 'locked_term', 'capitalization_change'
        ])
        writer.writerow({
            'reference': 'Reference',
            'word_position': 'Word_Position',
            'word_1611': '1611_Word',
            'word_1769': '1769_Word',
            'diff_type': 'Diff_Type',
            'similarity': 'Similarity_Score',
            'locked_term': 'Locked_Term',
            'capitalization_change': 'Capitalization_Change'
        })
        writer.writerows(all_differences)
    
    print(f"✓ Main analysis written to: {csv_filename}")
    
    # Write structural differences CSV
    if only_1611 or only_1769:
        struct_filename = 'kjv_structural_differences.csv'
        with open(struct_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Reference', 'Present_In', 'Text'])
            
            for ref in only_1611:
                writer.writerow([ref, '1611_ONLY', data_1611[ref]['raw_text']])
            for ref in only_1769:
                writer.writerow([ref, '1769_ONLY', data_1769[ref]['raw_text']])
        
        print(f"✓ Structural differences written to: {struct_filename}")
    
    # Write summary statistics CSV
    summary_filename = 'kjv_comparison_summary.csv'
    with open(summary_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Metric', 'Value'])
        writer.writerow(['Total Differences', stats['total_differences']])
        writer.writerow(['Locked Term Changes', stats['locked_term_changes']])
        writer.writerow(['Verses Affected', stats['verses_affected']])
        writer.writerow(['Verses in Both', len(common_refs)])
        writer.writerow(['Verses Only in 1611', len(only_1611)])
        writer.writerow(['Verses Only in 1769', len(only_1769)])
        writer.writerow(['', ''])
        writer.writerow(['Difference Type', 'Count'])
        for diff_type, count in sorted(stats['diff_type_counts'].items()):
            writer.writerow([diff_type, count])
    
    print(f"✓ Summary statistics written to: {summary_filename}")
    print()
    
    # Show sample differences
    if all_differences:
        print("Sample differences (first 20):")
        print("-" * 120)
        for diff in all_differences[:20]:
            locked_marker = " [LOCKED]" if diff['locked_term'] == 'YES' else ""
            print(f"{diff['reference']:20} | {diff['word_1611']:15} → {diff['word_1769']:15} | "
                  f"{diff['diff_type']:25} | Sim: {diff['similarity']:.3f}{locked_marker}")
        print("-" * 120)
    
    print("\n✓ Comparison complete!")

if __name__ == "__main__":
    main()



