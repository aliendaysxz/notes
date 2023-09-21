import numpy as np
rng = np.random.default_rng(123)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
 
iris_2d[rng.integers(0,150,20), rng.integers(0,4,20)] = np.nan

print(iris_2d[np.all(~np.isnan(iris_2d), axis=1)])







# Método 2
nan = np.array([~np.any(np.isnan(row)) for row in iris_2d])
print(iris_2d[nan])

# Método 3
print(iris_2d[np.sum(np.isnan(iris_2d), axis = 1) == 0])



