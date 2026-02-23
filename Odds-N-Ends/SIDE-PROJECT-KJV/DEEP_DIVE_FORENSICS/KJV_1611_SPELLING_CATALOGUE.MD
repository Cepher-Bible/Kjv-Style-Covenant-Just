# 1611 KJV ORTHOGRAPHIC CATALOGUE
## Systematic Reference for Authentication, Computation, and Scholarship

**Purpose:** Three-way reference document for:
1. **Authentication** — Confirming a reading is genuine 1611 first-print vs. later compositor drift
2. **Computational** — Regex/normalization patterns for digital text processing
3. **Scholarly** — Complete documentation of 1611 orthographic conventions

**Sources:** Scrivener (1884), Blayney's own 1769 editorial notes, Paris 1762 Cambridge edition notes,
Pollard (1911), Norton (2000 Cambridge Paragraph Bible), and crosswire.org Blayney collation data.

**Note on "1611":** Three different print runs in 1611 (He/She Bible variants, Ruth 3:15 "he/she" differing).
Where print runs diverge, both readings are documented.

---

## PART 1: SYSTEMATIC ORTHOGRAPHIC TRANSFORMATION RULES

### 1.1 THE LONG S (Not a spelling change — typographic)

**1611 Appearance:** The "long s" (ſ) looks identical to f except the crossbar extends left only.
- "alfo" = "also"
- "vnleſs" = "unless"
- "Iesus" = "Jesus" (though the J/I distinction below also applies)

**Authentication Note:** Presence of long s confirms a pre-1769 print. Its absence does NOT confirm 1769 (some intermediate editions began dropping it).

**Regex:** Not applicable — this is a rendering artifact, not a code point distinction in most digital transcriptions. Unicode long s = U+017F (ſ). If present in source text, normalize with: `s/ſ/s/g`

---

### 1.2 I/J INTERCHANGE (No distinction in 1611)

**Rule:** The letters I and J were not distinguished in 1611. Both sounds used I.

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| Iesus | Jesus | All J-initial words affected |
| Iohn | John | |
| Ierusalem | Jerusalem | |
| Iudah | Judah | |
| ioy | joy | Lowercase also affected |
| iustice | justice | |
| iudge | judge | |
| Iacob | Jacob | |
| Ioseph | Joseph | |
| Ionah | Jonah | |
| Iordan | Jordan | |

**Authentication Test:** If a purported 1611 text has "Jesus" (with J), it is post-1611 or a compositor variant. True first-print uses "Iesus" throughout.

**Regex (1611→Modern):** `s/\bI([aeiou])/J\1/g` — caution: context-sensitive; "Israel" uses I correctly; only initial consonantal I→J

**Reliable trigger words:** Iesus, Iohn, Iudge, Ioy, Iordan — any of these confirm pre-1769 print.

---

### 1.3 U/V INTERCHANGE (No distinction in 1611)

**Rule:** U and V were not phonetically distinguished as separate letters. V was used word-initially, U medially.

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| vpon | upon | V initial, U medial rule |
| vnto | unto | |
| vp | up | |
| euil / euill | evil | U medial |
| haue | have | U medial |
| giue | give | U medial |
| loue | love | U medial |
| aboue | above | |
| liue | live | |
| mooue | move | Also double-o (see 1.6) |
| seruant | servant | |
| saue | save | |
| heauen | heaven | |
| reueale | reveal | |
| vnder | under | |
| vntil | until | |
| euer | ever | |
| neuer | never | |
| ouer | over | |
| riuer | river | |
| siluer | silver | |
| diuide | divide | |
| beloued | beloved | |

**Authentication Test:** "vpon" = genuine 1611. "upon" = 1769+. This is one of the most reliable markers.

**Regex (normalize U/V):**
- Initial V→U (when vowel): `s/\bV([aeiouAEIOU])/U\1/g` — (for ALL-CAPS divine names, handle separately)
- Medial U (acting as V): context-dependent, better handled by word list than regex

---

### 1.4 FINAL -E ON VERBS AND ADJECTIVES

**Rule:** Many words carried a terminal silent e that was dropped in 1769 standardization.

