import re
import requests

url = input('Insert page url:')

content = requests.get(url)

regex = "\\w+[\\w\\-\\.]*\\@\\w+((-\\w+)|(\\w*))\\.[a-z]{2,3}"

x = re.finditer(regex, content.text)

emails = []
for z in x:
    emails.append(z.group())

emails = list(dict.fromkeys(emails))

for mail in emails:
    print(mail)



