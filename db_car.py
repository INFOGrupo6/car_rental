## Base de datos de car rental 
import mysql.connector  # mysql-connector-python 
from mysql.connector import errorcode

## BD CAR_RENTAL 
## TABLA   CUIT  DIAS  HORAS  KM 
#          123                1000 
#          333    2 
#          120          10   

def connect():
    '''Creación de la Base de datos'''

    mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="islaNDZfidji85")

    cursor = mydb.cursor()

    print("Conexion exitosa\n")
    print(mydb)

    try:
        cursor.execute()
        print('La Base fue creada con éxito')
    except mysql.connector.Error as err:
       if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
       elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
       else:
         print(err)
    else:
       mydb.close() 

def create_db():
    '''Creación de la Base de datos'''

    mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="islaNDZfidji85")

    cursor = mydb.cursor()

    print("Conexion exitosa\n")
    print(mydb)

    sql = 'CREATE TABLE IF NOT EXISTS Alquiler(id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, CUIT VARCHAR(20) NOT NULL, dias VARCHAR(14) NOT NULL, horas VARCHAR(20) NOT NULL, kilometros VARCHAR(20) NOT NULL)'

    try:
        cursor.execute("CREATE DATABASE CAR_RENTAL")
        cursor.excute(sql) 
        print('La Base fue creada con éxito')
    except mysql.connector.Error as err:
       if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
       elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
       else:
         print(err)
    else:
       mydb.close() 








































































































































































































































