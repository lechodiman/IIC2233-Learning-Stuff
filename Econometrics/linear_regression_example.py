import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import cross_validation, preprocessing
import matplotlib.pyplot as plt

n_clients = [8, 7, 6, 4, 2, 1]
distance = [15, 19, 25, 23, 34, 40]

my_dict = {'Number Clients': n_clients, 'Distance': distance}

df = pd.DataFrame(my_dict)

print(df)

X = np.array(df.drop(['Number Clients'], 1))
y = np.array(df['Number Clients'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(fit_intercept=True)
clf.fit(X, y)
accuracy = clf.score(X, y)

print(clf.coef_)
print(clf.intercept_)


def regression_line(x):
    y = clf.coef_[0] * x + clf.intercept_

    return y


print('predicted value:', regression_line(X[4]))
print('real value: ', y[4])

y_values = [regression_line(x) for x in distance]

plt.scatter(X, y_values, color='r')
plt.scatter(X, y, color='k')
plt.xlabel('Distance')
plt.ylabel('Number Clients')
plt.show()
