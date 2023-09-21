import pandas as pd
import numpy as np

df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)

s = pd.Series([2, 4, 6, 8, 10])
print(s)

#s
#0     2
#1     4
#2     6
#3     8
#4    10
#dtype: int64

#s.value_counts(dropna=False)
#2     1
#4     1
#6     1
#8     1
#10    1
#Name: count, dtype: int64

#df.apply(pd.Series.value_counts)
#      X    Y    Z
#72  NaN  NaN  1.0
#78  1.0  NaN  NaN
#80  1.0  NaN  NaN
#83  NaN  1.0  1.0
#84  NaN  1.0  NaN
#85  1.0  NaN  NaN
#86  1.0  1.0  1.0
#89  NaN  1.0  NaN
#94  NaN  1.0  NaN
#96  1.0  NaN  1.0
#97  NaN  NaN  1.0

#s.mean()
#6.0

#s.replace([2,3,8],['two', 'three', 'eight'])
#0      two
#1        4
#2        6
#3    eight
#4       10
#dtype: object

#df.rename(columns={'old_name': 'new_ name'})	
