import pandas as pd

# Carregando o dataset
df = pd.read_csv('C:/Users/Rodrigo Buges/Downloads/a1/waterQuality1.csv')

# Verificando a quantidade de cada classe
print(df['is_safe'].value_counts())

# Reamostragem
c_0 = df[df.is_safe == 0].sample(n=912, random_state=1)
c_1 = df[df.is_safe == 1]

# Concatenando e redefinindo o índice
df = pd.concat([c_0, c_1]).reset_index(drop=True)

# Verificando o resultado
print(df['is_safe'].value_counts())

# Estatísticas descritivas
print(df.describe())

# Matriz de correlação
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

from sklearn.model_selection import train_test_split

# Separando features e label
X = df.drop(columns=['is_safe'])
y = df['is_safe']

# Dividindo os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)




