import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# URL do dataset (UCI Machine Learning Repository)
f_csv = 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

# Nomes das colunas conforme documentação do dataset
column_names = [
    'symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 
    'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 
    'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 
    'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 
    'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 
    'price'
]

# Leitura do arquivo CSV e definição de valores ausentes
df = pd.read_csv(f_csv, names=column_names, na_values='?')

# Remoção de registros sem valor de preço (variável alvo)
df = df.dropna(subset=['price'])

# Lista de colunas numéricas que terão imputação pela média
numeric_cols_to_impute = ['normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm']

# Conversão para numérico e imputação da média
for col in numeric_cols_to_impute:
    df[col] = pd.to_numeric(df[col])
    mean_val = df[col].mean()
    df[col] = df[col].fillna(mean_val)

# Imputação da moda para a variável categórica 'num-of-doors'
mode_val = df['num-of-doors'].mode()[0]
df['num-of-doors'] = df['num-of-doors'].fillna(mode_val)

# Codificação ordinal da variável 'num-of-cylinders'
cylinder_map = {
    'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'eight': 8, 'twelve': 12
}
df['num-of-cylinders_encoded'] = df['num-of-cylinders'].map(cylinder_map)

# Variáveis categóricas nominais para One-Hot Encoding
nominal_cols = [
    'make', 'fuel-type', 'aspiration', 'body-style', 'drive-wheels',
    'engine-type', 'fuel-system', 'num-of-doors', 'engine-location'
]

# Aplicação do One-Hot Encoding
df_encoded = pd.get_dummies(
    df,
    columns=nominal_cols,
    drop_first=True,
    dtype=int
)

# Remoção da coluna categórica original após codificação
df_encoded.drop('num-of-cylinders', axis=1, inplace=True)

# Visualizações exploratórias
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
sns.histplot(df_encoded['price'], kde=True)
plt.title('Distribuição da Variável Target (Price)')
plt.xlabel('Preço (USD)')

plt.subplot(1, 2, 2)
sns.boxplot(x='body-style', y='price', data=df)
plt.title('Preço vs. Estilo da Carroceria')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# Matriz de correlação entre principais variáveis numéricas
corr_matrix = df_encoded[
    ['price', 'horsepower', 'engine-size', 'curb-weight', 'city-mpg']
].corr()

plt.figure(figsize=(7, 6))
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True, fmt='.2f')
plt.title('Mapa de Calor de Correlação (Principais Features)')
plt.show()
