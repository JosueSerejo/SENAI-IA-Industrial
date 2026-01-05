import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from xgboost import XGBClassifier

print("Carregando dataset...")
try:
    df = pd.read_csv('flights_delays_120.csv')
    print("Dataset carregado com sucesso!")
except FileNotFoundError:
    print("ERRO: O arquivo 'flights_delays_120.csv' não foi encontrado.")
    exit()

print("\n--- Dimensões do Dataset (Linhas, Colunas) ---")
print(df.shape)

print("\n--- Informações dos Tipos de Dados ---")
print(df.info())

print("\n--- Primeiras 5 linhas ---")
print(df.head())


print("\nPreparando os dados...")

X = df.drop('delayed', axis=1)
y = df['delayed']

cols_to_encode = ['airline', 'origin', 'destination', 'weather']
X_encoded = pd.get_dummies(X, columns=cols_to_encode)

print(f"Colunas originais: {len(X.columns)}")
print(f"Colunas após codificação: {len(X_encoded.columns)}")

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, 
    y, 
    test_size=0.2,
    random_state=42, 
    stratify=y 
)

print(f"Tamanho do Treino: {X_train.shape}")
print(f"Tamanho do Teste: {X_test.shape}")

print("\nIniciando treinamento do XGBoost...")

model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

model.fit(X_train, y_train)

print("Treinamento concluído.")

print("\nAvaliando o modelo...")

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
relatorio = classification_report(y_test, y_pred)
matriz_confusao = confusion_matrix(y_test, y_pred)

print(f"\n--- Acurácia Final: {acc:.4f} ({acc*100:.2f}%) ---")

print("\n--- Relatório de Classificação ---")
print(relatorio)

print("\n--- Matriz de Confusão ---")
print(matriz_confusao)