#!/usr/bin/env python3
"""
KJV 1611 Spelling Peculiarities Catalogue
Identifies authentic 1611 orthographic patterns vs 1769 modernizations
For establishing textual baseline accuracy
"""

import csv
import re
from difflib import SequenceMatcher
from collections import defaultdict
import json

def parse_bible_text(filename):
    """Parse Bible text into structured dict."""
    bible_data = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                
                # Format: "Book Chapter:Verse text"
                match = re.match(r'^(.*?)\s+(\d+):(\d+)\s+(.*)$', line)
                
                if match:
                    book = match.group(1).strip().replace(' ', '_')
                    chapter = match.group(2)
                    verse = match.group(3)
                    text = match.group(4)
                    ref = f"{book}.{chapter}.{verse}"
                    
                    # Extract words with position metadata
                    words = []
                    for word_match in re.finditer(r'\b(\w+)\b', text):
                        word = word_match.group(1)
                        words.append({
                            'original': word,
                            'clean': word.lower(),
                            'position': word_match.start()
                        })
                    
                    bible_data[ref] = {
                        'words': words,
                        'raw_text': text
                    }
    
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found!")
        return {}
    
    return bible_data

def classify_spelling_pattern(word_1611, word_1769):
    """
    Classify the specific spelling difference pattern.
    Returns pattern type and specific transformation.
    """
    w1 = word_1611.lower()
    w2 = word_1769.lower()
    
    if w1 == w2:
        return None, None
    
    # Pattern detection (ordered by specificity)
    
    # 1. U/V interchange patterns
    if w1.replace('u', 'v') == w2 or w1 == w2.replace('u', 'v'):
        return 'u_v_interchange', f"{word_1611} → {word_1769}"
    
    if w1.replace('v', 'u') == w2 or w1 == w2.replace('v', 'u'):
        return 'v_u_interchange', f"{word_1611} → {word_1769}"
    
    # 2. I/J interchange
    if w1.replace('i', 'j') == w2 or w1 == w2.replace('i', 'j'):
        return 'i_j_interchange', f"{word_1611} → {word_1769}"
    
    if w1.replace('j', 'i') == w2 or w1 == w2.replace('j', 'i'):
        return 'j_i_interchange', f"{word_1611} → {word_1769}"
    
    # 3. VV to W
    if 'vv' in w1 and 'w' in w2:
        return 'vv_to_w', f"{word_1611} → {word_1769}"
    
    # 4. Final -e addition/removal
    if w1 + 'e' == w2:
        return 'final_e_added', f"{word_1611} → {word_1769}"
    if w1 == w2 + 'e':
        return 'final_e_removed', f"{word_1611} → {word_1769}"
    
    # 5. Double consonant changes
    if re.sub(r'([bcdfghjklmnpqrstvwxyz])\1', r'\1', w1) == w2:
        return 'double_consonant_simplified', f"{word_1611} → {word_1769}"
    if w1 == re.sub(r'([bcdfghjklmnpqrstvwxyz])\1', r'\1', w2):
        return 'double_consonant_added', f"{word_1611} → {word_1769}"
    
    # 6. Specific archaic endings
    if w1.endswith('eth') and w2.endswith('s'):
        return 'eth_to_s_ending', f"{word_1611} → {word_1769}"
    
    if w1.endswith('est') and w2.endswith('s'):
        return 'est_to_s_ending', f"{word_1611} → {word_1769}"
    
    # 7. Vowel changes
    vowel_pairs = [
        ('ie', 'y'), ('ei', 'i'), ('ou', 'o'), ('oo', 'o'),
        ('ae', 'e'), ('oe', 'e'), ('ea', 'ee')
    ]
    for old_v, new_v in vowel_pairs:
        if old_v in w1 and new_v in w2:
            if w1.replace(old_v, new_v) == w2:
                return f'{old_v}_to_{new_v}', f"{word_1611} → {word_1769}"
    
    # 8. Specific common 1611 spellings
    known_1611_patterns = {
        'forme': 'form',
        'voyd': 'void',
        'heauen': 'heaven',
        'giue': 'give',
        'haue': 'have',
        'beleeve': 'believe',
        'receiue': 'receive',
    }
    
    for pattern_1611, pattern_1769 in known_1611_patterns.items():
        if pattern_1611 in w1 and pattern_1769 in w2:
            return 'known_1611_archaic', f"{word_1611} → {word_1769}"
    
    # 9. Capitalization only
    if w1 == w2 and word_1611 != word_1769:
        return 'capitalization_only', f"{word_1611} → {word_1769}"
    
    # 10. Calculate similarity for remaining
    similarity = SequenceMatcher(None, w1, w2).ratio()
    
    if similarity > 0.85:
        return 'minor_variant', f"{word_1611} → {word_1769}"
    elif similarity > 0.6:
        return 'moderate_variant', f"{word_1611} → {word_1769}"
    else:
        return 'major_variant', f"{word_1611} → {word_1769}"

