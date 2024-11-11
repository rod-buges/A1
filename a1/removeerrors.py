import pandas as pd

# Carregando o dataset
df = pd.read_csv('C:/Users/Rodrigo Buges/Downloads/a1/waterQuality1.csv')

# Verificando valores inválidos na coluna "ammonia"
df['ammonia'] = pd.to_numeric(df['ammonia'], errors='coerce')

# Verificando valores inválidos na coluna "is_safe"
df['is_safe'] = pd.to_numeric(df['is_safe'], errors='coerce')

# Removendo registros com valores nulos
df = df.dropna(subset=['ammonia', 'is_safe'])
