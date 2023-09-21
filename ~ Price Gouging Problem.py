import numpy as np
import pandas as pd

rng = np.random.default_rng(123)

b = pd.Series(
    data = np.round(rng.uniform(3, 5, 10), 2),
    index = rng.choice(10, 10, replace=False)
)

print(b,'b\n')

c = b[np.sort(b.index.to_numpy())][:-1].reset_index(drop=True)
d = b[np.sort(b.index.to_numpy())][1:].reset_index(drop=True)
e = d - c
print(e,'e\n')

f = pd.Series(
    data = e.max(),
    index = [e.idxmax()+1])

print(f,'f\n')

##########

b.sort_index(inplace=True)
g = b.shift(periods=1)
h = b - g
print(h.idxmax())
