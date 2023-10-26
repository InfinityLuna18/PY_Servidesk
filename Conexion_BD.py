import pyodbc

Driver = 'SQL server'
Server = 'DESKTOP-FRNPL1P\SQLEXPRESS'
bd = 'BDPrincipal'

usuario = ''
contrasenia = ''

try:
    conexion = pyodbc.connect('DRIVER='+Driver+'; SERVER='+Server+'; DATABASE='
                              +bd+';Uid=;PWD=;')
    #conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+'; DATABASE='
                              #+bd+';Uid = '+usuario+';PWD='+contrasenia)
    print('conexion exitosa')
    
except:
    print ('error al intentar conectarse.')