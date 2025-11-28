from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

df=pd.read_csv('house.csv')
X = df.drop('price_$', axis=1) 
y = df["price_$"] 

linear_regression = LinearRegression()


linear_regression.fit(X, y)

predick=linear_regression.predict(df)

print(predick)
