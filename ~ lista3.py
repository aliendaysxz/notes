import pandas as pd
import numpy as np
#https://github.com/qodatecnologia/exercicios-pandas/blob/master/Pandas.ipynb

lista_2 = list('abcedfghijklmnopqrstuvwxyz')
arr = np.arange(26)
dic_2 = dict(zip(lista_2, arr))

ser1 = pd.Series(lista_2)
ser2 = pd.Series(arr)
ser3 = pd.Series(dic_2)
print(ser3.head())

