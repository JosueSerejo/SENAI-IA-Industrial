import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import joblib
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

print("Iniciando Treinamento...")

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

model = XGBClassifier(eval_metric='logloss')
model.fit(X_train, y_train)

artifacts = {
    'model': model,
    'features': X_encoded.columns.tolist()
}
joblib.dump(artifacts, 'modelo_voos_final.pkl')
print("Modelo salvo em 'modelo_voos_final.pkl'. Implantação concluída!")

print("\n 2. Carregando o modelo do disco para uso...")

loaded_artifacts = joblib.load('modelo_voos_final.pkl')
loaded_model = loaded_artifacts['model']
model_features = loaded_artifacts['features']

def preparar_dados_novos(df_novo, colunas_modelo):
    df_enc = pd.get_dummies(df_novo, columns=['airline', 'origin', 'destination', 'weather'])
    df_enc = df_enc.reindex(columns=colunas_modelo, fill_value=0)
    return df_enc

print("\n--- A. Teste em Tempo Real (1 Passageiro) ---")

novo_passageiro = {
    'airline': 'JetCloud',
    'origin': 'GRU',
    'destination': 'MIA',
    'departure_hour': 14,
    'day_of_week': 5,
    'weather': 'Rain'
}

df_realtime = pd.DataFrame([novo_passageiro])
X_realtime = preparar_dados_novos(df_realtime, model_features)

pred_classe = loaded_model.predict(X_realtime)[0]
pred_prob = loaded_model.predict_proba(X_realtime)[0][1]

print(f"Passageiro: {novo_passageiro['airline']} saindo de {novo_passageiro['origin']}")
print(f"Previsão: {'Atraso Confirmado' if pred_classe == 1 else 'No Horário'}")
print(f"Risco de Atraso: {pred_prob*100:.2f}%")

print("\n--- B. Teste em Lote (Batch Transform) ---")

df_lote = pd.read_csv('flights_delays_120.csv')
X_lote = df_lote.drop('delayed', axis=1, errors='ignore')

X_lote_pronto = preparar_dados_novos(X_lote, model_features)

preds_lote = loaded_model.predict(X_lote_pronto)
probs_lote = loaded_model.predict_proba(X_lote_pronto)[:, 1]

df_resultado = X_lote.copy()
df_resultado['PREVISAO_ATRASO'] = preds_lote
df_resultado['PROBABILIDADE'] = probs_lote

df_resultado.to_csv('resultado_batch.csv', index=False)
print("Processamento em lote finalizado.")
print("Arquivo 'resultado_batch.csv' gerado com sucesso!")
print("\nExemplo das primeiras linhas processadas:")
print(df_resultado[['airline', 'origin', 'PREVISAO_ATRASO', 'PROBABILIDADE']].head())