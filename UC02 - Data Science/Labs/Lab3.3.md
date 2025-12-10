### Observações – Laboratório 3.3

O conjunto de dados foi importado a partir do UCI Machine Learning Repository e carregado em um DataFrame do Pandas. O dataset contém informações técnicas e comerciais de automóveis, incluindo variáveis numéricas e categóricas, além da variável alvo `price`.

Inicialmente, foi realizada a remoção de registros sem valor de preço, pois essa variável é essencial para análises posteriores. Em seguida, foram identificados valores ausentes em variáveis numéricas e categóricas, sendo aplicada imputação por média para variáveis numéricas e por moda para variáveis categóricas.

### Estatísticas descritivas básicas

Foram analisadas estatísticas descritivas das variáveis numéricas do conjunto de dados, permitindo compreender medidas de tendência central, dispersão e amplitude. Essa análise auxiliou na identificação de padrões gerais e possíveis inconsistências nos dados antes da etapa de codificação das variáveis categóricas.

### Codificação de variáveis categóricas

Para preparar os dados para a etapa de modelagem, foram aplicadas técnicas de codificação em variáveis categóricas. A variável `num-of-cylinders`, de natureza ordinal, foi convertida para valores numéricos por meio de um mapeamento explícito.

As variáveis categóricas nominais foram transformadas utilizando One-Hot Encoding, pois não possuem ordem intrínseca. Essa abordagem evita a introdução de relações artificiais entre categorias e é adequada para algoritmos de Machine Learning baseados em distância ou regressão.

### Análise de correlação

A matriz de correlação foi calculada para avaliar a relação entre a variável alvo `price` e algumas das principais variáveis numéricas do conjunto de dados. O mapa de calor facilitou a visualização da intensidade e do sentido dessas correlações, auxiliando na identificação de atributos com maior potencial preditivo.