#! python3
# mcb.pyw - Saves abd loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclib, sys

mcbShelf = shelve.open('mcb')

# Save cliboard content
if len(sys.argv) == 3 and sys.argv[1].lower() = 'save':
    mcbShelf[sys.argv[2]] = pyperclib.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
    pyperclib.copy(str(list(mcbShelf.keys())))
elif sys.argv[1] in mcbShelf:
    pyperclib.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()