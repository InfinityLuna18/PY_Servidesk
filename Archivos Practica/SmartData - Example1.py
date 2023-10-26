#Librerías de visualización
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seabord as sns
import datetime as dt
import zipfile

#Librerías de MachineLearning
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

#Descomprimir Archivo:
with zipfile.ZipFile ('TransaccionesRetail.zip','r') as zip_ref:
    zip_ref.extractall('OutPut')

#Leer archivo Csv
df = pd.read_csv('/Archivos Practica/SmartData - Example1.py', sep=",",encoding="ISO-8859-1", header=0)
df.head()