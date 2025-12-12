import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")


# 1. CARREGAR O ARQUIVO CSV
df = pd.read_csv("flights_100.csv")

print("Arquivo carregado!\n")

# 2. VISÃO GERAL DO DATASET
print("Dimensão do dataset:", df.shape)
print("\nTipos de variáveis:")
print(df.info())
print("\nValores nulos por coluna:")
print(df.isna().sum())

col_num = df.select_dtypes(include=[np.number]).columns.tolist()
col_cat = df.select_dtypes(exclude=[np.number]).columns.tolist()

print("\nColunas numéricas:", col_num)
print("Colunas categóricas:", col_cat)

# 3. ESTATÍSTICAS DESCRITIVAS
print("\nEstatísticas descritivas:")
print(df.describe(include="all"))

# 4. LIMPEZA E CONVERSÃO DE TIPOS
if "FL_DATE" in df.columns:
    df["FL_DATE"] = pd.to_datetime(df["FL_DATE"], errors="coerce")

for c in col_cat:
    df[c] = df[c].astype(str).str.strip()

for col in ["DEP_DELAY", "ARR_DELAY"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# 5. CRIAR VARIÁVEL ALVO - ATRASO > 15 MIN
delay_column = "ARR_DELAY"

if delay_column in df.columns:
    df["ATRASO_15"] = np.where(df[delay_column] > 15, 1, 0)
    df["ATRASO_ABS"] = df[delay_column].abs()

print("\nPrimeiras linhas com variável ATRASO_15:")
print(df.head())

# 6. DISTRIBUIÇÃO DOS ATRASOS
if delay_column in df.columns:
    print("\nProporção de atrasos > 15 min:", df["ATRASO_15"].mean())

    plt.figure(figsize=(10,5))
    sns.histplot(df[delay_column], kde=True, bins=30)
    plt.title("Distribuição dos Atrasos (ARR_DELAY)")
    plt.show()

# 7. DETECÇÃO DE OUTLIERS - IQR
if delay_column in df.columns:
    Q1 = df[delay_column].quantile(0.25)
    Q3 = df[delay_column].quantile(0.75)
    IQR = Q3 - Q1

    limite_inf = Q1 - 1.5 * IQR
    limite_sup = Q3 + 1.5 * IQR

    print("\nLimite inferior:", limite_inf)
    print("Limite superior:", limite_sup)

    outliers = df[(df[delay_column] < limite_inf) | (df[delay_column] > limite_sup)]
    print("Total de outliers:", outliers.shape[0])

# 8. MAPA DE CORRELAÇÃO
if len(col_num) > 1:
    plt.figure(figsize=(12,8))
    sns.heatmap(df[col_num].corr(), cmap="coolwarm")
    plt.title("Mapa de Correlação das Variáveis Numéricas")
    plt.show()

# 9. TOP AEROPORTOS COM MAIOR MÉDIA DE ATRASO
if delay_column in df.columns and "ORIGIN" in df.columns:
    top = df.groupby("ORIGIN")[delay_column].mean().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    sns.barplot(x=top.index, y=top.values)
    plt.title("Top 10 Aeroportos com Maior Média de Atraso")
    plt.ylabel("Média de ArrDelay")
    plt.xticks(rotation=45)
    plt.show()

# 10. SALVAR DATASET LIMPO
df.to_csv("dataset_limpo.csv", index=False)
print("\nDataset limpo salvo como 'dataset_limpo.csv'!")
