import numpy as np

rng = np.random.default_rng(123)

targets = rng.uniform(low=0,
                      high=1,
                      size=20) >= 0.6


preds = np.round(rng.uniform(low=0,
                             high=1,
                             size=20), 2)

c = rng.choice(a = np.arange(14),
              size = 5,
              replace = False)

v = np.sort(preds[c])
preds[np.sort(c)] = v
print(preds)

def accuracy_rate(preds, targets):
    return np.mean((preds >= 0.5) == targets)

print(accuracy_rate(preds, targets), 'teste preds')



#print(accuracy_rate(preds3, targets

#i = np.in1d(preds[c], preds)

#t = np.take(preds, c)

#s = np.argsort(preds[c])

#i = np.array([ 8, 15, 11,  6,  1])
#preds2 = np.insert(np.delete(preds, i), np.sort(i), np.sort(preds[i]))
#print(preds2, 'preds2\n')
