

added the new locked nodes, flexible cadences, and wisdom-stack rules you suggested, while preserving your original structure and philosophy. Everything is backward-compatible, but now tighter and more opinionated where the Hebrew demands it.

```json
{
  "engine_version": "1.1.0-TRUNK",
  "philosophy": "Seed-to-Tree / Heat-Restored",
  "immutable_locks": {
    "firmament": "Hammered Sky [raqia]",
    "righteousness": "Covenant-Justice",
    "justice": "Covenant-Justice",
    "spirit": "Spirit-Breath",
    "soul": "Life-Breath [nephesh]",
    "repentance": "Turning [teshuvah]",
    "subdue": "Ordered Authority",
    "grace": "Covenant-Faithfulness",
    "mercy": "Covering-Mercy",
    "knowing": "Intimate Union before Intellect [yada]",
    "light": "Covenant Visibility (not wattage)"
  },
  "cadence_flexible": {
    "glory": ["Glory Weight", "Substance of Presence"],
    "hell": {
      "context_grave": "Sheol/Hades",
      "context_judgment": "Gehenna",
      "context_fallen_angels": "Tartarus",
      "context_void": "The Abyss"
    },
    "servant": "Slave [doulos/ebed]",
    "fear_of_the_lord": "Holy Dread",
    "love": {
      "covenantal": "Covenant-Love [agape]",
      "affectional": "Friend-Affection [philia]"
    },
    "covering": ["Protective Shadow", "Atoning Blood"],
    "majestic_plurality": "Default: plural of majesty / intensity unless context demands polytheism"
  },
  "wisdom_stack_enforcement": {
    "sequence": [
      "Knowing [intimate union]",
      "Holy Dread",
      "Wisdom",
      "Understanding",
      "Counsel",
      "Knowledge",
      "Covenant-Justice Action"
    ],
    "validation_rules": [
      "FAIL_IF_KNOWLEDGE_PRECEDES_DREAD",
      "FAIL_IF_INTELLECTUAL_KNOWING_PRECEDES_INTIMATE_UNION"
    ]
  },
  "animal_living_precedence": {
    "rule": "Process living creatures by primary verb/action before noun identity",
    "examples": {
      "seraphim": "Fiery Ones (burning action first)",
      "nahaliel": "Torrent-of-God (flowing action first)",
      "cherubim": "Guarding / Covering ones (protective action first)"
    }
  },
  "silence_gaps": {
    "rule": "Three consecutive dots (…) or ellipsis in source text = 'God spoke nothing' → treat as semantic silence / withheld revelation",
    "behavior": "Do not fill. Do not paraphrase. Preserve as data point."
  }
}
```

### Quick changelog / why each addition

- Added `"knowing": "Intimate Union before Intellect [yada]"` → forces the engine to prioritize relational/tactile knowing (sex, touch, deep acquaintance) before abstract cognition.
- Added `"light": "Covenant Visibility (not wattage)"` → kills modern physics bleed-in; light is always functional/revelatory in covenant context.
- Expanded `"covering"` to allow both shadow (protective) and blood (atoning) senses — covers both cherub wings and Passover blood.
- Added `"majestic_plurality"` rule — default assumption for "us/let us/gods" language unless polytheism is contextually forced.
- Wisdom stack now has two fail conditions: no knowledge before dread, and no intellectual knowing before intimate union.
- New `animal_living_precedence` block — makes sure the engine reads seraphim as "burners" first, not "angel class" first.
- New `silence_gaps` rule — treats ellipsis / silence as meaningful absence, not something to gloss over.
