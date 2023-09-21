import pandas as pd
import numpy as np

#https://github.com/qodatecnologia/exercicios-pandas/blob/master/Pandas.ipynb

data = np.array([2,4,6,8,10])
sa = pd.Series(data)
print(sa,'sa\n')

sb = pd.Series(data = data,
               index = [1001,1002,1003,1004,1005])
print(sb,'sb\n')

###
dic_1 = {'A' : 10, 'B' : 20, 'C' : 30}
sc = pd.Series(dic_1)
print(sc,'sc\n')


sd = pd.Series(data=dic_1,
               index=['B','C','A'])
print(sd,'sd\n')

se = pd.Series(data=dic_1,
               index=['A','B','C','D'])
print(se,'se\n')

###
lista_1 = [11,22,33,44,55]
sf = pd.Series(lista_1)
print(sf,'sf\n')

sg = pd.Series(data=lista_1,
               index=['a','b','c','d','e'])
print(sg,'sg\n')

###
#df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")  
#ser = pd.Series(df['Name'])
#print(ser.head(10))

###
lista_2 = list('abcedfghijklmnopqrstuvwxyz')
arr = np.arange(26)
dic_2 = dict(zip(lista_2, arr))

ser1 = pd.Series(lista_2)
ser2 = pd.Series(arr)
ser3 = pd.Series(dic_2)
print(ser3.head())
