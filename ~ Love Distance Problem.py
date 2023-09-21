import numpy as np

rng = np.random.default_rng(1010)

a = rng.uniform(0,100,10)
love_scores = np.round(a,2)
print(love_scores)

x = love_scores[np.newaxis, :]
y = love_scores[:, np.newaxis]

result = abs(x-y)

np.set_printoptions(linewidth=100000)
print(result)
