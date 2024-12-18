# -*- coding: utf-8 -*-
"""Module6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cmZ0YLZqTxanWsmAYc3OubBNxxqv6iBY
"""

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from google.colab import files

df = pd.read_csv("/content/cleaned_application_data.csv")
df = df[['TARGET', 'CODE_GENDER', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'CNT_CHILDREN']]

df = df[df['CODE_GENDER'].isin(['M', 'F'])]
# print(df.shape)

mlb_gender = MultiLabelBinarizer()
gender_labels = mlb_gender.fit_transform(df['CODE_GENDER'])
temp_gender = pd.DataFrame(gender_labels, columns=mlb_gender.classes_)

df = pd.concat([df, temp_gender], axis=1)
df = df.drop(columns=['CODE_GENDER'])

x = df[['AMT_INCOME_TOTAL', 'AMT_CREDIT', 'CNT_CHILDREN', 'F', 'M']]
y = df['TARGET']
x = x.fillna(x.median())
y = y.dropna()
x = x.loc[y.index]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x_train, y_train)
test_pred = neigh.predict(x_test)

print("Classification Report for KNN:")
print(classification_report(y_test, test_pred))
print("Test Accuracy:", accuracy_score(y_test, test_pred))

incorrect_indices = np.where(test_pred != y_test)[0]
incorrect_samples = x_test.iloc[incorrect_indices]
incorrect_true_labels = y_test.iloc[incorrect_indices]
incorrect_pred_labels = test_pred[incorrect_indices]

print("\nFive incorrect predictions:")
for i in range(min(5, len(incorrect_indices))):
    print(f"Sample {i + 1}:")
    print(incorrect_samples.iloc[i])
    print(f"True Label: {incorrect_true_labels.iloc[i]}")
    print(f"Predicted Label: {incorrect_pred_labels[i]}")
    print("-----------------------------")