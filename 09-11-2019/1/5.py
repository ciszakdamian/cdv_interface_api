file = open("file.txt", "w")

text = ''
while True:
    line = input("Podaj linie tekstu: ")
    if not line.strip():
        break
    text += str(line+'\n')

file.write(text)
file.close()
print('Plik file.txt został utworzony.')
