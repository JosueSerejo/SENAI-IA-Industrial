import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

data = {
    'idade': [22, 25, 47, 52, 46, 56, 55, 60, 62, 70],
    'tempo_cadastro': [1, 2, 5, 10, 7, 12, 11, 15, 20, 25],
    'email_aberto': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    'clicou_no_link': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    'comprou': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print("Dados carregados com sucesso:")
print(df)

X = df[['idade', 'tempo_cadastro', 'email_aberto', 'clicou_no_link']]
y = df['comprou']

print("\n Variáveis independentes (X):")
print(X.head())
print("\n Variável dependente (y):")
print(y.head())

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"\n  número de amostras de treino: {len(X_treino)}")
print(f"  número de amostras de teste: {len(X_teste)}")

modelo_dt = DecisionTreeClassifier(random_state=42)
modelo_dt.fit(X_treino, y_treino)

print("\n Modelo treinado com sucesso.")

previsoes = modelo_dt.predict(X_teste)

print("\n Previsões realizadas:")
print(previsoes)

acuracia = accuracy_score(y_teste, previsoes)
relatorio = classification_report(y_teste, previsoes)
print("\n Relatório de Avaliação do modelo:")
print(f"\n Acurácia do modelo: {acuracia:.2f}")

print("\n Relatório de Classificação:")
print(relatorio)