cities = ["Poznań", "Warszawa", "Kraków", "Wrocław", "Radom"]

code = ord('K')

for x in cities:
    if code < ord(x[0]) and len(x) > 6:
        print(x)