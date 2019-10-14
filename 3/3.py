def sort_second(val):
    return val[1]

#load data
file = open('data.txt')
text = file.read()

print(text)

#load data to list
arr = []
for char in text:
    arr.append(ord(char))

#get unique
arr.sort()
unique = []
for x in arr:
    if x not in unique:
        unique.append(x)

#count
count = []
for x in unique:
    count.append((chr(x), arr.count(x)))

#sort by chars amount
count.sort(key=sort_second)
print(count)







# arr.sort()
# print(arr)
# print(arr.count(97))
# print(chr(97))


