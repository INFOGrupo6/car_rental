import mysql.connector   # Importamos la libreria 

verde = '\33[32m'
rojo = '\33[31m'
amarillo = '\33[33m'
reset = '\u001b[0m' 

#-- Probar coneccion a DB con funcion connect --
def testConnect():
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="password"
    )
   print("\nConexion exitosa")
   print(mydb)
   mydb.close() 

# Test de conexion a DB , imprime el objeto de la conexion y el mensaje si hay exito 
testConnect() 


#-- Funcion para crear la base de datos -- 
def CreateDB():
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="15256010"
    )
   cursor = mydb.cursor()
   cursor.execute("CREATE DATABASE IF NOT EXISTS testDB") 
   cursor.execute("SHOW DATABASES")
   print("\nCrear db exitosa")
   for x in cursor:
       print(x)
   mydb.close() 

CreateDB() 


#-- Crear tabla de base de datos --
def CreateTable():
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="15256010"
    )
   cursor = mydb.cursor()
   try:  
     cursor.execute("CREATE TABLE `testDB`.`tableTestDB`(\
     `ID_CUIT` VARCHAR(10) NOT NULL,\
     `DIAS` VARCHAR(45) NULL,\
     `HORAS` VARCHAR(45) NULL,\
     `KILOMETROS` VARCHAR(45) NULL,\
     PRIMARY KEY (`ID_CUIT`))")
     print("\nCrear tabla exitosa")
   except:
     print("\nHubo un error, probablemente la tabla ya existe")  
   mydb.close() 

CreateTable() 


#-- Insertar datos a tabla --
def insert(cuit,dias,horas,km):
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="15256010"
    )
   cursor = mydb.cursor()
   try: 
      sql = ("INSERT INTO `testDB`.`tableTestDB` (`ID_CUIT`, `dias`, `horas`,`kilometros`)\
      VALUES (%s,%s,%s,%s)") 
      val = (cuit,dias,horas,km)
      cursor.execute(sql,val) 
      print("\nInsercion de datos exitosa")
   except:
      print("Error al insertar datos")

   # El commit se usa para subir los cambios a la DB     
   mydb.commit()   
   mydb.close() 

insert()


#-- Borrar datos a tabla especificos --
def delete(cuit):
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="15256010"
    )  
   cursor = mydb.cursor()

   sql2 = ('SELECT * FROM testDB.tableTestDB WHERE ID_CUIT = %s')
   val1 = (cuit,)
   cursor.execute(sql2,val1) 
   myresult = cursor.fetchall()   
   #cursor.reset() 
   try: 
     if (cuit == myresult[0][0]): 
       sql = ("DELETE FROM `testDB`.`tableTestDB` WHERE `ID_CUIT` = %s") 
       val = (cuit,)
       cursor.execute(sql,val)
       print(verde+"\nborrado exitoso"+reset)
   except:
       print(rojo+"\nNo hay ese cuit"+reset)    

   # El commit se usa para subir los cambios a la DB     
   mydb.commit()   
   mydb.close() 

delete()


#-- Borrar datos a tabla Todos los datos--
def deleteALL():
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="15256010"
    )
   cursor = mydb.cursor()
   try: 
      sql = ("DELETE FROM testDB.tableTestDB") 
      cursor.execute(sql) 
      print("\nDelete de todos los datos exitoso")
   except:
      print("Error en delete")

   # El commit se usa para subir los cambios a la DB     
   mydb.commit()   
   mydb.close() 

deleteALL()



#-- Actualizar datos de tabla --
def update(cuit):
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="15256010"
    )
   cursor = mydb.cursor()

   sql2 = ('SELECT * FROM testDB.tableTestDB WHERE ID_CUIT = %s')
   val1 = (cuit,)
   cursor.execute(sql2,val1) 
   myresult = cursor.fetchall()  
   try: 
      if (cuit == myresult[0][0]): 
        print(verde+"El cuit existe"+reset)
        print(myresult) 
        val = input("\nIngrese el cuit nuevo: ")
        sql = (f"UPDATE `testDB`.`tableTestDB` SET `id_cuit` = {val} WHERE ID_CUIT = %s") 
        cursor.execute(sql,val1) 
        print(verde+"\nUpdate exitoso"+reset)
   except:
      print(rojo+"\nError en update"+reset)

   # El commit se usa para subir los cambios a la DB     
   mydb.commit()   
   mydb.close() 

update()


#-- Obtener datos de la tabla especificos por cuit todos los datos -- 
def select(cuit):
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="15256010"
    )
   cursor = mydb.cursor()
   
   #sql = ("SELECT *, id_cuit = %s FROM tableTestDB")
    
   sql = ('SELECT * FROM testDB.tableTestDB WHERE ID_CUIT = %s')
   val = (cuit,)
   cursor.execute(sql,val) 
   myresult = cursor.fetchall()
   
   
   #print(myresult[0][0])
   #print(type(myresult[0]))
   try: 
     if (cuit == myresult[0][0]): 
        print(verde+"\nSelect exitoso"+reset)
        print(amarillo+"&&&___ Busqueda de CUIT ___&&&"+reset)
        print(amarillo+"--------------------------"+reset)
        cont = 0
        for x in myresult:
           cont += 1
           print(x)
           # Multiplos de 3 ponen barra 
           if (cont % 4 == 0):
               print(amarillo+"--------------------------"+reset) 
   except:       
        print(rojo+"\n##__cuit no encontrado__##"+reset)  

   # El commit se usa para subir los cambios a la DB     
   mydb.commit()   
   mydb.close()

select()



#-- Obtener datos de toda la tabla completa -- 
def selectALL():
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="15256010"
    )
   cursor = mydb.cursor()
   
   #sql = ("SELECT *, id_cuit = %s FROM tableTestDB")
    
   sql = ('SELECT * FROM testDB.tableTestDB')
   cursor.execute(sql) 
   myresult = cursor.fetchall()
   print("\nSelect exitoso\n")
   print(amarillo+"\n&&&___ Lista de Autos rentados ___&&&"+reset)
   print(amarillo+"--------------------------"+reset)
   cont = 0
   for x in myresult:
      cont += 1
      print(x)
      # Multiplos de 3 ponen barra 
      if (cont % 1 == 0):
          print(amarillo+"--------------------------"+reset) 
      
   # El commit se usa para subir los cambios a la DB     
   mydb.commit()   
   mydb.close()

selectALL()






































































































































































