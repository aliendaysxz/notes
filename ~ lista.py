import numpy as np

rng = np.random.default_rng(42)

a = rng.integers(0,9,(3,3))
print(a,'a\n')
b = a >= 5
print(b, ' a >= 5\n')

c = np.array([True,False,True])
print(c,'c\n')

d = np.full((3,3), True, dtype=bool)
print(d,'d\n')

print(a[a % 2 != 0],'imp em a')

a[a % 2 != 0] = -1
print(a, 'imp em a --> -1')
