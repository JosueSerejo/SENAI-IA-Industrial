import warnings, requests, zipfile, io
import pandas as pd
from scipy.io import arff

# Ignora avisos para deixar a saída mais limpa
warnings.simplefilter('ignore')

# URL do dataset compactado (UCI Machine Learning Repository)
f_zip = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00212/vertebral_column_data.zip'

# Download do arquivo ZIP
r = requests.get(f_zip, stream=True)

# Extração do conteúdo do arquivo ZIP
vertebral_zip = zipfile.ZipFile(io.BytesIO(r.content))
vertebral_zip.extractall(path='data/')

# Leitura do arquivo ARFF
data = arff.loadarff('data/column_2C_weka.arff')

# Criação do DataFrame a partir dos dados carregados
df = pd.DataFrame(data[0])

# Verificação da dimensão do DataFrame (linhas e colunas)
df.shape

# Visualização dos primeiros registros
df.head()
