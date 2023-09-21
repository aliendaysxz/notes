import numpy as np

arr1 = np.linspace(17,28,3)
arr2 = np.linspace(32,36,3)
print(arr1,arr2)

d1 = 30 - arr1[1]
d2 = arr2[1] - 30

print('distância 1 =', d1, '\ndistância =', d2)

print('\n--------alt/testes---------\n')

arr3 = np.linspace([17,32], [28,36], 3, axis=0)
print(arr3)
arr4 = np.linspace([17,32], [28,36], 3, axis=1)
print(arr4)

arr5 = np.abs(arr4-30)[[0,1],[1,1]]
print(arr5)
