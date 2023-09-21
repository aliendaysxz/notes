import numpy as np
import pandas as pd

rng = np.random.default_rng(123)

coaches = pd.Series(['Aaron', 'Donald', 'Joshua', 'Peter', 'Scott', 'Stephen'],
                    dtype='string')
players = pd.Series(['Asher', 'Connor', 'Elizabeth', 'Emily', 'Ethan', 'Hannah', 'Isabella', 'Isaiah', 'James',
                     'Joshua', 'Julian', 'Layla', 'Leo', 'Madison', 'Mia', 'Oliver', 'Ryan', 'Scarlett', 'William',
                     'Wyatt'],
                    dtype='string')
print(coaches,'\n')
print(players,'\n')

a = coaches.to_numpy()
b = rng.choice(players.index, 19, replace = False)
c = players.loc[b].to_numpy()

dic = {'Aaron' : c[:3],
       'Donald': c[3:6],
       'Joshua' : c[6:9],
       'Peter' : c[9:12],
       'Scott' : c[12:15],
       'Stephen' : c[15:19]}

e = pd.Series(dic)

#############
co = coaches.sample(frac=1,
                   random_state=2357)

pl = players.sample(frac=1,
                   random_state=7532)

repeats = np.ceil(len(pl)/len(co)).astype('int64')

co_repeated = pd.concat([co] * repeats).head(len(pl))
result = pl.copy()
result.index = pd.Index(co_repeated, name='coach')
print(result)
