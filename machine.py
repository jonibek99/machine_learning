from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd.read_csv('house.csv')

X = df.drop('price_$', axis=1)  
y = df['price_$']

# To'g'ri train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model yaratish
linear_regression = LinearRegression()

# Modelni o‘qitish
linear_regression.fit(X_train, y_train)

# Bashorat qilish
predict = linear_regression.predict(X_test)

print(predict)
