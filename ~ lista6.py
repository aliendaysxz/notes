import numpy as np
import jovian
jovian.commit(project='100-numpy-exercicios')

rng = np.random.default_rng(123)
#3
a = np.zeros((10))
print(a,'a\n')

#4 
print(a.dtype,'\n')

#5 
#print(np.info(np.where)'\n')

#6
b = np.zeros((10))
b[4] = 1
print(b,'b\n')

#7
c = rng.integers(10,50,10)
print(c,'c\n')

#8
d = c[::-1]
print(d,'d\n')

#9
e = np.arange(0,9).reshape(3,3)
print(e,'e\n')

#10
f = np.array([1,2,0,0,4,0])
g = f > 0
h = np.where(g)[0]
print(h,'h\n')

#11
i = rng.integers(0,10,(3,3))
print(i,'i\n')

#12
j = rng.integers(0,50,(3,3,3))
print(j,'j\n')

#13
k = rng.integers(0,100,(10,10))
print(k,'k\n')
print('MAX',np.amax(k),'MIN', np.amin(k), '\n')

#14
print(np.mean(rng.integers(0,50,30)), '\n')

#15
#x = int(input('linhas: '))
#y = int(input('colunas: '))
#l = np.zeros((x,y))
l = np.zeros((4,4))
l[0] = 1
l[-1] = 1
l[:,0] = 1
l[:,-1] = 1
print(l,'l\n')

#16
def defmirabolante(axis, pos):
    linhas = k.shape[0]
    colunas = k.shape[1]
    if axis == 0:
        if pos == -1:
            out = np.vstack((k, np.zeros(colunas)))
        elif pos == 0:
            out = np.vstack((np.zeros(colunas), k))
    elif axis == 1:
        if pos == -1:
            out = np.hstack((k, np.zeros(linhas)[:,np.newaxis]))
        elif pos == 0:
            out = np.hstack((np.zeros(linhas)[:,np.newaxis], k))
    return out

#axis = int(input('axis: '))
#pos = int(input('posição: '))
#print(defmirabolante(axis, pos))

#17

# >>> 0 * np.nan
##### nan

# >>> np.nan == np.nan         #True
##### False

# >>> np.inf > np.nan          #False
##### False

# >>> np.nan - np.nan          #nan
##### nan

# >>> np.nan in set([np.nan])  #False
##### True

# >>> 0.3 == 3 * 0.1           #False
##### False

# >>> 3 * 0.1 == 0.3
##### False

# >>> 3 * 0.1
##### 0.30000000000000004    (?????)

#18
m = np.diag([1,2,3,4], k=-1)
print(m,'m\n')

#19
x = np.arange(0,8,2)
y = np.arange(1,8,2)
z = np.zeros((8,8))
z[[x[:,np.newaxis]], [x]] = 1
z[[y[:,np.newaxis]], [y]] = 1
print(z, 'z\n')

#20
p = np.round(rng.uniform(0,50,(6,7,8)),2)
v = p.reshape(1,-1)[0][100]

dim, lin, col = np.where(p == v)
print('dimensão: ', dim)
print('linha: ', lin)
print('coluna: ', col)
