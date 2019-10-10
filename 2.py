text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

decode = ""
for char in text:
    code = ord(char)

    if code == 32:
        number = code
    else:
        number = code + 2
        # print(code)
    decode += chr(number)

print(decode)
