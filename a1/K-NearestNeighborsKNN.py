import pandas as pd

# Carregando o dataset
df = pd.read_csv('caminho/do/arquivo/water_quality.csv')  # substitua pelo caminho correto

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

print("K-Nearest Neighbors Classification Report")
print(classification_report(y_test, y_pred_knn))
