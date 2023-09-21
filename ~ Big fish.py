import numpy as np

locs = np.array([
    [0,0,0],
    [1,1,2],
    [0,0,0],
    [2,1,3],
    [5,5,4],
    [5,0,0],
    [5,0,0],
    [0,0,0],
    [2,1,3],
    [1,3,1]
])

rng = np.random.default_rng(1010)
weights = rng.normal(size=10)

sorted_fish = np.argsort(weights)[::-1]
uniques, first_idxs = np.unique(locs[sorted_fish],
                                axis = 0,
                                return_index = True)
survivors = sorted_fish[first_idxs]
print(survivors)

#7 000, 4 554, 1 112, 6 500, 9 131, 2 7, 3 213, 8 3, 5 6, 0 7
