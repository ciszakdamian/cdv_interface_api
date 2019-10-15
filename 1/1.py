#http://www.pythonchallenge.com/pc/def/274877906944.html

import string
def translate(text):
    decode = ""
    for char in text:
        code = ord(char)

        if 97 > code <= 120:
            number = code
        else:
            if code == 121 or code == 122:
                # print(code)
                number = code - 26 + 2
                # print("N"+str(number))
            else:
                number = code + 2

        decode += chr(number)
    return decode

print(translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))

print(translate("map"))