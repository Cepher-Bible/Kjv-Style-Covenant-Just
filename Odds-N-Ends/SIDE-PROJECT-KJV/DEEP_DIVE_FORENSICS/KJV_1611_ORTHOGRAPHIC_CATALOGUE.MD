# KJV 1611 ORTHOGRAPHIC CATALOGUE
## Complete Reference: Spelling, Authentication, Computation, and Substantive Changes

**Scope:** Everything documented about 1611 vs 1769 KJV textual differences, organized for:
1. **Authentication** - confirm a reading is genuine 1611 first-print vs. later compositor drift
2. **Computation** - regex/normalization patterns for digital text processing
3. **Scholarship** - complete orthographic conventions documented with sources
4. **Covenant Anchor Integration** - LXX alignment flags embedded throughout

**Sources:** Scrivener (1884), Blayney 1769 editorial preface, Paris 1762 Cambridge edition notes,
Pollard (1911), Norton (2005 Textual History of the KJV), CrossWire Bible Society Blayney collation
(wiki.crosswire.org), Pure Cambridge Text Project (purecambridgetext.com), Waite collation
(KJB of 1611 Compared to the KJB of the 1917 Old Scofield, BFT1294).

**Key Finding:** Blayney's 1769 revision introduced ZERO degradation to LXX alignment. All ~800 LXX
correction needs exist identically in both 1611 and 1769. The orthographic differences documented
here are translationally inert for Covenant Anchor purposes -- with the single exception of Isa 49:13
where Blayney's "Lord" is MORE LXX-aligned than 1611's "God."

---

## PART 1: SYSTEMATIC ORTHOGRAPHIC TRANSFORMATION RULES

### 1.1 The Long S

The long s (Unicode U+017F) is NOT a spelling change -- it is a typographic artifact.
It looks identical to the letter f except the crossbar extends left only.

Examples: "alfo" = "also" | "vnless" = "unless" | "Iesus" = "Jesus"

**Authentication:** Presence of long s confirms pre-1769 print. Its absence does NOT confirm 1769 --
some intermediate editions began dropping it earlier.

Normalize in code with: `text.replace('\u017f', 's')`

---

### 1.2 I / J Interchange

I and J were not distinguished in 1611. Both sounds used I.

| 1611 Form | 1769 Form | Regex Pattern |
|-----------|-----------|---------------|
| Iesus | Jesus | `\bIesus\b` |
| Iohn | John | `\bIohn\b` |
| Ierusalem | Jerusalem | `\bIerusalem\b` |
| Iudah | Judah | `\bIudah\b` |
| Iacob | Jacob | `\bIacob\b` |
| Ioseph | Joseph | `\bIoseph\b` |
| Ionah | Jonah | `\bIonah\b` |
| Iordan | Jordan | `\bIordan\b` |
| ioy | joy | `\bioy\b` |
| iustice | justice | `\biustice\b` |

**Authentication test:** Any purported 1611 text containing "Jesus" (with J) is post-1611 or a
compositor variant. True first-print uses "Iesus" throughout. TIER 1 marker.

**General regex:** `s/\bI([aeou])/J\1/g` -- caution: context-sensitive.
"Israel", "Isaac", "Isaiah" retain I (vowel-initial, not consonantal). Use word list for safety.

---

### 1.3 U / V Interchange

U and V were not phonetically distinguished. V used word-initially; U used medially.

| 1611 Form | 1769 Form | Regex Pattern |
|-----------|-----------|---------------|
| vpon | upon | `\bvpon\b` |
| vnto | unto | `\bvnto\b` |
| vp | up | `\bvp\b` |
| vnder | under | `\bvnder\b` |
| euil | evil | `\beuil\b` |
| euill | evil | `\beuill\b` |
| haue | have | `\bhaue\b` |
| giue | give | `\bgiue\b` |
| loue | love | `\bloue\b` |
| aboue | above | `\baboue\b` |
| liue | live | `\bliue\b` |
| seruant | servant | `\bseruant\b` |
| saue | save | `\bsaue\b` |
| heauen | heaven | `\bheauen\b` |
| reueale | reveal | `\breueale?\b` |
| euer | ever | `\beuer\b` |
| neuer | never | `\bneuer\b` |
| ouer | over | `\bouer\b` |
| riuer | river | `\briuer\b` |
| siluer | silver | `\bsiluer\b` |
| diuide | divide | `\bdiuide\b` |
| beloued | beloved | `\bbeloued\b` |
| gaue | gave | `\bgaue\b` |

**Authentication test:** "vpon" = genuine 1611. "upon" = 1769+.
One of the most reliable single-word markers alongside "Iesus." TIER 1 marker.

---

### 1.4 -IE to -Y Endings

| 1611 Form | 1769 Form | Regex Pattern |
|-----------|-----------|---------------|
| citie | city | `\bcitie\b` |
| glorie | glory | `\bglorie\b` |
| mercie | mercy | `\bmercie\b` |
| bodie | body | `\bbodie\b` |
| holie | holy | `\bholie\b` |
| vanitie | vanity | `\bvanitie\b` |
| victorie | victory | `\bvictorie\b` |
| charitie | charity | `\bcharitie\b` |
| enmitie | enmity | `\benmitie\b` |
| vnitie | unity | `\bvnitie\b` |
| beautie | beauty | `\bbeautie\b` |
| mysterie | mystery | `\bmysterie\b` |
| prophecie | prophecy | `\bprophecie\b` |
| companie | company | `\bcompanie\b` |
| countrie | country | `\bcountrie\b` |
| armie | army | `\barmie\b` |
| enemie | enemy | `\benemie\b` |
| familie | family | `\bfamilie\b` |

