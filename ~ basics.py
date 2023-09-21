import numpy as np

rng = np.random.default_rng(42)

vetor = np.array([1,2,3])
matrix = np.array([[1,2,3],
                   [4,5,6]])
matrix3d = np.array([[[1,2,3],
                     [4,5,6]],
                    [[7,8,9],
                     [10,11,12]]])

print(vetor, vetor.ndim, vetor.dtype, vetor.shape,'\n')
print(matrix, matrix.ndim, matrix.dtype, matrix.shape,'\n')
print(matrix3d, matrix3d.ndim, matrix3d.dtype, matrix3d.shape,'\n')

ones = np.ones((10,2))

ones2 = np.ones((3,5))

zeros = np.zeros((5,4,3))

rang = np.arange(0,100,3)

rand = rng.integers(0,10,(7,2))

rand2 = rng.uniform(0,1,(5,3))

rand3 = rng.integers(0,10,(5,3))

rand4 = rng.integers(0,10,(3,5))

matrix2 = rand4 - ones2
#array([[ 5.,  8.,  6.,  2.,  8.],
 ##      [ 3.,  2.,  8.,  2., -1.],
   ##    [ 3.,  6.,  0.,  3.,  0.]])

#np.mean(matrix2) --> 3.6666666666666665

#matrix2.T
##array([[ 5.,  3.,  3.],
  ##     [ 8.,  2.,  6.],
    ##   [ 6.,  8.,  0.],
      ## [ 2.,  2.,  3.],
       ##[ 8., -1.,  0.]])
