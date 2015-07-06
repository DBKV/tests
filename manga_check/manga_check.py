#!/usr/bin/python

import urllib
import re

print "Hello\n"
pandaurl = "http://www.mangapanda.com/"
handle = urllib.urlopen(pandaurl)
html = handle.read()

toriko = re.search("<div class=\"hot\"></div>\n<br />\n\s*<.*toriko/(\d+)", html, re.MULTILINE)
if toriko:
    print "New chapter Toriko " + toriko.group(1) + "!"
else:
    print "No match found for toriko!"

one_piece = re.search("<div class=\"hot\"></div>\n<br />\n\s*<.*one-piece/(\d+)", html, re.MULTILINE)
if one_piece:
    print "New chapter One Piece " + one_piece.group(1) + "!"
else:
    print "No match found for one_piece!"

bleach = re.search("<div class=\"hot\"></div>\n<br />\n\s*<.*bleach/(\d+)", html, re.MULTILINE)
if bleach:
    print "New chapter Bleach " + bleach.group(1) + "!"
else:
    print "No match found for bleach!"
    
assassination_classroom = re.search("<div class=\"hot\"></div>\n<br />\n\s*<.*assassination-classroom/(\d+)", html, re.MULTILINE)
if assassination_classroom:
    print "New chapter Assassination Classroom " + assassination_classroom.group(1) + "!"
else:
    print "No match found for Assassination Classroom!"
