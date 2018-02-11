# Decision Tree
from sklearn import tree
from sklearn import datasets

# Mass in grams, texture
features = [[140, 1],
            [130, 1],
            [150, 0],
            [170, 0]]

# Apples and oranges
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)

new_samples = [[160, 0]]
print('Prediction: {}'.format(clf.predict(new_samples)))
