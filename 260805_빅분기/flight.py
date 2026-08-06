import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

train = pd.read_csv('flight_train.csv')
test = pd.read_csv('flight_test.csv')

# print(train.head())
# airline   flight source_city departure_time stops arrival_time destination_city     class  duration  days_left  price

# print(train.info())

# print(train.shape, test.shape) # (10505, 11) (4502, 10)

# print(train.isnull().sum()) # 학습 데이터 결측치 없음

# print(train.dtypes)

# 인코딩 대상 컬럼
cols = ['airline', 'flight', 'source_city', 'departure_time', 'stops',
       'arrival_time', 'destination_city', 'class']

target = train.pop('price')

df = pd.concat([train, test])

le = LabelEncoder()

for col in cols:
    df[col] = le.fit_transform(df[col])

# print(df.info())

train = df.iloc[:len(train)].copy()
test = df.iloc[len(test):].copy()

X_train, X_val, y_train, y_val = train_test_split(train, target,test_size=0.2, random_state=0)

# lr = LinearRegression()
# lr.fit(X_train, y_train)  # 학습
# y_pred = lr.predict(X_val) # 예측
# print(y_pred)

# result = root_mean_squared_error(y_val, y_pred)
# print(result) # 6947.877807956758

rf = RandomForestRegressor(random_state=0)
rf.fit(X_train, y_train) # 학습
# y_pred = rf.predict(X_val) # 예측
# result = root_mean_squared_error(y_val, y_pred)
# print(result) # 3786.24800904035 --> 오차가 줄었다.

pred = rf.predict(test)
print(pred)

submit = pd.DataFrame({'pred':pred})
print(submit.head())