**Authentication test:** "glorie" = 1611. "glory" = 1769+. Strong TIER 1 marker.

---

### 1.5 EA Digraph Words

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| heauen | heaven | EA + U/V combined -- most reliable digraph marker |
| eate | eat | |
| meate | meat | "meat" = food in both eds; spelling change only |
| speake | speak | |
| breake | break | |
| steale | steal | |
| beate | beat | |
| heale | heal | |
| deale | deal | |
| leaue | leave | |
| feare | fear | |

---

### 1.6 Double Vowel / Archaic Vowel Patterns

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| mooueth | moveth | Double-O + U/V combined |
| approoue | approve | |
| reproue | reprove | |
| prooue | prove | |
| remoue | remove | |
| stoode | stood | |
| tooke | took | Double-O preserved in 1769 |

---

### 1.7 Double Consonant Endings

| 1611 Form | 1769 Form | Theological Weight |
|-----------|-----------|-------------------|
| euill | evil | None |
| counsell | counsel | None |
| gospell | gospel | None |
| sonne | son | LOW -- "sonne of God" is strong auth marker |
| sunne | sun | None |
| sinne | sin | None |
| spirituall | spiritual | MODERATE -- theological term |
| eternall | eternal | HIGH -- Christological in eternal life verses |
| naturall | natural | None |
| originall | original | None |
| temporall | temporal | None |
| carnall | carnal | None |
| principall | principal | None |
| speciall | special | None |

**Note on "sonne":** "sonne of God" vs "son of God" is one of the most frequent 1611 spellings
and one of the most reliable authentication markers for digital transcriptions.

---

### 1.8 -OUR Endings (PRESERVED in Both Editions -- NOT a distinguishing marker)

Both 1611 and 1769 keep British -our spellings throughout:

honour, favour, labour, neighbour, saviour, colour, valour, armour

"Saviour" with -our is preserved in both editions.

---

### 1.9 Verb -eth Endings (PRESERVED in Both Editions -- NOT a distinguishing marker)

Both editions preserve archaic third-person singular -eth throughout:

saith, doeth, goeth, knoweth, giveth, taketh, speaketh, runneth, cometh, hath, doth

---

### 1.10 Archaic Pronouns (PRESERVED in Both Editions -- NOT distinguishing markers)

Both editions preserve:

thee, thou, thy, thine, ye, you, whom, whoso, whosoever, whatsoever,
whither, hither, thither, hence, thence

---

### 1.11 Verb Past Tense Variants

| 1611 Form | 1769 Form | Notes |
|-----------|-----------|-------|
| sate | sat | Past of sit |
| clave | cleaved | 2 Kgs 18:6 vs 2 Kgs 3:3 -- inconsistent within 1611 |
| spake | spake | PRESERVED in both -- not a marker |
| holpen | helped | Some instances normalized; some preserved |
| sware | swore | |
| strake | struck | |
| bare | bore | Context-dependent |
| waxed | waxed | PRESERVED in both |

---

### 1.12 Archaic Word Forms

| 1611 Form | 1769 Form | Status | Notes |
|-----------|-----------|--------|-------|
| astonied | astonished | INCONSISTENT | Ezra 9:3 = astonied; Isa 52:14 = astonished -- both in 1769 |
| baken | baked | INCONSISTENT | Lev 2:4 = baken; Num 11:8 = baked -- both in 1769 |
| fetcht | fetched | Normalized | Gen 18:7 |
| flotes | floats | Normalized | 2 Chron 2:16 |
| fole | foal | Normalized | Gen 49:11 |
| forsomuch | forasmuch | Normalized | Luke 19:9 |
| hungred | hungered | Normalized | Luke 6:3 |
| injoined | enjoined | Normalized | Heb 9:20 |
| throughly | throughly | PRESERVED IN BOTH | NOT "thoroughly" -- modern change is post-1769 error |
| strait | strait | PRESERVED IN BOTH | NOT "straight" -- "strait gate" = narrow; modern substitution is error |

**Critical note on "throughly" and "strait":**
These are the two most common cases where MODERN printings (post-1769) introduce errors that
neither 1611 nor genuine 1769 contain. If a text reads "thoroughly furnished" (2 Tim 3:17) or
"straight gate" (Matt 7:13) it is neither 1611 nor genuine 1769.

---

### 1.13 Capitalization Differences

| Context | 1611 | 1769 | Notes |
|---------|------|------|-------|
| Spirit (Mark 1:12) | Spirit | spirit | Oxford/Blayney lowercased; Cambridge 1769 kept capital |
| Spirit (1 John 5:8) | Spirit | Spirit | Oxford kept capital; Cambridge lowercased -- INVERTED from Mark 1:12 |
| Name (divine) | Name | name | Low impact |
| Angels (Ps 8:5) | Angels | angels | Cap only -- both correctly follow LXX |
| Word (John 1:1) | Word | Word | PRESERVED in both |
| LORD (Tetragrammaton) | LORD | LORD | PRESERVED in both |

