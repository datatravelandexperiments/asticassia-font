## Version 023.138

Initial release.

## Version 023.139

Packaging changes:

- Generate a ‘Narrow’ version that is close to the ‘duel’ style.
- Generate WOFF as well as TTF.

Glyph changes:

- Fix degree symbol ° (U+00B0) to match e6 20:50. It doesn't match the style,
  so I suspect the official font doesn't have it, but it is as it is.
  Modified ′ ″ ‴ to match.
- Add Œ (U+0152) (already had œ but forgot to do the capital), Ĳ (U+0132),
  and ĳ (U+0133).
- Added a few more accents and autogenerated more accented characters.
- Fix upside-down tilde.
