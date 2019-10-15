#http://www.pythonchallenge.com/pc/def/ocr.html

def sort_second(val):
    return val[1]

#load data
file = open('data.txt')
text = file.read()

#load data to list
arr = []
for char in text:
    arr.append(ord(char))

#get unique
unique = []
for x in arr:
    if x not in unique:
        unique.append(x)

#count
count = []
for x in unique:
    count.append([chr(x), arr.count(x)])

#sort by chars amount
count.sort(key=sort_second)

word = ''
#print only uniq char = 0
for x in range(len(count)):
    if count[x][1] == 1:
        word += count[x][0]

print(word)