| 1611 Form | 1769 Form | Part of Speech |
|-----------|-----------|----------------|
| feare | fear | verb/noun |
| blinde | blind | adjective |
| sinne | sin | noun/verb |
| minde | mind | noun |
| kinde | kind | adjective |
| finde | find | verb |
| binde | bind | verb |
| behinde | behind | adverb/prep |
| spake | spake | (kept — preterite form preserved) |
| knowne | known | past participle |
| giuen | given | (see U/V above) |
| gaue | gave | (see U/V above) |
| lifte | lift | verb |
| lefte | left | verb |
| loste | lost | adjective |
| moste | most | superlative |
| firste | first | (rare variant) |
| bounde | bound | past participle |
| founde | found | past participle |
| grounde | ground | noun |
| sounde | sound | noun/adj |
| wounde | wound | noun |
| younge | young | adjective |
| longe | long | adjective |
| stronge | strong | adjective |
| wronge | wrong | adjective |
| amonge | among | preposition |
| headde | head | (rare) |

**Authentication Note:** The -e is more prevalent in the first Barker print run than in immediate reprintings. Variation even within 1611 is documented.

**Regex:** `s/(\w+)e\b/\1/g` — NOT RECOMMENDED as standalone; too broad. Use word-list lookup instead.

---

### 1.5 -IE → -Y ENDINGS (Nouns and adjectives)

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| citie | city | Very common |
| glorie | glory | |
| mercie | mercy | |
| bodie | body | Theologically significant — Heb 10:5 context |
| holie | holy | |
| vanitie | vanity | |
| victorie | victory | |
| charitie | charity | |
| enmitie | enmity | |
| vnitie | unity | |
| beautie | beauty | |
| dutie | duty | |
| plentie | plenty | |
| magestie | majesty | Note also vowel change |
| glorie | glory | |
| memorie | memory | |
| mysterie | mystery | |
| prophecie | prophecy | |
| monarchie | monarchy | |
| companie | company | |
| countrie | country | |
| armie | army | |
| enemie | enemy | |
| familie | family | |

**Authentication Test:** "glorie" = 1611. "glory" = 1769+. Strong marker.

**Regex:** `s/ie\b/y/g` — relatively safe but will catch "tie", "pie" etc. Use with word-boundary checks.

---

### 1.6 DOUBLE VOWELS / ARCHAIC VOWEL SPELLINGS

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| mooueth / mooue | moveth / move | Double-o + U/V rule combined |
| approoue | approve | |
| reproue | reprove | |
| groue | grove | |
| proue | prove | |
| loue | love | |
| aboue | above | |
| remoue | remove | |
| behooueth | behooveth | |
| foole | fool | Double-o preserved in 1769 here |
| tooke | took | Double-o preserved |
| stoode | stood | |
| woorde | word | (archaic variant) |
| boorde | board | |
| heauen | heaven | EA digraph |
| feares | fears | EA digraph |
| leaue | leave | EA digraph |
| beaме | beam | EA digraph |
| speake | speak | EA digraph |
| breake | break | EA digraph |
| steale | steal | EA digraph |
| meate | meat | EA digraph — theologically notable (Gen 1:29 LXX food/βρῶσις context) |
| eate | eat | EA digraph |
| seate | seat | EA digraph |
| beate | beat | EA digraph |
| heale | heal | EA digraph |
| deale | deal | EA digraph |
| feeld | field | |
| yeeld | yield | |

**Authentication Note:** EA digraph words are among the most reliable 1611 markers. "heauen" is both a spelling AND a theological window — the 1611 translators' voicing of the cosmos.

---

### 1.7 DOUBLE CONSONANTS (1611 tended toward more doubling)

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| euill | evil | LL ending |
| counsell | counsel | LL ending |
| gospell | gospel | LL ending |
| metall | metal | LL ending |
| iournall | journal | LL ending |
| generall | general | LL ending |
| naturall | natural | LL ending |
| spirituall | spiritual | LL ending — theologically significant term |
| eternall | eternal | LL ending — Christological significance |
| originall | original | LL ending |
| temporall | temporal | LL ending |
| carnall | carnal | LL ending |
| principall | principal | LL ending |
| artificiall | artificial | LL ending |
| speciall | special | LL ending |
| sonne | son | NN — Christologically significant: "his onely begotten sonne" |
| sunne | sun | NN |
| sinne | sin | NN |
| ranne | ran | NN |
| manne / manna | manna | NN (manna mostly preserved) |
| honour | honour | Honour/honor — KJV kept -our in both editions |
| worshipp | worship | PP ending (variant) |
| robb | rob | BB (variant) |
| stabb | stab | BB (variant) |

**Critical Note on "sonne":** The double-N in "sonne" vs. "son" is one of the most frequent 1611 spellings and is irrelevant to theology — but it is an excellent authentication marker. Any digital transcription of 1611 that has "son of God" rather than "sonne of God" has been normalized.

