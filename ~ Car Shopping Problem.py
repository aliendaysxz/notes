import numpy as np
import pandas as pd

a = pd.Series([5000, 7600, 9000, 8500, 7000],
              index=['civic', 'civic', 'camry', 'mustang', 'mustang'])
print(a,'a\n')
f = pd.Series([5500, 7500, 7500],
              index=['civic', 'mustang', 'camry'])
print(f,'f\n')

#print(a['civic'][a['civic'] < f['civic']])
#print(a['mustang'][a['mustang'] < f['mustang']])
#print(a['camry'][a['camry'] < f['camry']])

###########

b = f.loc[a.index]
print(b,'b\n')
c = a - b
print(c,'c\n')
d = (c < 0).reset_index(drop=True)
print(d,'d\n')
print(d.loc[d].index.to_list())
