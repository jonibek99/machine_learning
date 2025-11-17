import pandas as pd
import numpy as np
from sklearn.base import check_array
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
min_max_scaller=MinMaxScaler()
df=pd.read_csv('house.csv')
# median=df['total_rooms'].median()
# xmin=df['total_rooms'].min()
# xmax=df['total_rooms'].max()
# xnew=(median-xmax)/(xmax-xmin)
# print(xnew)
housing_num=df[['area_m2','rooms','price_$','total_rooms','total_households','average_area_m2','average_price_$','oldest_built_year']].median()
min_max_scaller.fit_transform(housing_num)
print(min_max_scaller)