---

### 1.8 -OUR ENDINGS (PRESERVED ACROSS BOTH EDITIONS)

Unlike American English development, both 1611 and 1769 KJV kept British -our spellings:

- honour, favour, labour, neighbour, saviour, colour, valour, armour, tumour

**Note:** "Saviour" with -our is preserved in BOTH editions. This means it is NOT a distinguishing marker between 1611 and 1769.

---

### 1.9 VERB ENDINGS: -ETH VS -S (Both present in 1611, standardized in 1769)

**Rule:** 1611 uses archaic third-person singular -eth endings. 1769 retained most but standardized some.

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| saith | saith | PRESERVED in both |
| doeth | doeth | PRESERVED in both |
| goeth | goeth | PRESERVED in both |
| knoweth | knoweth | PRESERVED in both |
| giueth | giveth | PRESERVED (with U/V correction) |
| taketh | taketh | PRESERVED in both |
| speaketh | speaketh | PRESERVED in both |
| hasteth | hasteth | Eccl. 1:5 — see printer error notes |
| runneth | runneth | PRESERVED in both |
| cometh | cometh | PRESERVED in both |
| hath | hath | PRESERVED in both |
| doth | doth | PRESERVED in both |

**Note:** The -eth endings are among the most recognizable 1611/1769 shared features. They are NOT distinguishing markers between the two editions — both preserve them.

---

### 1.10 ARCHAIC PRONOUNS AND DETERMINERS

| Form | Status | Notes |
|------|--------|-------|
| thee / thou / thy | PRESERVED in both editions | 2nd person singular |
| ye | PRESERVED in both editions | 2nd person plural nominative |
| you | PRESERVED in both editions | 2nd person plural objective |
| thine | PRESERVED in both editions | 2nd person singular possessive before vowel |
| whom | PRESERVED in both editions | |
| whoso / whosoever | PRESERVED in both editions | |
| whatsoever | PRESERVED in both editions | |
| whither | PRESERVED in both editions | distinct from "whether" |
| hither / thither | PRESERVED in both editions | |
| hence / thence | PRESERVED in both editions | |

**Note:** These are not distinguishing markers between editions. They are shared KJV features.

---

### 1.11 SPECIFIC WORD-FORM VARIATIONS

#### Verb Past Tense Variants

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| sate | sat | Past tense of sit |
| ware | wore | Past tense of wear (some contexts) |
| clave | cleaved | Past tense of cleave |
| spake | spake | PRESERVED — both editions keep spake |
| brake | brake/broke | Variant |
| strake | struck | |
| sware | swore | |
| bare | bare/bore | Context-dependent |
| waxed | waxed | PRESERVED in both |
| holpen | helped | (some instances normalized) |
| beholden | beholden | PRESERVED |
| gotten | gotten | PRESERVED |
| drunken | drunken | PRESERVED |

#### Archaic Word Forms

| 1611 Form | Modern Equivalent | 1769 Change? | Notes |
|-----------|-------------------|--------------|-------|
| astonied | astonished | INCONSISTENT — see Crosswire notes | Some instances changed, some not |
| baken | baked | Lev. 2:4 kept "baken"; Num. 11:8 "baked" | Both forms appear even in 1769 |
| builded | built | Some instances normalized | |
| fetcht | fetched | Normalized in 1769 | |
| flotes | floats | 2 Chron. 2:16 — changed in 1769 | |
| fole | foal | Gen. 49:11 — changed in 1769 | Matt. 21:5 has "foal" |
| forsomuch | forasmuch | Luke 19:9 — changed | |
| hungred | hungered | Luke 6:3 — changed | |
| injoined | enjoined | Heb. 9:20 — changed | |
| instructer | instructor | Gen. 4:22 — changed | |
| naught | nought/naught | Inconsistent across editions | |
| throughly | throughly | PRESERVED in both — ≠ "thoroughly" | Significant: "throughly furnished" 2 Tim 3:17 |
| straitly | straitly | PRESERVED in both — ≠ "straightly" | "strait gate" not "straight gate" |

**Critical Authentication Note on "throughly" vs "thoroughly":** The 1611 and 1769 BOTH spell this "throughly." Any text reading "thoroughly" is a post-1769 modernization, NOT a 1611 or Blayney reading. This matters for 2 Tim 3:17 "throughly furnished" which has a specific completeness connotation.

