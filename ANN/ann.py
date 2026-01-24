import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Veri Setinin Yüklenmesi [cite: 3031, 3032]
data = pd.read_csv('prostate_cancer_data.csv')

# Özellik (PSA) ve Etiket (Cancer) seçimi [cite: 3038, 3039, 3040]
X = data[['PSA']].values
y = data['Cancer'].values

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
sns.histplot(data['PSA'], kde=True, color='blue', bins=10)
plt.title('Distribution of PSA Levels')
plt.xlabel('PSA Level')
plt.ylabel('Frequency')

# Dağılım Grafiği 
plt.subplot(2, 2, 2)
sns.scatterplot(x=data['PSA'], y=data['Cancer'], color='red')
plt.title('PSA vs Cancer (1 = Cancer, 0 = No Cancer)')
plt.xlabel('PSA Level')
plt.ylabel('Cancer (0 or 1)')

plt.tight_layout()
plt.show()

# 3. Verinin Eğitim ve Test Setlerine Ayrılması [cite: 3096, 3097]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizasyon [cite: 3098, 3099, 3100]
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Yapay Sinir Ağı (ANN) Modelinin Oluşturulması [cite: 3102, 3103]
model = Sequential()

model.add(Dense(units=8, activation='relu', input_dim=1))
model.add(Dense(units=8, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğitme (100 epoch) [cite: 3123, 3127, 3128]
history = model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=0)


plt.figure(figsize=(10, 6))
plt.plot(history.history['accuracy'])
plt.title('Training Accuracy Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()

y_pred = (model.predict(X_test) > 0.5).astype("int32")
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Hata Matrisi (Confusion Matrix) [cite: 3161, 3162]
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['No Cancer', 'Cancer'], yticklabels=['No Cancer', 'Cancer'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()