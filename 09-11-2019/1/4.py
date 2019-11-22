import math


def pole_kola(r):
    pole = round(math.pi * math.pow(r, 2), 3)
    return pole


def obwod_kola(r):
    obwod = round(2 * math.pi * r, 3)
    return obwod

r = input('Podaj promien kola: ')
print('Pole kola o promieniu ' +str(r)+ 'wynosi: ' + str(pole_kola(int(r))))
print('Obwod kola o promieniu ' +str(r)+ 'wynosi: ' + str(obwod_kola(int(r))))
