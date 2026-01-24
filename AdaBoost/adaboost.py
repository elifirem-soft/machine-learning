from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Initialize the base classifier (Decision Tree)
base_classifier = DecisionTreeClassifier(max_depth=1) 

# Step 4: Initialize the AdaBoost model with the base classifier
ada_boost = AdaBoostClassifier(base_classifier, n_estimators=50, random_state=42)

# Step 5: Train the AdaBoost model
ada_boost.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = ada_boost.predict(X_test)

# Step 7: Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of AdaBoost model: {accuracy:.2f}")

# Step 8: Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Step 9: Plot the confusion matrix using seaborn heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=data.target_names, yticklabels=data.target_names)
plt.title('Confusion Matrix for AdaBoost Model')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()
