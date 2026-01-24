import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris.data[:, :2] 
y = iris.target
target_names = iris.target_names 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = svm.SVC(kernel='linear', C=1.0) 
clf.fit(X_train, y_train)

w = clf.coef_[0]
b = clf.intercept_[0]

slope = -w[0] / w[1]
intercept = -b / w[1]

for i in range(len(target_names)):
    plt.scatter(X[y == i, 0], X[y == i, 1], label=target_names[i], s=50)

xx = np.linspace(min(X[:, 0]), max(X[:, 0]), 100)
yy = slope * xx + intercept

plt.plot(xx, yy, 'k-', label='Decision Boundary')

support_vectors = clf.support_vectors_
plt.scatter(support_vectors[:,0], support_vectors[:,1], s=150, facecolors='none', edgecolors='k', label='Support Vectors')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('SVM Decision Boundary and Support Vectors')
plt.legend()
plt.show()

accuracy = clf.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')