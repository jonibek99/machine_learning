# import matplotlib.pyplot as plt 
# import seaborn as sns
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import StratifiedShuffleSplit

# df = pd.read_csv('house.csv')

# df['rooms_per_households']=df['total_rooms']/df['total_households']
# df['bedrooms_per_room']=df['rooms']/df['total_rooms']
# df['average_area_m2']=df['average_price_$']/df['total_households']
# df.corrwith(df['price_$'].sort_values(ascending=False))
# print(df)
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

df = pd.read_csv('house.csv')

# price_$ ustunini float ga o'tkazish (agar CSVda $ bo'lsa)
df['price_$'] = df['price_$'].replace('[\$,]', '', regex=True).astype(float)

# qo'shimcha ustunlar
df['total_rooms'] = df['rooms'].sum()
df['total_households'] = len(df)
df['rooms_per_household'] = df['total_rooms'] / df['total_households']
df['bedrooms_per_room'] = df['rooms'] / df['total_rooms']
df['average_area_m2'] = df['area_m2'].mean()
df['average_price_$'] = df['price_$'].mean()

# price_$ bilan korrelyatsiya
corr_matrix = df.corr()
print(corr_matrix['price_$'])

# DataFrame ni tekshirish
print(df.head())
