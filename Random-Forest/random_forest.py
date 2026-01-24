import pandas as pd
import numpy as np
data_set = pd.read_csv('CreditCard.csv')
print (data_set.head())

df = pd.get_dummies(data=data_set, drop_first=True)
y = df.card_yes
X = df.drop(columns=['card_yes'])
print(X.head())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42, stratify = y)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators = 50, random_state = 42)
model.fit(X_train, y_train)

model_predict = model.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, model_predict))