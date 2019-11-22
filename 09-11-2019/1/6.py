def read_file():
    f = open("people.txt", "r")
    i = 0
    for row in f:
        i += 1
        print(str(i) + '. ' + row.rstrip())
    f.close()


file = open("people.txt", "w")

line = ''
while True:

    name = input("Podaj imie: ")
    if not name.strip():
        file.close()
        read_file()
        break

    surname = input("Podaj nazwisko: ")
    if not surname.strip():
        file.close()
        read_file()
        break

    age = input("Podaj wiek: ")
    if not age.strip():
        file.close()
        read_file()
        break

    line = 'Imie: ' + name + ', Nazwisko: ' + surname + ', Wiek: ' + age + '\n'
    file.write(line)
