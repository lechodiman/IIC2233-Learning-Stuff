import pandas as pd
from sklearn import cross_validation, preprocessing
from sklearn.linear_model import LinearRegression
import numpy as np
import math

df = pd.read_csv('tabla final utilizada.txt')

# gdp = np.array(pd.read_csv('gdp.txt'))

df = df[['IDC', 'largopob1', 'carretcant2']]

X = np.array(df.drop(['IDC'], 1))

y = np.array(df['IDC'])

# use 20 percent of data as test data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(accuracy)

# linear regression N
clf = LinearRegression()
clf.fit(X, y)
data_47 = np.array(clf.coef_)

# 2/3 N
clf = LinearRegression()
X_2 = X[0: int(2 * len(X) / 3)]
y_2 = y[0: int(2 * len(y) / 3)]
clf.fit(X_2, y_2)
data_31 = np.array(clf.coef_)

# N/2
clf = LinearRegression()
X_3 = X[0: int(len(X) / 2)]
y_3 = y[0: int(len(y) / 2)]
clf.fit(X_3, y_3)
data_23 = np.array(clf.coef_)

new_df = pd.DataFrame({'N': data_47, '2N/3': data_31, 'N/2': data_23})
print(new_df.head())

# new_df.to_csv('Sensitivity_Analisis.csv')
# new_df.to_excel('Sensitivity_Analisis.xlsx')
