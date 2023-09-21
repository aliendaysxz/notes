import numpy as np
import pandas as pd

babynames = pd.Series([
    'Jathonathon', 'Zeltron', 'Ruger', 'Phreddy', 'Ruger', 'Chad', 'Chad',
    'Ruger', 'Ryan', 'Ruger', 'Chad', 'Ryan', 'Phreddy', 'Phreddy', 'Phreddy',
    'Mister', 'Zeltron', 'Ryan', 'Ruger', 'Ruger', 'Jathonathon',
    'Jathonathon', 'Ruger', 'Chad', 'Zeltron'], dtype='string')
# ‘Chad’, ‘Ruger’, and ‘Zeltron’.


a = babynames.to_numpy()

c = np.where(a == 'Chad')
r = np.where(a == 'Ruger')
z = np.where(a == 'Zeltron')

b = pd.Series([len(a[c]), len(a[r]), len(a[z])], index = ['Chad', 'Ruger', 'Zeltron'])

#############
d = babynames.value_counts().loc[['Chad','Ruger','Zeltron']]

#e = pd.Series(np.sort(babynames.value_counts().loc[['Chad','Ruger','Zeltron']].to_numpy()),
 #             index=['Chad','Ruger','Zeltron'])
