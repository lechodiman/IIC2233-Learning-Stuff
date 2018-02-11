from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
iris = datasets.load_iris()

# iris is a Bunch, similar do a dictionary
print(type(iris))

print(iris.keys())
pd.scatter_matrix()
df = pd.DataFrame()
df.to_csv()
