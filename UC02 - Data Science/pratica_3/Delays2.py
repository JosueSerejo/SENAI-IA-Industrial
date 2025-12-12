import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

# 1. CARREGAR O CSV
df = pd.read_csv("Dataset_sint_tico_de_voos.csv")

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

# 4. TRATAMENTO DE TIPOS E LIMPEZA
if "data_voo" in df.columns:
    df["data_voo"] = pd.to_datetime(df["data_voo"], errors="coerce")

for c in col_cat:
    df[c] = df[c].astype(str).str.strip()

for col in ["atraso_partida", "atraso_chegada"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# 5. CRIAR FEATURES (ENGINEERING)
delay_col = "atraso_chegada"

if delay_col in df.columns:
    df["ATRASO_15"] = np.where(df[delay_col] > 15, 1, 0)
    df["ATRASO_ABS"] = df[delay_col].abs()

if "horario_partida" in df.columns:
    df["hora_partida"] = df["horario_partida"] // 100

print("\nPrimeiras linhas após feature engineering:")
print(df.head())

# 6. DISTRIBUIÇÃO DOS ATRASOS
if delay_col in df.columns:
    print("\nProporção de atrasos > 15 min:", df["ATRASO_15"].mean())

    plt.figure(figsize=(10,5))
    sns.histplot(df[delay_col], kde=True, bins=30)
    plt.title("Distribuição dos Atrasos (Chegada)")
    plt.show()

# 7. OUTLIERS (IQR)
if delay_col in df.columns:
    Q1 = df[delay_col].quantile(0.25)
    Q3 = df[delay_col].quantile(0.75)
    IQR = Q3 - Q1

    low = Q1 - 1.5 * IQR
    high = Q3 + 1.5 * IQR

    print("\nLimite inferior:", low)
    print("Limite superior:", high)

    outliers = df[(df[delay_col] < low) | (df[delay_col] > high)]
    print("Total de outliers:", outliers.shape[0])

# 8. CORRELAÇÃO
if len(col_num) > 1:
    plt.figure(figsize=(12,8))
    sns.heatmap(df[col_num].corr(), cmap="coolwarm")
    plt.title("Mapa de Correlação")
    plt.show()

# 9. AEROPORTOS QUE MAIS ATRASAM
if delay_col in df.columns and "origem" in df.columns:
    top = df.groupby("origem")[delay_col].mean().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    sns.barplot(x=top.index, y=top.values)
    plt.title("Top 10 Aeroportos com Maior Média de Atraso (Chegada)")
    plt.xticks(rotation=45)
    plt.ylabel("Média de Atraso (min)")
    plt.show()

# 10. SALVAR DATASET LIMPO
df.to_csv("dataset_limpo_pratica2.csv", index=False)
print("\nDataset limpo salvo como 'dataset_limpo_pratica2.csv'!")