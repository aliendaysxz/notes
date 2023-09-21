import numpy as np
import pandas as pd

bees = pd.Series([True, True, False, np.nan, True, False, True, np.nan])
knees = pd.Series([5,2,9,1,3,10,5,2], index = [7,0,2,6,3,5,1,4])

x = bees.loc[pd.isna].index
knees.iloc[x] = knees.iloc[x].to_numpy() * 2
print(knees)

#########

knees.loc[pd.isna(bees).to_numpy()] *= 2

#knees
#7     5
#0     2
#2     9
#6     2
#3     3
#5    10
#1     5
#4     4
#dtype: int64
