import pandas as pd

# Carregando o dataset
df = pd.read_csv('caminho/do/arquivo/water_quality.csv')  # substitua pelo caminho correto

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=1)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

print("Decision Tree Classification Report")
print(classification_report(y_test, y_pred_dt))