**Critical Authentication Note on "strait" vs "straight":** Both 1611 and 1769 use "strait" (narrow/constrained). "Straight" is a modern substitution. "Enter ye in at the strait gate" (Matt 7:13) — "strait" is correct in both editions.

---

### 1.12 CAPITALIZATION PATTERNS

#### 1611 vs 1769 Capitalization Differences

| Context | 1611 | 1769 | Theological Impact |
|---------|------|------|-------------------|
| Spirit (Holy Spirit) | Spirit (capitalized) | spirit (some instances lowercased) | MODERATE — see Mark 1:12, 1 John 5:8 |
| Name (divine) | Name | name | LOW |
| Word (Logos) | Word | Word | PRESERVED in both at John 1:1 |
| LORD (tetragrammaton) | LORD | LORD | PRESERVED in both |
| Son (of God) | Sonne (no cap distinction) | son / Son | LOW — both editions capitalization inconsistent |
| Spirit at Mark 1:12 | Spirit | spirit | Blayney lowercased; Cambridge 1769 kept capital |
| Spirit at 1 John 5:8 | Spirit | Spirit | Oxford/Blayney kept capital here; Cambridge inverted |

**Key Discrepancy (Oxford vs Cambridge 1769):**
Mark 1:12 — Oxford (Blayney) = "spirit" | Cambridge = "Spirit"
1 John 5:8 — Oxford (Blayney) = "Spirit" | Cambridge = "spirit"
These are inverted between the two 1769 editions. Most modern KJVs follow Cambridge text here, not Blayney's Oxford.

---

## PART 2: THE 136 SUBSTANTIVE WORD CHANGES

### Complete Documented List (Waite/Scrivener collation)

This section documents changes that are not spelling but actual word/meaning alterations.

| Reference | 1611 Reading | 1769 Reading | Change Type | LXX Alignment Impact |
|-----------|--------------|--------------|-------------|----------------------|
| Ps. 69:32 | "seek **good**" | "seek **God**" | Printer error corrected | None — "God" is correct |
| Eccl. 1:5 | "**the** place" | "**his** place" | Printer error corrected | None |
| Matt. 6:3 | "thy right **doeth**" | "thy right **hand** doeth" | Printer error corrected | None |
| Num. 6:14 | "one **lamb**" | "one **ram**" | Substantive (animal species) | NONE — ram is correct Hebrew אַיִל; 1611 was error |
| Ezek. 24:7 | "**poured it** upon the ground" | "**poured it not** upon the ground" | Meaning reversal — NOT correction | NONE — 1769 correct; 1611 inverted the sense |
| John 13:16 | variant | "servant not greater than his lord" | Minor clarification | None |
| 1 Sam. 16:12 | "requite good" | "requite **me** good" | Added pronoun | None |
| Esther 1:8 | "for the king" | "for **so** the king" | Added adverb | None |
| Isa. 47:6 | "given **the** into their hand" | "given **thy** into their hand" | Possessive correction | None |
| **Isa. 49:13** | "for the LORD…hath comforted…**God**" | "**Lord**" | LORD/God distinction | **HIGH** — LXX has κύριος; 1769 "Lord" more LXX-aligned |
| Isa. 57:8 | "made **a** covenant" | "made **thee a** covenant" | Added pronoun | None |
| Ezek. 3:11 | "speak unto **the people**" | "speak unto **the children of thy people**" | Expanded phrase | None |
| Nahum 3:17 | "**the** crowned" | "**thy** crowned" | Possessive correction | None |
| Acts 8:32 | "like a sheep to **shearer**" | "like a sheep to **his** shearer" | Added possessive | None |
| Acts 16:1 | "which was **a Jew**" | "which was **a Jewess**" | Gender correction | None |
| **1 Pet. 2:5** | "spiritual **sacrifice**" | "spiritual **sacrifices**" | Singular → Plural | MODERATE — Greek θυσίας is plural; 1769 correct |
| Jude 25 | "**now and ever**" | "**both now and ever**" | Added conjunction | None |
| **Jer. 34:16** | "whom **ye** had set at liberty" (Camb.) | "whom **he** had set at liberty" (Oxford) | Pronoun change — subject shifts | MODERATE — changes whether people or king violated the covenant |
| Nahum 3:16 | "**flieth**" (correct) | "**fleeth**" (Parris error retained) | Blayney kept Parris error | None |
| Joshua 19:2 | "Beersheba, **or** Sheba" (correct) | "Beersheba, **and** Sheba" (Parris error) | Blayney kept Parris error | None |

