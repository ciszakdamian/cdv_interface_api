import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 1], [1, 1]])

print('A = '+str(a))
print('B = '+str(b))


print('A + B = '+str(np.add(a, b)))
print('A * B = '+str(np.matmul(a, b)))