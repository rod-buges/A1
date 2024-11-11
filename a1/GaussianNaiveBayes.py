import pandas as pd

# Carregando o dataset
df = pd.read_csv('C:/Users/Rodrigo Buges/Downloads/a1/waterQuality1.csv')

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred_gnb = gnb.predict(X_test)

print("Gaussian Naive Bayes Classification Report")
print(classification_report(y_test, y_pred_gnb))
