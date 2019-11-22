a = set([1, 2, 5])
b = set([1, 3, 4])

logic_sum = a.union(b)
logic_intersection = a.intersection(b)
logic_difference = a.difference(b)

print('a='+str(a)+'\nb='+str(b))
print('\nSuma logiczna: ' + str(logic_sum))
print('Część wspólna: ' + str(logic_intersection))
print('Różnica: ' + str(logic_difference))
