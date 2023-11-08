from Archivos_Practica.ConexionBD import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import zipfile

#Dimensionamiento de datos
df_tabla.shape

#Vista general de los datos
df_tabla.info()

#Estadística descriptiva
df_tabla.describe()
#mean --> media
#std --> desviación
#cuando la mean < std, existe una probabilidad que NO haya valores atípicos
#cuando la mean > std, existe una probabilidad que SI haya valores atípicos

#--------------------------------------------------------------------------------------
#LIMPIEZA DE DATOS

#Revisión de valores faltantes o vacíos --> se muestra en porcentaje
round(100*(df_tabla.isnull().sum())/len(df_tabla),2)

#Si se encuetran valores vacíos, se deben eliminar
df_tabla = df_tabla.dropna()

df_tabla.shape

#Cambiar el código de la llave principal de float a texto
#df_tabla ['nTBLServideskID'] = df_tabla['nTBLServideskID'].astype(str)


#--------------------------------------------------------------------------------------
#PREPARACIÓN DE LA DATA
df_rfm_f1 = df_tabla.groupby('Usuario_Solicitante')['Usuario_Solicitante'].count()
df_rfm_f1 = df_rfm_f1.reset_index()
df_rfm_f1.columns = ['cUsuario_Solicitante','']

df = pd.DataFrame({'Usuario_Solicitante': df_tabla.loc[:,'Usuario_Solicitante']
                   ,'TiempoDias': df_tabla.loc[:,'TiempoDias']
                   #,'Cantidad_Casos' : df_tabla.groupby(['Usuario_Solicitante']).count()
                   })
df

df.groupby(['Usuario_Solicitante']).count()
df.groupby(by = ['Usuario_Solicitante','TiempoDias']).count()

df.groupby(by = ['Usuario_Solicitante','TiempoDias']).value_counts()

df2 = pd.DataFrame(df.groupby(by = ['Usuario_Solicitante','TiempoDias']).value_counts())
df2

df3 = pd.DataFrame(df2, index=df2['TiempoDias'])

df2.head()

df2.index

plt.bar(df2['Usuario_Solicitante'], df['count'])
plt.bar(df2.index, df2['count'])
plt.bar(x = df2['Usuario_Solicitante'] , height = df2['count'])

colum1 = df_tabla['Usuario_Solicitante']
colum2 = df_tabla['TiempoDias']

datos = {'USUARIOS': colum1, 'TipoTiempo': colum2}


datos_fin = pd.DataFrame(data=datos)
d = pd.DataFrame(datos_fin.groupby(['USUARIOS','TipoTiempo']).size().reset_index(name='contador'))
d
plt.bar(d['USUARIOS'], d['contador'])
plt.show()

d['USUARIOS'][2:4]
df_new = d[['USUARIOS','contador']] [:3]
df_new

plt.bar(df_new['USUARIOS'], df_new['contador'])
plt.show()

df_new = d[['TipoTiempo','contador']] #[:3]
df_new

plt.bar(df_new['TipoTiempo'], df_new['contador'])
plt.show()

plt.bar(d.index, d['TipoTiempo'])
plt.bar(d['contador'], d['TipoTiempo'])
plt.show()

#ANÁLISIS RFM
#R (RECENCY) -->
#F (FRECUENCIA) -->
#M (MONETARIO)