def build_spelling_catalogue(data_1611, data_1769):
    """
    Build comprehensive catalogue of spelling patterns.
    """
    
    catalogue = {
        'patterns': defaultdict(list),
        'word_mappings': defaultdict(set),
        'statistics': defaultdict(int),
        'examples_by_pattern': defaultdict(list)
    }
    
    common_refs = sorted(set(data_1611.keys()) & set(data_1769.keys()))
    
    for ref in common_refs:
        words_1611 = data_1611[ref]['words']
        words_1769 = data_1769[ref]['words']
        
        max_len = max(len(words_1611), len(words_1769))
        
        for i in range(max_len):
            if i >= len(words_1611) or i >= len(words_1769):
                continue
                
            w1 = words_1611[i]['original']
            w2 = words_1769[i]['original']
            
            if w1.lower() == w2.lower() and w1 == w2:
                continue  # Identical
            
            pattern, transformation = classify_spelling_pattern(w1, w2)
            
            if pattern:
                catalogue['patterns'][pattern].append({
                    'reference': ref,
                    'position': i + 1,
                    '1611': w1,
                    '1769': w2,
                    'transformation': transformation
                })
                
                catalogue['word_mappings'][w1.lower()].add(w2.lower())
                catalogue['statistics'][pattern] += 1
                
                # Store representative examples (max 5 per pattern)
                if len(catalogue['examples_by_pattern'][pattern]) < 5:
                    catalogue['examples_by_pattern'][pattern].append({
                        'reference': ref,
                        '1611': w1,
                        '1769': w2
                    })
    
    return catalogue

def generate_1611_peculiarities_reference(catalogue):
    """
    Generate a reference guide of 1611 spelling peculiarities.
    """
    
    peculiarities = []
    
    # Group by pattern type
    for pattern, examples in catalogue['examples_by_pattern'].items():
        count = catalogue['statistics'][pattern]
        
        peculiarities.append({
            'pattern': pattern,
            'frequency': count,
            'description': get_pattern_description(pattern),
            'examples': examples,
            'rule': get_pattern_rule(pattern)
        })
    
    # Sort by frequency
    peculiarities.sort(key=lambda x: -x['frequency'])
    
    return peculiarities

def get_pattern_description(pattern):
    """Get human-readable description of pattern."""
    descriptions = {
        'u_v_interchange': "U/V interchange (1611 used u/v interchangeably)",
        'v_u_interchange': "V/U interchange (reverse pattern)",
        'i_j_interchange': "I/J interchange (1611 used i/j interchangeably)",
        'j_i_interchange': "J/I interchange (reverse pattern)",
        'vv_to_w': "Double-V (vv) modernized to W",
        'final_e_added': "Silent E added in modernization",
        'final_e_removed': "Final E removed in modernization",
        'double_consonant_simplified': "Double consonant simplified",
        'double_consonant_added': "Consonant doubled in modernization",
        'eth_to_s_ending': "Archaic -eth verb ending modernized to -s",
        'est_to_s_ending': "Archaic -est verb ending modernized to -s",
        'ie_to_y': "IE vowel digraph changed to Y",
        'known_1611_archaic': "Known 1611 archaic spelling pattern",
        'capitalization_only': "Capitalization change only",
        'minor_variant': "Minor spelling variant (>85% similar)",
        'moderate_variant': "Moderate spelling variant (60-85% similar)",
        'major_variant': "Major spelling variant (<60% similar)"
    }
    return descriptions.get(pattern, f"Pattern: {pattern}")

def get_pattern_rule(pattern):
    """Get the orthographic rule for this pattern."""
    rules = {
        'u_v_interchange': "1611: Letters u and v were positional variants (v at start, u in middle)",
        'i_j_interchange': "1611: Letters i and j were positional variants (j at start, i elsewhere)",
        'vv_to_w': "1611: W was represented as double-v (vv or uu)",
        'final_e_added': "1769: Added silent E for modern orthography",
        'eth_to_s_ending': "1611: Third-person singular verbs used -eth (maketh, goeth)",
        'known_1611_archaic': "1611: Common archaic spellings standardized by 1769"
    }
    return rules.get(pattern, "Pattern-specific orthographic variance")

