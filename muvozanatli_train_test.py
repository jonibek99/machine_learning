import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

df = pd.read_csv('house.csv')
df.reset_index(drop=True, inplace=True)

# Narxni 3 ta kategoriya bo'yicha ajratish
df['price_cat'] = pd.cut(df['price_$'],
                         bins=[0, 100000, 200000, np.inf],
                         labels=['low', 'medium', 'high'])

# Stratified sampling
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=25)
for train_index, test_index in split.split(df, df['price_cat']):
    train_index = df.loc[train_index]
    test_index = df.loc[test_index]
print(train_index.drop('price_cat',axis=1,inplace=True))


