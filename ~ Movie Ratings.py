import numpy as np

rng = np.random.default_rng(123)
ratings = np.round(rng.uniform(low=0.0, high=10.0, size=(10, 2)))
ratings[[1,2,7,9], [0,0,0,0]] = np.nan

f = ratings[:, 0]
d = ratings[:, 1]

coluna3_1 = np.where(np.isnan(f), d, f).reshape(10,1)

r1 = np.concatenate((ratings, coluna3_1),
                   axis=1
                   )



coluna3_2 = np.where(np.isnan(f), d, f)
r2 = np.insert(arr=ratings,
               values=coluna3_2,
               axis=1,
               obj=2
)

r3 = np.hstack((ratings, coluna3_2[:,None]))

print(r1,'r1\n')
print(r2,'r2\n')
print(r3,'r3\n')

