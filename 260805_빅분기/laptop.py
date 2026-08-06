import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

train = pd.read_csv('laptop_train.csv')
test = pd.read_csv('laptop_test.csv')

# print(train.head())
# print(train.isnull().sum())
# print(train.info())

print(train.select_dtypes(include="str").columns)

cols = ['Brand', 'Model', 'Series', 'Processor', 'Processor_Gen',
       'Hard_Disk_Capacity', 'OS']

target = train.pop('Rating')