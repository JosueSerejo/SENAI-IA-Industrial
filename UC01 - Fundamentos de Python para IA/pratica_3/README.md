# Monitoramento de Temperaturas com Análise Estatística

## 📌 Descrição do Projeto
Este projeto implementa um sistema de monitoramento de temperaturas utilizando Programação Orientada a Objetos (POO) em Python.  
O sistema registra leituras de temperatura, verifica se estão dentro de limites de segurança e calcula estatísticas utilizando a biblioteca NumPy.

A aplicação permite:

- Armazenar leituras de temperatura.
- Verificar automaticamente se as leituras estão dentro do intervalo seguro.
- Emitir alertas para valores fora do limite.
- Calcular estatísticas (máximo, mínimo e média).
- Configurar limites de segurança personalizados.

---

## 📚 Tecnologias Utilizadas
- **Python 3.x**
- **NumPy**

---

## 🧩 Estrutura do Sistema
A classe `TemperatureMonitor` contém:

- **Atributos**
  - Lista de temperaturas registradas
  - Limite inferior e superior de segurança

- **Métodos**
  - `add_reading()` – adiciona uma nova leitura
  - `is_within_safe_limits()` – verifica se está dentro dos limites
  - `calculate_statistics()` – usa NumPy para gerar estatísticas
  - `display_statistics()` – exibe o relatório final de monitoramento

---