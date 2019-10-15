#http://www.pythonchallenge.com/pc/def/equality.html

import string

#load data from file
file = open("data.txt")
data = file.read()

#generate ascci lowercase code
alphabet = string.ascii_lowercase

lowercase_ascii = []
for char in alphabet:
    lowercase_ascii.append(ord(char))

print(lowercase_ascii)

#find lowercase later
#refex ([A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z])
lowercase = ''



print(lowercase)
