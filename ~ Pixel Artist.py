import numpy as np

rng = np.random.default_rng(1234)
imgs = np.round(rng.uniform(low=0, high=1, size=(5,3,10,10)))
#img, canal de cores, linha de pixels,coluna de pixels

a = imgs[:][:].reshape(5,3,100,1)

b = np.hstack((a[0][0],a[0][1],a[0][2]))
c = np.hstack((a[1][0],a[1][1],a[1][2]))
d = np.hstack((a[2][0],a[2][1],a[2][2]))
e = np.hstack((a[3][0],a[3][1],a[3][2]))
f = np.hstack((a[4][0],a[4][1],a[4][2]))

r = np.vstack((b,c,d,e,f)).reshape(5,100,3)
print(r)
