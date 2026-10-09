import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets # Importing datasets
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])

iris_data = datasets.load_iris()
X, y = iris_data.data, iris_data.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1333)

print(X_train.shape)
print(X_train[0])

print(y_train.shape)
print(y_train)

plt.figure(figsize=(5,5))
plt.scatter(X[:,0],X[:,1], c = y, cmap = cmap, s=20)
plt.show()

