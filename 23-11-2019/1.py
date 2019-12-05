from sklearn import tree
from random import randrange, uniform


# generator
# Czy pies?
# Wzrost 20cm - 100cm
# Waga 1kg - 100kg
# Ogon 0 - 1.


def generate_date():
    features = []
    labels = []
    area = int(input('Podaj zakres do wygenerowania: '))

    for x in range(area):
        height = randrange(0, 106)
        weight = randrange(0, 106)
        tail = randrange(0, 2)
        features += [[height, weight, tail]]
        if 20 <= height <= 100 and 1 <= weight <= 100 and tail == 1:
            labels += str(1)
        else:
            labels += str(0)

    count1 = round(labels.count('1') / area * 100, 2)
    count0 = round(labels.count('0') / area * 100, 2)
    print('Dane do nauki modelu:')
    print(features)
    print(labels)
    print('Ilosc pasujących: ' + str(count1) + '%')
    print('Ilosc fałszywych: ' + str(count0) + '%')

    clf = tree.DecisionTreeClassifier()
    clf.fit(features, labels)
    test = [[63, 68, 0], [32, 89, 1], [48, 51, 1], [53, 93, 1]]
    value = ['0', '1', '1', '1']
    predict = clf.predict(test)
    print('Test modelu:')
    print('Dane testowe: '+str(test))
    print('Poprawne oznaczenie: '+str(value))
    print('Wynik '+str(predict))

generate_date()
