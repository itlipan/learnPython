# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
from sys import argv

script,filename=argv
print "The program will open %r" % filename

text= open(filename)

print "Here's your file %r" % filename
print text.read()

print "Type the filename again:"
file_again = raw_input("> ")

text_again = open(file_again)

print text_again.read()
