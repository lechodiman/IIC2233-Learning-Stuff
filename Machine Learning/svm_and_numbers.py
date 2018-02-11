import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100)

X, y = digits.data[:-10].reshape(1, -1), digits.target[:-10]
clf.fit(X, y)

for i in range(10, 0, -1):
    print('Prediction: {}'.format(clf.predict(digits.data[-i])))
    print('Real: {}'.format(digits.target[-i]))

    # plt.imshow(digits.images[-i], cmap=plt.cm.gray_r, interpolation='nearest')

plt.show()
