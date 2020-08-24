import sqlite3

def crearBaseDatos():
   conexion = sqlite3.connect('car_rental.db')
   CursorRental = conexion.cursor()
   

   try:
      CursorRental.execute("""CREATE TABLE CLIENTE ("CUIT" INTEGER PRIMARY KEY,
                                                   "NOMBRE" VARCHAR(50),
                                                   "PASSWORD" INTEGER NOT NULL)""")
   except:
      None

   try:
      CursorRental.execute("""CREATE TABLE FACTURA ("ID" INTEGER PRIMARY KEY AUTOINCREMENT,
                                                     "CLIENTE" VARCHAR(50) NOT NULL,
                                                     "AUTO" VARCHAR(50) UNIQUE,
                                                     "TIPO" VARCHAR(4),
                                                     "CANTIDAD" INTEGER,
                                                     "PRECIO" INTEGER,
                                                     "FECHA" DATETIME)""")
   except:
      None
























































































































































