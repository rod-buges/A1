import pandas as pd

# Carregando o dataset
df = pd.read_csv('C:/Users/Rodrigo Buges/Downloads/a1/waterQuality1.csv')

# Visualizando as primeiras linhas
print(df.head())

# Visualizando as últimas linhas
print(df.tail())

# Verificando os tipos de dados
print(df.dtypes)