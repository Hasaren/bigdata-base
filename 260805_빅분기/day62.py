'''
미국의 1994년 인구 조사 
- 나이, 직업, 학력 등으로 연소득이 5만 달러를 초과 (income 컬럼) 예측 --> 이진분류 문제
- income --> <=50k / >50k 
- 평가지표 --> ROC-AUC 
'''


# 라이브러리 불러오기
import pandas as pd

pd.set_option('display.max_rows', None)  # 모든 행
pd.set_option('display.max_columns', None)  # 모든 컬럼
pd.set_option('display.width', None) # 줄바꿈 없이 넓게

# 데이터 불러오기
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# print(train.head())
# print(train['income'].value_counts())

# EDA 는 
# 1.크기 --> 2.타입 --> 3.통계요약(수치/범주 분리) --> 4.결측치 --> 5.이상치 --> 6.타겟(정답) 분포

# 결측치 확인
# print(train.isnull().sum()) # age, workclass, occupation, hours.per.week, native.country
# print(test.isnull().sum()) # workclass, occupation, native.country   

# 자료형 확인
# print(train.info())
# print(test.info())

# -----------------------------------------------------------------------------------------
# # 결측치 삭제 --> 결측치가 있는 데이터(행) 전체 삭제 --> dropna() 기본값 axis=0 (행 삭제)
# df = train.dropna()
# # print(df.shape)

# # 결측치가 있는 특정 컬럼 기준으로만 행 삭제 --> subset=[...]
# df = train.dropna(subset=['native.country', 'workclass'])
# print(df.isnull().sum())

# # 결측치가 있는 컬럼(열) 자체를 삭제 --> axis=1 --> 열 기준
# df = train.dropna(axis=1)
# print(df.shape) # (29304, 11)
# print(df.info())

# # 결측치가 많은 특정 컬럼을 직접 지정해서 삭제 --> drop (axis=1)
# print(train.shape)
# df = train.drop(['native.country', 'workclass'], axis=1)
# print(df.shape)

# -----------------------------------------------------------------------------------------
# 결측치 채우기 (범주형) --> fillna(값)
# 최빈값(mode)으로 채우기
# m = train['workclass'].mode()
# print(m)  # 0    Private

m = train['workclass'].mode()[0]  # 최빈값
# print(m)
train['workclass'] = train['workclass'].fillna(m)

m = train['native.country'].mode()[0]
train['native.country'] = train['native.country'].fillna(m)

# print(train.isnull().sum())

# 결측치를 아예 새로운 카테고리('X')로 만들어서 채우기
# (최빈값 대체와 달리, "결측이었다는 사실 자체"도 모델이 학습할 수 있게 한다.)
train['occupation'] = train['occupation'].fillna('X')
# print(train.isnull().sum())
# print(train.info())

# -----------------------------------------------------------------------------------------
# 결측치 채우기 (수치형) --> fillna(값)
# age 컬럼을 평균값으로 채우기
value = int(train['age'].mean())  # 사람 나이는 보통 정수로 측정
# print(value)  # 38

train['age'] = train['age'].fillna(value)

# 주당근무시간은 이상치에 덜 민감한 중앙값(median)으로 채우기
value = int(train['hours.per.week'].median())
# print(value) # 40

train['hours.per.week'] = train['hours.per.week'].fillna(value)

# print(train.isnull().sum().sum())
# print(test.isnull().sum())

# test데이터의 결측치는 train에서 구한 값으로 채워야 한다!
# 범주형 --> 최빈값으로 결측치를 채웠다. 
# 수치형 --> 나이는 평균값으로 결측치를 채웠다. 주당일시간은 중앙값으로 채웠다.
test['workclass'] = test['workclass'].fillna(test['workclass'].mode()[0])
test['occupation'] = test['occupation'].fillna(test['occupation'].mode()[0])
test['native.country'] = test['native.country'].fillna(test['native.country'].mode()[0])
test['age'] = test['age'].fillna(test['age'].mean())
test['hours.per.week'] = test['hours.per.week'].fillna(test['hours.per.week'].median())

# print(test.isnull().sum().sum())

# -----------------------------------------------------------------------------------------
# 이상치 처리 --> age가 0보다 작은 값이 있는지 확인
# print(train[train['age'] <= 0])
# print(test[test['age'] <= 0])  # 확인만 한다. 이상치 처리하지 않는다(삭제하지 않는다.)

# age가 1 이상인 데이터만 남긴다 (train만 삭제 처리)
# print(train.shape)
train = train[train['age'] > 0]
# print(train.head())
# print(train.shape)

# ----------------------------------------------------------------------------------------

# 타겟(target, 정답)을 먼저 분리 (전처리 과정에서 X와 y를 함께 다루면 혼동되기 쉽다)
# pop() : 해당 컬럼을 train에서 꺼내면서 동시에 원본 train에서는 제거한다.
y_train = train.pop('income')

# -----------------------------------------------------------------------------------------
# 인코딩 (범주형 -> 숫자)
# 원-핫 인코딩
# 판다스의 get_dummies() : 범주형 컬럼들을 0/1로 이루어진 여러 컬럼으로 자동 변환
# train_oh = pd.get_dummies(train)
# test_oh = pd.get_dummies(test)
# # print(train.shape, test.shape, train_oh.shape, test_oh.shape) # (29301, 15) (3257, 15) (29301, 107) (3257, 102)
# # print(train_oh.info())
# print(test_oh.info())

# 주의!! train과 test를 따로 원핫인코딩하면 카테고리 값의 종류가 서로 달라 생성되는 
#       더미 컬럼의 개수/이름이 어긋날수 있다. (예: train에만 있는 특정 국가명)
#       이를 해결하기 위해 train+test 합친 뒤 한 번에 인코딩 한다.
#       다시 분리하는 것이 안전한 방법
data = pd.concat([train, test], axis=0)  # 위 아래로 합치기(행 단위로 합치기 axis=0)
# print(data.shape) # (32558, 15)
data_oh = pd.get_dummies(data) # 원-핫 인코딩 수행
# print(data_oh.shape)  # (32558, 107)
# print(train.shape) # (29301, 15)

# iloc[행 번호, 열 번호]
# print(len(train))  # 29301
train_oh = data_oh.iloc[:len(train)].copy()  # 0~29300
test_oh = data_oh.iloc[len(train):].copy()  # 29301~ 끝까지 다 
# print(train_oh.shape, test_oh.shape) # (29301, 107) (3257, 107)

# -----------------------------------------------------------------------------------------
# 인코딩 (범주형 -> 숫자)
# 레이블 인코딩 --> 사이킷런
# print(train.info())
cols = train.select_dtypes(include='object').columns 
# print(cols) # Index(['workclass', 'education', 'marital.status', 'occupation',
#     #    'relationship', 'race', 'sex', 'native.country'],
#     #   dtype='object')

from sklearn.preprocessing import LabelEncoder
# train --> fit_transform()
# test --> transform()
for col in cols:
    le = LabelEncoder()
    train[col] = le.fit_transform(train[col])
    test[col] = le.transform(test[col])

# -----------------------------------------------------------------------------------------
# 스케일링
# 수치형 컬럼들을 조정
# print(train.info())
cols = ['age', 'fnlwgt', 'education.num', 'capital.gain', 'capital.loss', 'hours.per.week']

# 여러 스케일러를 비교 실습을 할 때, 이전 스케일링이 누적되지 않도록 원본을 복사해서 시작
#
