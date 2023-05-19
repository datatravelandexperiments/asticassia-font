# Run with `fontforge -script generate.py` from src/

import datetime

import fontforge
import psMat

font = fontforge.open('AsticassiaWide.sfd')

print(f'{font.os2_weight=}')
print(f'{font.os2_width=}')

# Update the version.
today = datetime.date.today()
font.version = f'{today.year - 2000:03}.{today.strftime("%j")}'
font.save('AsticassiaWide.sfd')

# Generate AsticassiaWide.
font.generate('../ttf/AsticassiaWide.ttf')
font.generate('../woff/AsticassiaWide.woff2')

# Create condensed version, AsticassiaNarrow.
font.fontname = 'AsticassiaNarrow'
font.fullname = 'Asticassia Narrow'
font.os2_weight = 4
condense = psMat.scale(2/3., 1.)
font.selection.all()
font.transform(condense, ('round', 'simplePos'))

# Generate AsticassiaNarrow.
font.generate('../ttf/AsticassiaNarrow.ttf')
font.generate('../woff/AsticassiaNarrow.woff2')