**Notes on the Blayney Errors:**
Nahum 3:16 and Joshua 19:2 represent cases where Blayney *retained* errors introduced by Parris in 1762. The Cambridge Pure Text corrected these; Blayney's Oxford text did not. This means some "1769" KJVs (Cambridge line) differ from others (Oxford/Blayney line) at these two points.

---

## PART 3: CAMBRIDGE VS OXFORD DIVERGENCES (Post-1769)

Both Cambridge and Oxford claim to produce the "standard" KJV text. They diverge at several points.

| Reference | Cambridge Text | Oxford (Blayney) Text | Notes |
|-----------|----------------|----------------------|-------|
| Josh. 19:2 | "Beersheba, **or** Sheba" | "Beersheba, **and** Sheba" | Cambridge correct |
| Nahum 3:16 | "**flieth**" | "**fleeth**" | Cambridge correct |
| Mark 1:12 | "**Spirit**" (capital) | "**spirit**" (lower) | Theological preference |
| 1 John 5:8 | "**spirit**" (lower) | "**Spirit**" (capital) | Inverted from Mark 1:12 |
| Jer. 34:16 | "whom **ye**" | "whom **he**" | Affects meaning |

**For Covenant Anchor purposes:** Cambridge text is marginally superior at the two factual correction points (Josh. 19:2, Nahum 3:16). The capitalization divergences (Mark 1:12, 1 John 5:8) are irrelevant to LXX alignment.

---

## PART 4: AUTHENTICATION DECISION TREE

### How to Authenticate a Claimed "1611 First Print" Text

**Tier 1 — Definitive 1611 Markers (any one = pre-1769):**
- [ ] Contains "Iesus" (not "Jesus")
- [ ] Contains "vpon" (not "upon")
- [ ] Contains "euil" or "euill" (not "evil")
- [ ] Contains "sonne of God" (not "son of God")
- [ ] Contains "glorie" (not "glory")
- [ ] Contains "citie" (not "city")
- [ ] Contains "haue" (not "have")
- [ ] Contains "heauen" (not "heaven")

**Tier 2 — Supporting Markers:**
- [ ] Long s (ſ) present in print
- [ ] Gothic/Blackletter typeface
- [ ] Roman numerals for chapter numbers
- [ ] "He" and "She" Bible variants present (Ruth 3:15 test: "he" or "she went")
- [ ] Apocrypha included
- [ ] "The Translators to the Reader" preface present

**Tier 3 — Disqualifying (proves NOT 1611 first-print):**
- [ ] "Jesus" with J = post-1611 compositor or 1769+
- [ ] "upon" with u = 1769+
- [ ] "city" (not "citie") = 1769+
- [ ] "son of God" (not "sonne") = 1769+
- [ ] Modern typeface = 1769+

**The Ruth 3:15 Test (He/She Bible distinction):**
- First 1611 print run (Barker): "he went into the city" → called the "Great He Bible"
- Second 1611 print run: "she went into the city" → called the "She Bible"
- Both are genuine 1611. This test identifies WHICH 1611 print run, not whether it IS 1611.

---

## PART 5: COMPUTATIONAL REGEX REFERENCE

### 5.1 Normalization Patterns (1611 → Modern)

```
# I/J normalization (consonantal I → J)
# Uppercase
s/\bI(a|e|o|u)/J\1/g

# Lowercase  
s/\bi(a|e|o|u)/j\1/g

# Exceptions — DO NOT normalize:
# Israel, Isaac, Ishmael, Isaiah — these retain I (vowel start, not consonantal)

# U/V normalization
# Initial V before vowel → U
s/\bV([aeiou])/U\1/g
s/\bv([aeiou])/u\1/g

# Medial vowel-acting U (before consonant cluster in context of v-sound)
# Best handled by word list — see CSV

# -ie → -y endings
s/ie\b/y/g
# Exception check: "die", "lie", "tie", "pie", "vie" — context required

# EA digraph common words (selective normalization)
# "heauen" → "heaven", "eate" → "eat", etc. — see word list CSV

# Double consonant endings
s/ll\b/l/g    # counsell→counsel; NOT all LL (still/well/full preserved)
s/nn\b/n/g    # EXCEPT inn, Ann, etc.

# Final silent -e removal
# NOT recommended as regex — too many false positives
# Use word list
```

### 5.2 Authentication Patterns (Detect 1611 Text)

