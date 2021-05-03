#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generates the Mono font files based on a proportional font
Required files:
- vendor/fonttobechanged.ttf
- vendor/referencefont.ttf
Based on:
- monospacifier: https://github.com/cpitclaudel/monospacifier/blob/master/monospacifier.py
- YosemiteAndElCapitanSystemFontPatcher: https://github.com/dtinth/YosemiteAndElCapitanSystemFontPatcher/blob/master/bin/patch
- https://github.com/dtinth/comic-mono-font
- Comic Mono: https://github.com/dtinth/comic-mono-font

"""

import os
import re
import sys


import fontforge
import psMat
import unicodedata

def height(font):
    return float(font.capHeight)

def adjust_height(source, template, scale):
    source.selection.all()
    source.transform(psMat.scale(height(template) / height(source)))
    for attr in ['ascent', 'descent',
                'hhea_ascent', 'hhea_ascent_add',
                'hhea_linegap',
                'hhea_descent', 'hhea_descent_add',
                'os2_winascent', 'os2_winascent_add',
                'os2_windescent', 'os2_windescent_add',
                'os2_typoascent', 'os2_typoascent_add',
                'os2_typodescent', 'os2_typodescent_add',
                ]:
        setattr(source, attr, getattr(template, attr))
    source.transform(psMat.scale(scale))
#change the next to lines to the font you want to convert and the reference font
# make sure those two fonts are in the vendor directory
font = fontforge.open('vendor/Lexend-Regular.ttf')
ref = fontforge.open('vendor/Cousine-Regular.ttf')
for g in font.glyphs():
    uni = g.unicode
    category = unicodedata.category(chr(uni)) if 0 <= uni <= sys.maxunicode else None
    if g.width > 0 and category not in ['Mn', 'Mc', 'Me']:
                # change target width to either make characters norrow or wide
        target_width = 750
        if g.width != target_width:
            delta = target_width - g.width
            g.left_side_bearing += delta / 2
            g.right_side_bearing += delta - g.left_side_bearing
            g.width = target_width
# change next 4 lines to desired information
font.familyname = 'Lexend Mono'
font.version = '0.1.1'
font.comment = 'https://github.com/dtinth/comic-mono-font'
font.copyright = 'https://github.com/dtinth/comic-mono-font/blob/master/LICENSE'
#change number in adjust_height to make font shorter or taller
adjust_height(font, ref, 0.875)
font.sfnt_names = [] # Get rid of 'Prefered Name' etc.
#change to desired font name
font.fontname = 'LexendMono'
#change to desired full name
font.fullname = 'Lexend Mono'
#change to desired file name
font.generate('LexandMono.ttf')

font.selection.all()
#Bold section
#change to desired font name
font.fontname = 'LexendMono-Bold'
#change to desired full name
font.fullname = 'Lexend Mono Bold'
font.weight = 'Bold'
font.changeWeight(32, "LCG", 0, 0, "squish")
#change to desired file name
font.generate('LexendMono-Bold.ttf')
