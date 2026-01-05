import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score, accuracy_score
from xgboost import XGBClassifier

df = pd.read_csv('flights_delays_120.csv')

X = df.drop('delayed', axis=1)
y = df['delayed']

X_encoded = pd.get_dummies(X, columns=['airline', 'origin', 'destination', 'weather'])

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42, stratify=y
)

model = XGBClassifier(eval_metric='logloss')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_proba = model.predict_proba(X_test)[:, 1]

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

tn, fp, fn, tp = cm.ravel()

print("\n--- Decomposição da Matriz ---")
print(f"Verdadeiros Negativos (TN): {tn} (Não atrasou e modelo acertou)")
print(f"Falsos Positivos (FP):      {fp} (Não atrasou, mas modelo disse que ia)")
print(f"Falsos Negativos (FN):      {fn} (Atrasou, mas modelo disse que não ia)")
print(f"Verdadeiros Positivos (TP): {tp} (Atrasou e modelo acertou)")

sensibilidade = tp / (tp + fn) 
especificidade = tn / (tn + fp)
fpr = fp / (tn + fp)      
fnr = fn / (tp + fn) 
acuracia = (tp + tn) / (tp + tn + fp + fn)

print("\n--- Métricas de Desempenho ---")
print(f"Acurácia:        {acuracia:.4f}")
print(f"Sensibilidade:   {sensibilidade:.4f} (Capacidade de detectar atrasos)")
print(f"Especificidade:  {especificidade:.4f} (Capacidade de ignorar voos pontuais)")
print(f"Taxa Falso Pos.: {fpr:.4f}")
print(f"Taxa Falso Neg.: {fnr:.4f}")

auc_score = roc_auc_score(y_test, y_proba)
print(f"\nAUC Score:       {auc_score:.4f}")

fpr_curve, tpr_curve, thresholds = roc_curve(y_test, y_proba)

plt.figure(figsize=(6, 5))
plt.plot(fpr_curve, tpr_curve, label=f'XGBoost (AUC = {auc_score:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Aleatório (50%)') # Linha base
plt.xlabel('Taxa de Falsos Positivos (FPR)')
plt.ylabel('Taxa de Verdadeiros Positivos (TPR - Recall)')
plt.title('Curva ROC')
plt.legend()
plt.grid()
plt.show()