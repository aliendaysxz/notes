import numpy as np

np.random.seed(5555)
gold = np.random.randint(low=0, high=10, size=(7,7))
print(gold)

locs = np.array([
    [0,4],
    [2,2],
    [2,3],
    [5,1],
    [6,3]
])

arr = np.array([])

x = 0
for k in list(range(0,5)):
    au = gold[locs[0+x][0], locs[0+x][1]]
    arr = np.append(arr,au)
    x += 1

print('RESP', arr)

print('---alt---')

a = gold[locs[:, 0], locs[:, 1]]
print('RESP', a)

print('\n\n***********roux***********\n\n')



arr1 = np.array([9,0,4,0,1])

n = int(input('n: '))

arrq = (np.arange(n) + 4)**2
print(arrq)
arrz = np.zeros(n)
print(arrz)


def make_roux(n):
    x = 0
    global arr2
    arr2 = np.array([])
    while True:
        arr2 = np.insert(arr2,0,0)
        if len(arr2) >= n-5:
            break
        arr2 = np.insert(arr2,0,arrq[0+x])
        if len(arr2) >= n-5:
            break
        x += 1
    return arr2    

print(make_roux(n))

r = np.concatenate((arr2, arr1))
print(r)


