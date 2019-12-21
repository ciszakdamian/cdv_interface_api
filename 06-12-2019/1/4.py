import re

text = "Lorem ipsum  01/06/2019 tellus sed 03.04.2017 ullamcorper.\nProin 02-05-2018 interdum 04/03/16 mauris.\nMaecenas eget 05-02-15 risus tincidunt,06.01.14 tristique.\n"

regex = "([0-3][0-9](\\/|-|\\.)[0-1][0-9](\\/|-|\\.)(\\d{4}|\\d{2}))"
x = re.finditer(regex, text)

print(text)
for z in x:
    print('Match: ' + z.group())