def main():
    print("=" * 80)
    print("KJV 1611 SPELLING PECULIARITIES CATALOGUE")
    print("Establishing Authentic 1611 Orthographic Baseline")
    print("=" * 80)
    print()
    
    # Load texts
    print("Loading Bible texts...")
    data_1611 = parse_bible_text('1611.txt')
    data_1769 = parse_bible_text('1769.txt')
    
    if not data_1611 or not data_1769:
        print("ERROR: Could not load Bible texts.")
        return
    
    print(f"  1611: {len(data_1611)} verses loaded")
    print(f"  1769: {len(data_1769)} verses loaded")
    print()
    
    # Build catalogue
    print("Analyzing spelling patterns...")
    catalogue = build_spelling_catalogue(data_1611, data_1769)
    
    print(f"  Found {sum(catalogue['statistics'].values())} total spelling differences")
    print(f"  Identified {len(catalogue['statistics'])} distinct pattern types")
    print()
    
    # Generate peculiarities reference
    peculiarities = generate_1611_peculiarities_reference(catalogue)
    
    # Output 1: Detailed Catalogue CSV
    print("Generating detailed catalogue...")
    with open('1611_spelling_catalogue.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Pattern_Type', 'Reference', 'Word_Position', 
            '1611_Spelling', '1769_Spelling', 'Transformation'
        ])
        
        for pattern, instances in sorted(catalogue['patterns'].items()):
            for inst in instances:
                writer.writerow([
                    pattern,
                    inst['reference'],
                    inst['position'],
                    inst['1611'],
                    inst['1769'],
                    inst['transformation']
                ])
    
    print("  ✓ 1611_spelling_catalogue.csv")
    
    # Output 2: Pattern Summary
    with open('1611_pattern_summary.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Pattern_Type', 'Frequency', 'Description', 'Orthographic_Rule',
            'Example_1611', 'Example_1769'
        ])
        
        for pec in peculiarities:
            example = pec['examples'][0] if pec['examples'] else {'1611': '', '1769': ''}
            writer.writerow([
                pec['pattern'],
                pec['frequency'],
                pec['description'],
                pec['rule'],
                example['1611'],
                example['1769']
            ])
    
    print("  ✓ 1611_pattern_summary.csv")
    
    # Output 3: Word Mapping Dictionary
    with open('1611_to_1769_word_mapping.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['1611_Word', '1769_Equivalents', 'Variant_Count'])
        
        for word_1611, words_1769 in sorted(catalogue['word_mappings'].items()):
            writer.writerow([
                word_1611,
                ' | '.join(sorted(words_1769)),
                len(words_1769)
            ])
    
    print("  ✓ 1611_to_1769_word_mapping.csv")
    
    # Output 4: 1611 Authenticity Reference Guide
    with open('1611_authenticity_guide.json', 'w', encoding='utf-8') as f:
        guide = {
            'metadata': {
                'purpose': 'Reference for identifying authentic 1611 readings',
                'verses_analyzed': len(data_1611),
                'total_differences': sum(catalogue['statistics'].values()),
                'pattern_types': len(catalogue['statistics'])
            },
            'patterns': []
        }
        
        for pec in peculiarities:
            guide['patterns'].append({
                'type': pec['pattern'],
                'frequency': pec['frequency'],
                'description': pec['description'],
                'rule': pec['rule'],
                'examples': pec['examples']
            })
        
        json.dump(guide, f, indent=2, ensure_ascii=False)
    
    print("  ✓ 1611_authenticity_guide.json")
    print()
    
    # Console report
    print("=" * 80)
    print("TOP 15 SPELLING PATTERNS (1611 → 1769)")
    print("=" * 80)
    print()
    
    for i, pec in enumerate(peculiarities[:15], 1):
        print(f"{i}. {pec['pattern'].upper()}")
        print(f"   Frequency: {pec['frequency']}")
        print(f"   Description: {pec['description']}")
        
        if pec['examples']:
            examples = pec['examples'][:3]
            print(f"   Examples:")
            for ex in examples:
                print(f"     • {ex['1611']} → {ex['1769']} ({ex['reference']})")
        
        print()
    
    # Statistics
    print("=" * 80)
    print("CATALOGUE STATISTICS")
    print("=" * 80)
    print(f"Total spelling differences: {sum(catalogue['statistics'].values())}")
    print(f"Unique 1611 word forms: {len(catalogue['word_mappings'])}")
    print(f"Pattern types identified: {len(catalogue['statistics'])}")
    print()
    
    # Most variable words
    print("Most variable 1611 words (multiple 1769 equivalents):")
    variable_words = sorted(
        [(w, variants) for w, variants in catalogue['word_mappings'].items() if len(variants) > 1],
        key=lambda x: -len(x[1])
    )[:10]
    
    for word_1611, variants in variable_words:
        print(f"  {word_1611} → {', '.join(sorted(variants))}")
    
    print()
    print("✓ Analysis complete!")

if __name__ == "__main__":
    main()

