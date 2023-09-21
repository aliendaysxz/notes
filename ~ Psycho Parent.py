import numpy as np

rng = np.random.default_rng(1234)
field = np.zeros((10, 10))
print(field)
np.set_printoptions(linewidth=999)

a = rng.integers(0,10,20)
b = rng.integers(0,10,20)
vals = np.round(rng.normal(size=20),2)
field[[a],[b]] = vals
print(field)


