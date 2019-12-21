import re


def validate_number(number):
    regex = "^\\d{9}$|^\\d{3}\\s\\d{2}\\s\\d{2}\\s\\d{2}$|^(\\+\\d{2}\\s)?\\d{3}-\\d{3}-\\d{3}$"
    x = re.search(regex, number)
    if x is not None:
        r = 'Match'
    else:
        r = 'No match'
    return r + ': ' + number


print(validate_number('+48 0142-345-678'))
print(validate_number('012-345-67'))
print(validate_number('0123456781'))
print(validate_number('012 34 564 78'))
print(validate_number('+48 012-345-678'))
print(validate_number('012-345-678'))
print(validate_number('012345678'))
print(validate_number('012 34 56 78'))
