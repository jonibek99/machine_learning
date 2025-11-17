import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv('house.csv')
train_set,test_set=train_test_split(df,test_size=0.2,random_state=35)
print(train_set.head())

