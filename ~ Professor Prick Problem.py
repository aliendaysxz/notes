import numpy as np

rng = np.random.default_rng(80085)
scores = np.round(rng.uniform(30,100,15))
print(scores)

a = scores < 60
print(a)
print(scores[a])

print(scores[(scores < 60).nonzero()[0][:3]])
scores[(scores < 60).nonzero()[0][:3]] = 0
print(scores[(scores < 60).nonzero()[0][:3]])
print(scores)

#scores[np.nonzero(scores < 60)[0][:3]] = 0
#print(scores)