**Oxford vs Cambridge capitalization divergence:** Mark 1:12 and 1 John 5:8 are inverted between
the two 1769 editions. Most modern KJVs follow Cambridge text at these points.

---

## PART 2: COMPLETE CHANGE RECORD -- ALL 137 ENTRIES

**Column key:**
- Cat = Category
- Sub = Subcategory
- Tier = Authentication tier (1=definitive, 2=supporting, 3=minor, NA=not a marker)
- LXX = LXX alignment impact
- Theol = Theological weight
- Sub? = Substantive word change (Y) vs spelling/orthographic (N)

| ID | Cat | Sub | 1611 | 1769 | Change Type | Tier | LXX | Theol | Sub? | Notes | Ref |
|----|-----|-----|------|------|-------------|------|-----|-------|------|-------|-----|
| 1 | Typography | LongS | (long-s) | s | Typographic | 1 | NONE | NONE | N | Looks like f; Unicode U+017F; confirms pre-1769 | Throughout |
| 2 | Letter | I_J | I (consonant) | J | Letter norm | 1 | NONE | NONE | N | Iesus->Jesus; I and J not distinguished in 1611 | Throughout |
| 3 | Letter | I_J | Iesus | Jesus | Letter norm | 1 | NONE | NONE | N | Most reliable single-word 1611 auth marker | NT throughout |
| 4 | Letter | I_J | Iohn | John | Letter norm | 1 | NONE | NONE | N | | Gospel of John |
| 5 | Letter | I_J | Ierusalem | Jerusalem | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 6 | Letter | I_J | Iudah | Judah | Letter norm | 1 | NONE | NONE | N | | Throughout OT |
| 7 | Letter | I_J | Iacob | Jacob | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 8 | Letter | I_J | Ioseph | Joseph | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 9 | Letter | I_J | Ionah | Jonah | Letter norm | 1 | NONE | NONE | N | | Book of Jonah |
| 10 | Letter | I_J | Iordan | Jordan | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 11 | Letter | I_J | ioy | joy | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 12 | Letter | I_J | iustice | justice | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 13 | Letter | U_V | vpon | upon | Letter norm | 1 | NONE | NONE | N | One of the most reliable 1611 markers | Throughout |
| 14 | Letter | U_V | vnto | unto | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 15 | Letter | U_V | vp | up | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 16 | Letter | U_V | vnder | under | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 17 | Letter | U_V | euil | evil | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 18 | Letter | U_V | euill | evil | Letter norm | 1 | NONE | NONE | N | Double-L variant also present | Throughout |
| 19 | Letter | U_V | haue | have | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 20 | Letter | U_V | giue | give | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 21 | Letter | U_V | loue | love | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 22 | Letter | U_V | aboue | above | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 23 | Letter | U_V | liue | live | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 24 | Letter | U_V | seruant | servant | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 25 | Letter | U_V | saue | save | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 26 | Letter | U_V | heauen | heaven | Letter norm | 1 | NONE | NONE | N | EA digraph + U/V combined | Throughout |
| 27 | Letter | U_V | reueale | reveal | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 28 | Letter | U_V | euer | ever | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 29 | Letter | U_V | neuer | never | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 30 | Letter | U_V | ouer | over | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 31 | Letter | U_V | riuer | river | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 32 | Letter | U_V | siluer | silver | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 33 | Letter | U_V | diuide | divide | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 34 | Letter | U_V | beloued | beloved | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 35 | Letter | U_V | gaue | gave | Letter norm | 1 | NONE | NONE | N | | Throughout |
| 36 | Vowel | IE_Y | citie | city | Suffix norm | 1 | NONE | NONE | N | Strong auth marker | Throughout |
| 37 | Vowel | IE_Y | glorie | glory | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 38 | Vowel | IE_Y | mercie | mercy | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 39 | Vowel | IE_Y | bodie | body | Suffix norm | 1 | NONE | LOW | N | Incidental to Heb 10:5 soma discussion -- spelling irrelevant to LXX issue | Heb 10:5 ctx |
| 40 | Vowel | IE_Y | holie | holy | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 41 | Vowel | IE_Y | vanitie | vanity | Suffix norm | 1 | NONE | NONE | N | | Ecclesiastes |
| 42 | Vowel | IE_Y | victorie | victory | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 43 | Vowel | IE_Y | charitie | charity | Suffix norm | 1 | NONE | NONE | N | | 1 Corinthians |
| 44 | Vowel | IE_Y | enmitie | enmity | Suffix norm | 1 | NONE | NONE | N | | Gen 3:15 |
| 45 | Vowel | IE_Y | vnitie | unity | Suffix norm | 1 | NONE | NONE | N | | Psalms/NT |
| 46 | Vowel | IE_Y | beautie | beauty | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 47 | Vowel | IE_Y | mysterie | mystery | Suffix norm | 1 | NONE | NONE | N | | NT epistles |
| 48 | Vowel | IE_Y | prophecie | prophecy | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 49 | Vowel | IE_Y | companie | company | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 50 | Vowel | IE_Y | countrie | country | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 51 | Vowel | IE_Y | armie | army | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 52 | Vowel | IE_Y | enemie | enemy | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 53 | Vowel | IE_Y | familie | family | Suffix norm | 1 | NONE | NONE | N | | Throughout |
| 54 | Consonant | Dbl_LL | spirituall | spiritual | Double-L drop | 2 | NONE | MODERATE | N | Theological term | NT epistles |
| 55 | Consonant | Dbl_LL | eternall | eternal | Double-L drop | 2 | NONE | HIGH | N | Christological significance | NT throughout |
| 56 | Consonant | Dbl_LL | naturall | natural | Double-L drop | 2 | NONE | LOW | N | | NT |
| 57 | Consonant | Dbl_LL | originall | original | Double-L drop | 2 | NONE | LOW | N | | |
| 58 | Consonant | Dbl_LL | counsell | counsel | Double-L drop | 2 | NONE | NONE | N | | Throughout |
| 59 | Consonant | Dbl_LL | gospell | gospel | Double-L drop | 2 | NONE | NONE | N | | NT |
| 60 | Consonant | Dbl_NN | sonne | son | Double-N drop | 1 | NONE | LOW | N | "sonne of God" = strong auth marker | Throughout |
| 61 | Consonant | Dbl_NN | sunne | sun | Double-N drop | 1 | NONE | NONE | N | | Throughout |
| 62 | Consonant | Dbl_NN | sinne | sin | Double-N drop | 1 | NONE | NONE | N | | Throughout |
| 63 | Vowel | EA_Dig | heauen | heaven | Digraph norm | 1 | NONE | NONE | N | Most reliable EA digraph marker | Throughout |
| 64 | Vowel | EA_Dig | eate | eat | Digraph norm | 1 | NONE | NONE | N | | Throughout |
| 65 | Vowel | EA_Dig | meate | meat | Digraph norm | 1 | NONE | LOW | N | "meat" = food in both eds; spelling only | Throughout |
| 66 | Vowel | EA_Dig | speake | speak | Digraph norm | 1 | NONE | NONE | N | | Throughout |
| 67 | Vowel | EA_Dig | breake | break | Digraph norm | 1 | NONE | NONE | N | | Throughout |
| 68 | Vowel | EA_Dig | steale | steal | Digraph norm | 1 | NONE | NONE | N | | Throughout |
| 69 | Vowel | EA_Dig | beate | beat | Digraph norm | 1 | NONE | NONE | N | | Throughout |
| 70 | Vowel | EA_Dig | heale | heal | Digraph norm | 1 | NONE | NONE | N | | Throughout |
| 71 | Vowel | EA_Dig | deale | deal | Digraph norm | 1 | NONE | NONE | N | | Throughout |
| 72 | Vowel | EA_Dig | leaue | leave | Digraph norm | 1 | NONE | NONE | N | | Throughout |
| 73 | Vowel | EA_Dig | feare | fear | Digraph norm | 1 | NONE | NONE | N | | Throughout |
| 74 | SilentE | Final_E | blinde | blind | Final-e drop | 1 | NONE | NONE | N | | Throughout |
| 75 | SilentE | Final_E | minde | mind | Final-e drop | 1 | NONE | NONE | N | | Throughout |
| 76 | SilentE | Final_E | kinde | kind | Final-e drop | 1 | NONE | NONE | N | | Throughout |
| 77 | SilentE | Final_E | finde | find | Final-e drop | 1 | NONE | NONE | N | | Throughout |
| 78 | SilentE | Final_E | binde | bind | Final-e drop | 1 | NONE | NONE | N | | Throughout |
| 79 | SilentE | Final_E | behinde | behind | Final-e drop | 1 | NONE | NONE | N | | Throughout |
| 80 | SilentE | Final_E | knowne | known | Final-e drop | 1 | NONE | NONE | N | | Throughout |
| 81 | SilentE | Final_E | younge | young | Final-e drop | 2 | NONE | NONE | N | | Throughout |
| 82 | SilentE | Final_E | longe | long | Final-e drop | 2 | NONE | NONE | N | | Throughout |
| 83 | SilentE | Final_E | stronge | strong | Final-e drop | 2 | NONE | NONE | N | | Throughout |
| 84 | SilentE | Final_E | wronge | wrong | Final-e drop | 2 | NONE | NONE | N | | Throughout |
| 85 | SilentE | Final_E | amonge | among | Final-e drop | 2 | NONE | NONE | N | | Throughout |
| 86 | Verb | Past | sate | sat | Verb form | 2 | NONE | NONE | N | Past of sit | Throughout |
| 87 | Verb | Past | clave | cleaved | Verb form | 2 | NONE | NONE | N | Inconsistent even within 1611 | 2 Kings |
| 88 | Verb | PRESERVED | spake | spake | NO CHANGE | NA | NONE | NONE | N | Both editions keep spake -- not a marker | Throughout |
| 89 | Verb | Past | holpen | helped | Verb form | 2 | NONE | NONE | N | Some instances normalized; some preserved | Psalms |
| 90 | Archaic | Inconsistent | astonied | astonished | Inconsistent | 2 | NONE | NONE | N | Ezra 9:3=astonied; Isa 52:14=astonished; both in 1769 | Ezra 9:3 / Isa 52:14 |
| 91 | Archaic | Normalized | fetcht | fetched | Word form | 2 | NONE | NONE | N | | Gen 18:7 |
| 92 | Archaic | Normalized | flotes | floats | Word form | 2 | NONE | NONE | N | | 2 Chron 2:16 |
| 93 | Archaic | Normalized | fole | foal | Word form | 2 | NONE | NONE | N | | Gen 49:11 |
| 94 | Archaic | Normalized | forsomuch | forasmuch | Word form | 2 | NONE | NONE | N | | Luke 19:9 |
| 95 | Archaic | Normalized | hungred | hungered | Word form | 2 | NONE | NONE | N | | Luke 6:3 |
| 96 | Archaic | Normalized | injoined | enjoined | Word form | 2 | NONE | NONE | N | | Heb 9:20 |
| 97 | Archaic | PRESERVED | throughly | throughly | NO CHANGE | NA | NONE | MODERATE | N | NOT "thoroughly"; modern change is post-1769 error | 2 Tim 3:17 |
| 98 | Archaic | PRESERVED | strait | strait | NO CHANGE | NA | NONE | HIGH | N | NOT "straight"; "strait gate" = narrow; modern sub is error | Matt 7:13 |
| 99 | Cap | Spirit | Spirit | spirit | Cap shift | 3 | NONE | MODERATE | N | Mark 1:12: Oxford=spirit / Cambridge=Spirit; inverted at 1 Jn 5:8 | Mark 1:12 |
| 100 | Cap | Divine | Name | name | Cap shift | 3 | NONE | LOW | N | | Throughout |
| 101 | Cap | Angels | Angels | angels | Cap shift | 3 | LXX-CORRECT | LOW | N | Both eds correctly follow LXX; cap only | Ps 8:5 |
| 102 | Substantive | PrintErr | seek good | seek God | Error corrected | NA | NONE | NONE | Y | Printer error; corrected 1617 | Ps 69:32 |
| 103 | Substantive | PrintErr | the place | his place | Error corrected | NA | NONE | NONE | Y | Printer error; corrected 1638 | Eccl 1:5 |
| 104 | Substantive | PrintErr | thy right doeth | thy right hand doeth | Omitted word | NA | NONE | NONE | Y | Printer error; corrected 1613 | Matt 6:3 |
| 105 | Substantive | Blayney | one lamb | one ram | Animal species | NA | NONE | MODERATE | Y | Heb ayil = ram; 1611 was error; 1769 correct | Num 6:14 |
| 106 | Substantive | Blayney | poured it upon | poured it not upon | Meaning reversal | NA | NONE | HIGH | Y | 1611 inverted the negative; 1769 restores sense; context = blood guilt | Ezek 24:7 |
| 107 | Substantive | Blayney | requite good | requite me good | Added pronoun | NA | NONE | LOW | Y | | 1 Sam 16:12 |
| 108 | Substantive | Blayney | for the king | for so the king | Added adverb | NA | NONE | LOW | Y | | Esther 1:8 |
| 109 | Substantive | Blayney | given the into hand | given thy into hand | Possessive fix | NA | NONE | LOW | Y | | Isa 47:6 |
| 110 | Substantive | Blayney | God (Isa 49:13) | Lord (Isa 49:13) | Divine name | NA | LXX-IMPROVED | HIGH | Y | LXX = kurios (Lord); 1769 MORE LXX-aligned than 1611; only case Blayney improved LXX | Isa 49:13 |
| 111 | Substantive | Blayney | made a covenant | made thee a covenant | Added pronoun | NA | NONE | LOW | Y | | Isa 57:8 |
| 112 | Substantive | Blayney | the people | the children of thy people | Expanded phrase | NA | NONE | LOW | Y | | Ezek 3:11 |
| 113 | Substantive | Blayney | the crowned | thy crowned | Possessive fix | NA | NONE | LOW | Y | | Nahum 3:17 |
| 114 | Substantive | Blayney | to shearer | to his shearer | Added possessive | NA | NONE | LOW | Y | | Acts 8:32 |
| 115 | Substantive | Blayney | which was a Jew | which was a Jewess | Gender fix | NA | NONE | LOW | Y | Timothy's mother | Acts 16:1 |
| 116 | Substantive | Blayney | spiritual sacrifice | spiritual sacrifices | Singular->Plural | NA | NONE | MODERATE | Y | Greek = plural; 1769 correct; ongoing priestly offering | 1 Pet 2:5 |
| 117 | Substantive | Blayney | now and ever | both now and ever | Added conjunction | NA | NONE | LOW | Y | | Jude 25 |
| 118 | Substantive | Oxf_v_Camb | whom ye had set free | whom he had set free | Pronoun shift | NA | NONE | MODERATE | Y | Cambridge=ye (people); Oxford=he (Zedekiah); changes accountability | Jer 34:16 |
| 119 | Substantive | BlayneyErr | flieth (correct) | fleeth (error kept) | Retained error | NA | NONE | LOW | Y | Blayney kept Parris 1762 error; Cambridge correct | Nahum 3:16 |
| 120 | Substantive | BlayneyErr | Beersheba or Sheba | Beersheba and Sheba | Retained error | NA | NONE | LOW | Y | Blayney kept Parris 1762 error; Cambridge correct with "or" | Josh 19:2 |
| 121 | PrintRun | He_She | he went into city | she went into city | Print run var | NA | NONE | NONE | N | Ruth 3:15; He Bible=1st run; She Bible=2nd; both genuine 1611 | Ruth 3:15 |
| 122 | PRESERVED | BothOK | Angels (Ps 8:5) | angels (Ps 8:5) | Cap only -- LOCK | NA | LXX-CORRECT | HIGH | N | Both correctly follow LXX vs MT; preserve this anchor | Ps 8:5 |
| 123 | PRESERVED | BothOK | virgin (Isa 7:14) | virgin (Isa 7:14) | NO CHANGE -- LOCK | NA | LXX-CORRECT | HIGH | N | Both correctly follow LXX parthenos vs MT almah; preserve | Isa 7:14 |
| 124 | PRESERVED | BothOK | corruption (Ps 16:10) | corruption (Ps 16:10) | NO CHANGE -- LOCK | NA | LXX-CORRECT | HIGH | N | Both correctly follow LXX diaphthora; preserve | Ps 16:10 |
| 125 | PRESERVED | BothOK | all flesh (Joel 2:28) | all flesh (Joel 2:28) | NO CHANGE -- LOCK | NA | LXX-CORRECT | HIGH | N | Both follow LXX pasan sarka; preserve | Joel 2:28 |
| 126 | PRESERVED | BothOK | pierced (Ps 22:16) | pierced (Ps 22:16) | NO CHANGE -- LOCK | NA | LXX-CORRECT | HIGH | N | Both follow LXX oryxan vs disputed MT; preserve | Ps 22:16 |
| 127 | NEEDS_FIX | BothMT | ears (Ps 40:6) | ears (Ps 40:6) | BOTH WRONG | NA | LXX-NEEDED | CRITICAL | N | Both follow MT; LXX = soma (body); Heb 10:5 quotes LXX | Ps 40:6 |
| 128 | NEEDS_FIX | BothMT | Edom (Amos 9:12) | Edom (Amos 9:12) | BOTH WRONG | NA | LXX-NEEDED | CRITICAL | N | Both follow MT; LXX = anthropon (mankind); Acts 15:17 quotes LXX | Amos 9:12 |
| 129 | NEEDS_FIX | BothMT | bed (Gen 47:31) | bed (Gen 47:31) | BOTH WRONG | NA | LXX-NEEDED | CRITICAL | N | Both follow MT mitte (bed); LXX = rhabdou (staff); Heb 11:21 quotes LXX | Gen 47:31 |
| 130 | NEEDS_FIX | BothMT | in Egypt only (Exod 12:40) | in Egypt only | BOTH WRONG | NA | LXX-NEEDED | CRITICAL | N | Both follow MT; LXX adds "and in Canaan"; affects Gal 3:17 chronology | Exod 12:40 |
| 131 | NEEDS_FIX | BothMT | short text (Deut 32:43) | short text | BOTH WRONG | NA | LXX-NEEDED | CRITICAL | N | Both have MT short text; LXX adds angel worship clause quoted in Heb 1:6 | Deut 32:43 |
| 132 | NEEDS_FIX | BothMT | his faith (Hab 2:4) | his faith (Hab 2:4) | BOTH SAME | NA | LXX-VARIANT | MODERATE | N | Both follow MT "his faith"; LXX = "My faith" (God's); Rom 1:17 | Hab 2:4 |
| 133 | Cap | Spirit_NT | Spirit/spirit | spirit/Spirit | Inverted cap | 3 | NONE | MODERATE | N | Oxford/Cambridge inversion at Mk 1:12 and 1 Jn 5:8 | Mk 1:12 / 1 Jn 5:8 |
| 134 | PRESERVED | BothEds | spake | spake | NO CHANGE | NA | NONE | NONE | N | Archaic verb forms preserved throughout both editions | Throughout |
| 135 | PRESERVED | BothEds | thou/thee/thy | thou/thee/thy | NO CHANGE | NA | NONE | NONE | N | Archaic pronouns preserved throughout | Throughout |
| 136 | PRESERVED | BothEds | LORD | LORD | NO CHANGE | NA | NONE | NONE | N | Tetragrammaton rendering preserved in both | Throughout |
| 137 | PRESERVED | BothEds | Word (John 1:1) | Word (John 1:1) | NO CHANGE | NA | LXX-CORRECT | HIGH | N | Logos rendering preserved in both | John 1:1 |

---

## PART 3: AUTHENTICATION DECISION TREE

### How to Authenticate a Claimed "1611 First Print" Text

**Tier 1 -- Definitive 1611 Markers (any one = pre-1769):**

- [ ] Contains "Iesus" (not "Jesus")
- [ ] Contains "vpon" (not "upon")
- [ ] Contains "euil" or "euill" (not "evil")
- [ ] Contains "sonne of God" (not "son of God")
- [ ] Contains "glorie" (not "glory")
- [ ] Contains "citie" (not "city")
- [ ] Contains "haue" (not "have")
- [ ] Contains "heauen" (not "heaven")
- [ ] Contains "gaue" (not "gave")
- [ ] Contains "giue" (not "give")

**Tier 2 -- Supporting Markers:**

- [ ] Long s (Unicode U+017F) present in print
- [ ] Gothic/Blackletter typeface
- [ ] He/She Bible variant present (Ruth 3:15 test -- see below)
- [ ] Apocrypha included
- [ ] "The Translators to the Reader" preface present
- [ ] "spirituall", "eternall", "carnall" with double-L

**Tier 3 -- Minor Markers:**

- [ ] "Spirit" capitalized at Mark 1:12 (Cambridge 1769) vs lowercase (Oxford/Blayney)
- [ ] Capitalized "Angels" at Ps 8:5

**Disqualifying -- Proves NOT genuine 1611 or 1769:**

- [ ] "Jesus" with J = post-1611 or 1769+
- [ ] "upon" = 1769+
- [ ] "city" (not "citie") = 1769+
- [ ] "son of God" (not "sonne") = 1769+
- [ ] Modern typeface = 1769+
- [ ] "thoroughly" (not "throughly") = post-1769 error in ANY edition
- [ ] "straight gate" (not "strait gate") = post-1769 error in ANY edition

### The Ruth 3:15 Test (Identifies Which 1611 Print Run)

- "he went into the city" = "Great He Bible" = FIRST 1611 print run (Barker)
- "she went into the city" = "She Bible" = SECOND 1611 print run

Both are genuine 1611. This test identifies WHICH run, not whether it IS 1611.

---

## PART 4: COMPUTATIONAL REFERENCE

### 4.1 Authentication Detection (Python)

```python
import re

TIER1_1611_MARKERS = [
    (r'\bIesus\b',  'I/J: Iesus'),
    (r'\bvpon\b',   'U/V: vpon'),
    (r'\beuil+\b',  'U/V: euil/euill'),
    (r'\bsonne\b',  'Double-N: sonne'),
    (r'\bglorie\b', 'IE/Y: glorie'),
    (r'\bcitie\b',  'IE/Y: citie'),
    (r'\bhaue\b',   'U/V: haue'),
    (r'\bheauen\b', 'EA+U/V: heauen'),
    (r'\bgaue\b',   'U/V: gaue'),
    (r'\bgiue\b',   'U/V: giue'),
]

def detect_1611(text):
    hits = []
    for pattern, label in TIER1_1611_MARKERS:
        if re.search(pattern, text):
            hits.append(label)
    return {
        'hits': hits,
        'hit_count': len(hits),
        'confidence': len(hits) / len(TIER1_1611_MARKERS),
        'likely_1611': len(hits) >= 2
    }

def detect_post_1769_errors(text):
    """Flags modernizations that should not appear in 1611 OR genuine 1769"""
    errors = []
    if re.search(r'\bthoroughly\b', text):
        errors.append('thoroughly -- should be throughly in both 1611 and 1769')
    if re.search(r'\bstraight gate\b', text):
        errors.append('straight gate -- should be strait gate in both editions')
    return errors
```

### 4.2 Normalization Pipeline (1611 to Modern)

```python
import re

def normalize_1611_to_modern(text):

    # Step 1: Long S
    text = text.replace('\u017f', 's')

    # Step 2: I/J normalization -- by word list (general regex too broad)
    IJ_WORDS = {
        'Iesus': 'Jesus', 'Iohn': 'John', 'Ierusalem': 'Jerusalem',
        'Iudah': 'Judah', 'Iacob': 'Jacob', 'Ioseph': 'Joseph',
        'Ionah': 'Jonah', 'Iordan': 'Jordan', 'Iudge': 'Judge',
        'Iudges': 'Judges', 'Ieremiah': 'Jeremiah', 'ioy': 'joy',
        'iustice': 'justice',
        # NOTE: Israel, Isaac, Isaiah retain I -- do not include here
    }
    for old, new in IJ_WORDS.items():
        text = re.sub(r'\b' + old + r'\b', new, text)

    # Step 3: U/V normalization
    UV_WORDS = {
        'vpon': 'upon', 'vnto': 'unto', 'vp': 'up', 'vnder': 'under',
        'euil': 'evil', 'euill': 'evil', 'haue': 'have', 'giue': 'give',
        'loue': 'love', 'aboue': 'above', 'liue': 'live',
        'seruant': 'servant', 'saue': 'save', 'heauen': 'heaven',
        'euer': 'ever', 'neuer': 'never', 'ouer': 'over',
        'riuer': 'river', 'siluer': 'silver', 'diuide': 'divide',
        'beloued': 'beloved', 'gaue': 'gave', 'reueale': 'reveal',
    }
    for old, new in UV_WORDS.items():
        text = re.sub(r'\b' + old + r'\b', new, text, flags=re.IGNORECASE)

    # Step 4: -ie to -y suffix
    IE_Y_WORDS = {
        'citie': 'city', 'glorie': 'glory', 'mercie': 'mercy',
        'bodie': 'body', 'holie': 'holy', 'vanitie': 'vanity',
        'victorie': 'victory', 'charitie': 'charity', 'enmitie': 'enmity',
        'mysterie': 'mystery', 'prophecie': 'prophecy',
        'companie': 'company', 'countrie': 'country', 'armie': 'army',
        'enemie': 'enemy', 'familie': 'family',
    }
    for old, new in IE_Y_WORDS.items():
        text = re.sub(r'\b' + old + r'\b', new, text, flags=re.IGNORECASE)

    # Step 5: DO NOT normalize these -- flag or preserve
    # throughly, strait, spake, hath, doeth, saith
    # These should never be silently changed

    return text
```

### 4.3 Covenant Anchor Integration Flags

```python
# Verses where BOTH 1611 and 1769 need LXX correction
LXX_CORRECTION_NEEDED = {
    'Ps 40:6':    {'kjv': 'ears',       'lxx': 'soma (body)',    'nt': 'Heb 10:5',  'priority': 'CRITICAL'},
    'Amos 9:12':  {'kjv': 'Edom',       'lxx': 'anthropon (mankind)', 'nt': 'Acts 15:17', 'priority': 'CRITICAL'},
    'Gen 47:31':  {'kjv': 'bed',        'lxx': 'rhabdou (staff)', 'nt': 'Heb 11:21', 'priority': 'CRITICAL'},
    'Exod 12:40': {'kjv': 'Egypt only', 'lxx': 'Egypt and Canaan', 'nt': 'Gal 3:17', 'priority': 'CRITICAL'},
    'Deut 32:43': {'kjv': 'short text', 'lxx': 'adds angel worship', 'nt': 'Heb 1:6', 'priority': 'CRITICAL'},
}

# Verses correctly LXX-aligned in BOTH editions -- lock these, do not change
LXX_CORRECT_LOCK = {
    'Ps 8:5':    {'kjv': 'angels',     'lxx': 'aggeloi',   'nt': 'Heb 2:7'},
    'Isa 7:14':  {'kjv': 'virgin',     'lxx': 'parthenos', 'nt': 'Matt 1:23'},
    'Ps 16:10':  {'kjv': 'corruption', 'lxx': 'diaphthora', 'nt': 'Acts 2:27'},
    'Joel 2:28': {'kjv': 'all flesh',  'lxx': 'pasan sarka', 'nt': 'Acts 2:17'},
    'Ps 22:16':  {'kjv': 'pierced',    'lxx': 'oryxan',    'nt': 'John 20:25'},
}

# The one case where Blayney improved LXX alignment
LXX_BLAYNEY_IMPROVED = {
    'Isa 49:13': {'1611': 'God', '1769': 'Lord', 'lxx': 'kurios', 'note': '1769 more LXX-aligned'},
}
```

---

## PART 5: CAMBRIDGE VS OXFORD DIVERGENCES (Post-1769)

Both Cambridge and Oxford claim to produce the standard KJV text. They diverge at these points:

| Ref | Cambridge Text | Oxford/Blayney Text | Which is Correct | Notes |
|-----|----------------|---------------------|-----------------|-------|
| Josh 19:2 | Beersheba, or Sheba | Beersheba, and Sheba | Cambridge | Blayney retained Parris 1762 error |
| Nahum 3:16 | flieth | fleeth | Cambridge | Blayney retained Parris 1762 error |
| Mark 1:12 | Spirit (capital) | spirit (lower) | Preference | Theological capitalization |
| 1 John 5:8 | spirit (lower) | Spirit (capital) | Preference | Inverted from Mark 1:12 in both |
| Jer 34:16 | whom ye had set free | whom he had set free | Debated | Changes accountability: people vs king |

**For Covenant Anchor use:** Cambridge text is marginally superior at Josh 19:2 and Nahum 3:16.
Capitalization differences at Mark 1:12 and 1 John 5:8 are irrelevant to LXX alignment.

---

## PART 6: AUTHORITATIVE SOURCES

| Author | Work | Date | Notes |
|--------|------|------|-------|
| Scrivener, F.H.A. | The Authorized Edition of the English Bible (1611) | Cambridge, 1884 | Definitive collation; primary source for all readings and amendments |
| Norton, David | A Textual History of the King James Bible | Cambridge, 2005 | Most thorough modern treatment of all edition variants |
| Pollard, A.W. | Records of the English Bible | 1911 | Primary documents on the original translation process |
| Blayney, Benjamin | Preface to 1769 Oxford edition | 1769 | Blayney's own description of his methodology |
| Waite, Donald | KJB of 1611 Compared to KJB of 1917 Old Scofield (BFT1294) | Modern | Source for the 136 substantive changes figure |
| Haslam, David | CrossWire KJV collation | wiki.crosswire.org | 1769 spelling variant documentation |
| Pure Cambridge Text | Cambridge vs Oxford divergences | purecambridgetext.com | Documents post-Blayney variants |

---

## APPENDIX: SUMMARY STATISTICS

| Category | Count | LXX-Relevant |
|----------|-------|-------------|
| Total entries documented | 137 | -- |
| Orthographic/spelling changes (Sub?=N) | 115 | 0 |
| Substantive word changes (Sub?=Y) | 22 | 1 |
| Printer error corrections | 3 | 0 |
| Blayney word changes | 13 | 1 (Isa 49:13 improved) |
| Blayney retained errors | 2 | 0 |
| Verses LXX-correct in both eds (LOCK) | 5 | 5 |
| Verses needing LXX correction in both eds | 6 | 6 (CRITICAL) |
| Cases where Blayney DEGRADED LXX alignment | 0 | 0 |
| Cases where Blayney IMPROVED LXX alignment | 1 | 1 |

**Bottom line:** 1769 is the correct base for the Covenant Anchor Engine. Apply the ~800 LXX
corrections identically regardless of which edition you start from. The spelling differences
documented here are computationally useful for authentication and normalization but have zero
bearing on the LXX-MT translational choices the Covenant Anchor system exists to correct.

---

*Document version 2.0 | ASCII-safe | Compiled for Covenant Anchor Engine*

