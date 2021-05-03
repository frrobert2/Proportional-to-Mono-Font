# This project is a fork of dtinth/comic-mono-font

That project was to create a font. This project is designed to use the generate.py script and use it to take a proportional spaced font and make it a mono spaced font.

This may be a very silly idea.  I have got the script to work to generate a mono spaced font from a proportional font.  The key is tweaking the height and width so the fonts look nice.

## Dependencies

Python 2

The python bindings for font forge

This link may help you install the bindings

[https://stackoverflow.com/questions/36508944/install-fontcustom-fontforge-in-ubuntu](https://stackoverflow.com/questions/36508944/install-fontcustom-fontforge-in-ubuntu)

## How to use the script

Install the Dependencies
Put the proportional font you are going to convert in the vendor directory
Put the reference font you are going to use in the vendor directory
Edit the script.  See bellow
Make the script executable 
Run ./generate.py 
Your normal font and bold font will be generated and should be found in the same directory as generate.py
The fonts can now be installed.  
Depending on the width and height you set will affect what the font actually looks like.  It could look nice or it could look awful.

## You need to edit the script.  Here is the list of things you need to change:

### Change the following two lines to the script to the font you are going to convert and the reference font
font = fontforge.open('vendor/comic-shanns.otf')
ref = fontforge.open('vendor/Cousine-Regular.ttf')

### Change the integer value the larger the number the wider the font
target_width = 510

#### change number in adjust_height to make font shorter or taller
adjust_height(font, ref, 0.875)

### change to desired font name
font.fontname = 'ComicMono'
### change to desired full name
font.fullname = 'Comic Mono'
#change to desired file name
font.generate('ComicMono.ttf')

### Bold section
### change to desired font name
font.fontname = 'ComicMono-Bold'

### change to desired full name
font.fullname = 'Comic Mono Bold'

### change to desired file name
font.generate('ComicMono-Bold.ttf')

## Notes:
What is the reference font for?
Taken from Comic Mono font README.md
The glyph metrics have been adjusted to make it display better alongside system font, based on Cousine’s metrics.
You could use a different font as the reference as see how it changes the font.

## License
It is licensed under the [MIT License](LICENSE).
