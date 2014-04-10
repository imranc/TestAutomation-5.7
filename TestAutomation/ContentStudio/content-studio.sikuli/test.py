from sikuli.Sikuli import *
import os
from SikuliCS import *
from time import gmtime, strftime
import datetime
from org.sikuli.script.natives import Vision


addImagePath("content-studio.sikuli\gfx")

f = Finder("login_content_studio.png")

img = "login_content_studio_copy.png"

f.find(img) # find all matches

while f.hasNext(): # loop as long there is a first and more matches
        print "found: ", f.next() # access the next match in the row

print f.hasNext() # is False, because f is empty now
f.destroy()
