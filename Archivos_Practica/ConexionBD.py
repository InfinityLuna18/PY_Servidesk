#Conexión a la base de datos:
#def ConexionBD():
    
#Paso n°01: importar librería
import pyodbc
import pandas as pd


#Paso n°02: declarar las variables a utilizar para la conexión:
Driver = '{SQL Server}' 
Driver2 = '{ODBC Driver 18 for SQL Server}' #OTRO: {ODBC Driver 17 for SQL Server}
IP_Servidor = '192.168.18.4' #'DESKTOP-FRNPL1P\SQLEXPRESS'
BaseDatos = 'BDPrincipal'
nombre_usuario = ''
contraseña = ''

#Paso n°03: Realizar el proceso de conexión
try:
    conexion = pyodbc.connect('DRIVER='+Driver+'; SERVER=' +IP_Servidor+'; DATABASE='
                              +BaseDatos+#';Uid=;PWD=;Trusted_Connection=yes;')
                              #'UID = ' + nombre_usuario +
                              #'PWD = ' + contraseña
                              ';Uid=;PWD=;')
    cursor = conexion.cursor()
    
    query_tabla = 'SELECT * FROM TBL_Servidesk'
    
    df_tabla = pd.read_sql_query(query_tabla,conexion)
    
    #df_tabla.info()

    cursor.close()
   # data = pd.read_sql('SELECT TOP(100) * FROM TB_Servidesk', cursor)
except Exception as error:
    print('Ocurrió un error al conectar a SQL Server: ', error)

#if __name__ == '__main__':
#   ConexionBD()
