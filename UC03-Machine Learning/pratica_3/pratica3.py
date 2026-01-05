import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from xgboost import XGBClassifier

print("1. Carregando e Preparando Dados...")
try:
    df = pd.read_csv('flights_delays_120.csv')
except FileNotFoundError:
    print("ERRO: Arquivo 'flights_delays_120.csv' não encontrado.")
    exit()

X = df.drop('delayed', axis=1)
y = df['delayed']

X_encoded = pd.get_dummies(X, columns=['airline', 'origin', 'destination', 'weather'])

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Dados de Treino/Validação: {X_train.shape}")
print(f"Dados de Teste Final: {X_test.shape}")

print("\n 2. Configurando Otimização de Hiperparâmetros...")
xgb = XGBClassifier(eval_metric='logloss')

param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1]
}

grid_search = GridSearchCV(
    estimator=xgb,
    param_grid=param_grid,
    scoring='accuracy',
    cv=3,
    verbose=1
)

print("\n3. Iniciando a busca pelo melhor modelo (Isso pode demorar um pouco)...")
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
print(f"\nMelhores Parâmetros encontrados: {best_params}")
print(f"Melhor Acurácia na Validação: {grid_search.best_score_:.4f}")

best_model = grid_search.best_estimator_

print("\n 4. Avaliação Final no Dataset de Teste...")

y_pred = best_model.predict(X_test)

print("\n--- Relatório de Métricas ---")
print(classification_report(y_test, y_pred))

print("--- Matriz de Confusão ---")
print(confusion_matrix(y_test, y_pred))

print("\n 5. Teste de Inferência com um 'Novo Voo'...")

novo_dado = X_test.iloc[0:1] 

previsao = best_model.predict(novo_dado)
probabilidade = best_model.predict_proba(novo_dado)

print(f"Dados do voo simulado:\n{novo_dado.index}")
print(f"Previsão do Modelo: {'Atraso' if previsao[0] == 1 else 'No Horário'}")
print(f"Probabilidade de Atraso: {probabilidade[0][1]*100:.2f}%")