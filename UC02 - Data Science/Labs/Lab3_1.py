import warnings, requests, zipfile, io
import pandas as pd
from scipy.io import arff

warnings.simplefilter('ignore')

f_zip = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00212/vertebral_column_data.zip'

r = requests.get(f_zip, stream=True)

vertebral_zip = zipfile.ZipFile(io.BytesIO(r.content))
vertebral_zip.extractall(path='data/')

data = arff.loadarff('data/column_2C_weka.arff')

df = pd.DataFrame(data[0])

print(df.head())