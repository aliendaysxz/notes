import numpy as np

a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
doublediff = np.diff(np.sign(np.diff(a)))
picos = np.where(doublediff == -2)[0] + 1
print(picos)



np.random.seed(101)
arr = np.random.randint(1,4, size=6)
print(arr)

def valor_unico(arr):
    uniqs = np.unique(arr)
    out = np.zeros((arr.shape[0], uniqs.shape[0]))
    for i,k in enumerate(arr):
        out[i,k-1] = 1
    return out

print(valor_unico(arr))
