import re


def validate_name(name):
    regex = "^\\s*[a-zA-Z]*\\s{1}[a-zA-Z]*$"
    x = re.search(regex, name)
    if x is not None:
        r = 'Match'
    else:
        r = 'No match'
    return r+': '+name


print(validate_name('Da4234mian Cisz424ak'))
print(validate_name('Damian $Ciszak'))
print(validate_name('Damian  Ciszak'))
print(validate_name('Da mian Ciszak'))
print(validate_name('Damian Ciszak?'))
print(validate_name('Damian Ciszak'))
print(validate_name('damian ciszak'))

# print('Imie: '+name+'\nNazwisko: '+surname)
