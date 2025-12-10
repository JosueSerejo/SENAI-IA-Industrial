import warnings, requests, zipfile, io
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import arff
import seaborn as sns

f_zip = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00212/vertebral_column_data.zip'

r = requests.get(f_zip, stream=True)

vertebral_zip = zipfile.ZipFile(io.BytesIO(r.content)) 
vertebral_zip.extractall(path='data/')

data = arff.loadarff('data/column_2C_weka.arff')

df = pd.DataFrame(data[0])

df.shape

df.columns

df.dtypes

df['pelvic_incidence'].describe()

df.plot(kind='line')

plt.show()

df.plot(kind="density", subplots=True, layout=(4, 2), figsize= (12, 12), sharex=False)
plt.show()

df['degree_spondylolisthesis'].plot.density()

plt.show()

df['degree_spondylolisthesis'].plot.hist()

plt.show()

df['degree_spondylolisthesis'].plot.box()

plt.show()

df['class'].value_counts()

class_mapper = {b'Abnormal': 1, b'Normal': 0}

df['class'] = df['class'].map(class_mapper).astype(int)

df.plot.scatter(y='degree_spondylolisthesis', x='class')

df.groupby('class').boxplot(fontsize=20, rot=90, figsize=(10, 10), patch_artist=True)
plt.show() 

corr_matrix = df.corr(numeric_only=True)
corr_matrix["class"].sort_values(ascending=False)

pd.plotting.scatter_matrix(df, figsize=(12, 12))

plt.show()

plt.figure(figsize=(10, 10)) 
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True, fmt='.2f')

plt.show()