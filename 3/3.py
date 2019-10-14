file = open('data.txt')
text = file.read()

#print(text)

text = "Damiana"

print(text)

arr = []
print(type(arr))
for char in text:
    arr.append(ord(char))

arr.sort()

print(arr)

count = []
c = 0
for i in range(len(arr)):
    if i != len(arr) - 1:
        if arr[i] == arr[i+1]:
            print(count[i-1])
            count.append([arr[i], i+1])
        else:
            count.append([arr[i], 1])
    else:
        count.append([arr[i], 1])


print(count)


# arr.sort()
# print(arr)
# print(arr.count(97))
# print(chr(97))


