### Observações – Laboratório 3.2

O conjunto de dados foi importado a partir do UCI Machine Learning Repository e carregado em um DataFrame do Pandas. A inspeção inicial permitiu identificar a estrutura geral da base, incluindo o número de atributos, seus tipos e a presença da variável alvo `class`.

Nesta etapa, o foco foi realizar uma análise exploratória detalhada, utilizando estatísticas descritivas e visualizações gráficas, com o objetivo de compreender o comportamento das variáveis e identificar padrões relevantes, sem aplicar ainda tratamentos definitivos no conjunto de dados.

### Classificação das variáveis e tipos de dados

A análise da estrutura do DataFrame mostrou que a maior parte das variáveis possui tipo numérico, representando medições contínuas da coluna vertebral. A variável `class` é categórica e representa o rótulo de classificação das instâncias.

Essa separação entre variáveis numéricas e categóricas é essencial para a preparação dos dados, pois define as técnicas de tratamento e codificação que deverão ser aplicadas nas próximas etapas do pipeline de Machine Learning.

### Análise de valores ausentes

A verificação de valores ausentes foi realizada por meio da contagem de valores nulos em cada coluna. A análise indicou que o conjunto de dados não apresenta valores ausentes, não sendo necessária a aplicação de técnicas de remoção ou imputação nesta etapa.

### Estatísticas descritivas

Foram calculadas estatísticas descritivas básicas para as variáveis numéricas, incluindo média, desvio padrão, valores mínimo e máximo. Essas métricas permitem compreender a dispersão e a tendência central dos dados, auxiliando na identificação de possíveis outliers e padrões relevantes.

### Visualização e análise exploratória dos dados

Diversos gráficos exploratórios foram utilizados, como gráficos de linha, densidade, histogramas, boxplots e gráficos de dispersão. Essas visualizações permitiram analisar a distribuição das variáveis, comparar comportamentos entre classes e identificar possíveis relações entre os atributos.

A análise de correlação, complementada por um heatmap, possibilitou visualizar a intensidade das relações entre as variáveis numéricas e a variável alvo, auxiliando na identificação de atributos potencialmente relevantes para a modelagem.