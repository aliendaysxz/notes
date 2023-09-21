import numpy as np

rng = np.random.default_rng(1234)
field = np.zeros((10, 10))
print(field)
np.set_printoptions(linewidth=999)

vals = np.round(rng.normal(size = 20),2)
locs = rng.choice(field.size,  20, replace=False)
field.ravel()[locs] = vals
print(field)