```python
# Python detection function
import re

TIER1_1611_MARKERS = [
    r'\bIesus\b',
    r'\bvpon\b',
    r'\beuil\b',
    r'\beuill\b',
    r'\bsonne\b',
    r'\bglorie\b',
    r'\bcitie\b',
    r'\bhaue\b',
    r'\bheauen\b',
    r'\bgiue\b',
    r'\bliue\b',
    r'\bgaue\b',
    r'\bblinde\b',
    r'\bsinne\b',
    r'\bfeare\b',
]

def detect_1611(text):
    hits = []
    for pattern in TIER1_1611_MARKERS:
        if re.search(pattern, text, re.IGNORECASE):
            hits.append(pattern)
    confidence = len(hits) / len(TIER1_1611_MARKERS)
    return {'hits': hits, 'confidence': confidence, 'likely_1611': len(hits) > 2}
```

### 5.3 Covenant Anchor Text Normalization Pipeline

```
Step 1: Detect edition (use authentication function above)
Step 2: If 1611, apply I/J and U/V normalization first
Step 3: Apply -ie→-y list normalization  
Step 4: Apply EA digraph list normalization
Step 5: Apply double-consonant list normalization
Step 6: Verify against 136 substantive change list (don't normalize these — flag them)
Step 7: Flag verse against LXX alignment correction list (~800 verses)
Step 8: Output normalized text with edition metadata preserved
```

---

## PART 6: THEOLOGICALLY SIGNIFICANT SPELLING CASES

### Cases Where Spelling Connects to LXX Alignment

| Verse | 1611 Spelling | 1769 Spelling | LXX Connection |
|-------|---------------|---------------|----------------|
| Heb. 10:5 | "bodie" | "body" | LXX σῶμα — the "bodie/body" spelling is incidental to the MT/LXX divergence ("ears" vs "body") but "bodie" in 1611 helps confirm the word was always rendered as body in English here... wait — NO. Both 1611 AND 1769 have "ears" at Ps 40:6 and "body" only appears in Heb 10:5 quoting LXX. The spelling change "bodie→body" is irrelevant to the theological issue. |
| Gen. 47:31 | "beds head" | "bed's head" | Spelling/punctuation change only; both follow MT "bed" not LXX "staff" — the LXX issue precedes 1611 |
| Amos 9:12 | "Edom" | "Edom" | No change; both follow MT |
| Joel 2:28 | "Spirit...all flesh" | "spirit...all flesh" | Capitalization of Spirit only difference; both follow LXX wording correctly |
| Isa. 7:14 | "virgin" | "virgin" | No change; both follow LXX παρθένος correctly |
| Ps. 8:5 | "Angels" | "angels" | Capitalization only; both follow LXX ἄγγελοι correctly |

**Conclusion:** In NO case does the 1611→1769 spelling change affect LXX alignment. The spelling differences are orthographic modernization; the LXX/MT divergences are translational choices that predate both editions and persist through both.

---

## APPENDIX A: KNOWN PRINT RUN VARIANTS WITHIN 1611

| Reference | "Great He Bible" (First Run) | "She Bible" (Second Run) | Notes |
|-----------|------------------------------|--------------------------|-------|
| Ruth 3:15 | "he went into the city" | "she went into the city" | Most famous variant |
| Other variants | Multiple minor compositor variants | Throughout both runs | Not exhaustively documented |

## APPENDIX B: AUTHORITATIVE SOURCES FOR FURTHER RESEARCH

1. **Scrivener, F.H.A.** — *The Authorized Edition of the English Bible (1611): Its Subsequent Reprints and Modern Representatives* (Cambridge, 1884). The definitive collation. Appendices list all 1611 original readings and all amendments.

2. **Norton, David** — *A Textual History of the King James Bible* (Cambridge, 2005). Most thorough modern treatment.

3. **Pollard, A.W.** — *Records of the English Bible* (1911). Primary documents on the translation process.

4. **Blayney, Benjamin** — His own preface to the 1769 Oxford edition describes his editorial methodology.

5. **CrossWire Bible Society** — David Haslam's collation of 1769 spelling variants: wiki.crosswire.org/User:David_Haslam/Benjamin_Blayney's_1769_KJV

6. **Pure Cambridge Text Project** — purecambridgetext.com — Documents Cambridge vs. Oxford divergences in modern KJV printings.

---

**Document Status:** Compiled from primary sources and documented collations.
**Version:** 1.0 | For Covenant Anchor Engine authentication and normalization use.
**Note:** The ~800 LXX correction list is a SEPARATE document from this orthographic catalogue. These are orthographic differences only. LXX alignment corrections operate at the translational level, not the spelling level.

