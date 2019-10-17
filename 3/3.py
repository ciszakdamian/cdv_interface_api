#http://www.pythonchallenge.com/pc/def/equality.html

import re

#load data from file
file = open("data.txt")
data = file.read()

#search match regex
regex = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
data = regex.findall(data)

#extract lowercase
regex = re.compile('([a-z])')
t = []
for x in data:
    t += regex.findall(x)

text = ''.join(t)

print(text)
