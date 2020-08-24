from tkinter import *
from tkinter import messagebox
from BaseDatos import *
import time
crearBaseDatos()

"""Una empresa de alquiler de autos ofrece distintas modalidades de alquiler:
* Por hora: el cliente debe pagar por cada hora que alquila el auto. El costo es de $ 100 / hora.
* Por día: el cliente paga un monto fijo por día (el día son 24 horas) no importa si el auto se devuelve antes. La cantidad de días debe definir al momento del alquiler.
 El costo es de $ 2000 / día
* Por kilometraje: el cliente paga un precio fijo por cada kilómetros recorrido durante el período de alquiler. Este tipo de alquiler implica
 devolución dentro del mismo día de alquiler. El costo $ 100 de base más $ 10/km.

Al mismo tiempo hay una serie de reglas de facturación:
* Los días miércoles todos los alquileres tienen una bonificación de 50 pesos.
* Si quien alquila es una empresa (cuit empieza con 26) tiene un descuento del 5% como parte de la política de fidelización de clientes
* Si el auto es devuelto luego de finalizado el tiempo establecido al momento de alquiler, se cobra un recargo del 100%.
>> Hacer un programa que permita calcular la correspondiente facturación para los alquileres, debes diseñar las clases que consideres adecuadas con los datos convenientes."""

class cliente():
    def __init__(self,cuit,password,nombre):
        self.cuit = cuit
        self.nombre = nombre
        self.password = password

    """def agregarCliente(self):
        try:
            conexion = sqlite3.connect('car_rental.db')
            CursorRental = conexion.cursor()
            usuario = [(int(self.cuit), self.nombre, int(self.password))]
            CursorRental.executemany("INSERT INTO CLIENTE VALUES(?,?,?)", usuario)
            #CursorRental.executemany("INSERT INTO FACTURA VALUES(NULL,?,NULL,NULL,NULL,NULL)", usuario)
            messagebox.showinfo("Listo!","Cuenta creada con exito!...\n")
            conexion.commit()
        except:
            messagebox.showwarning("Hola","Bienvenido nuevamente! ")"""


class alquilerAuto(cliente):
    def __init__(self,cuit,password,nombre,auto,tipo,cantidad):
        cliente.__init__(self,cuit,password,nombre)
        self.auto = auto
        self.tipo = tipo
        self.cantidad = cantidad

    def agregarCliente(self):
        try:
            conexion = sqlite3.connect('car_rental.db')
            CursorRental = conexion.cursor()
            usuario = [(int(self.cuit), self.nombre, int(self.password))]
            CursorRental.executemany("INSERT INTO CLIENTE VALUES(?,?,?)", usuario)
            messagebox.showinfo("Listo!","Cuenta creada con exito!...\n")
            conexion.commit()
        except:
            messagebox.showwarning("Hola","Bienvenido nuevamente! ")

    def factura(self):
        try:
            conexion = sqlite3.connect('car_rental.db')
            CursorRental = conexion.cursor()
            times = time.strftime('%Y-%m-%d %H:%M')
            factura = [(int(self.cuit),self.auto, self.tipo, int(self.cantidad),0,times)]
            CursorRental.executemany("INSERT INTO FACTURA VALUES(NULL,?,?,?,?,?,?)", factura)
            messagebox.showinfo("Listo!","Alquiler creado con exito!...\n")
            messagebox.showinfo("yeah!","Su factura estará siendo procesada!...\n")
            conexion.commit()
        except:
            messagebox.showwarning("Upss..","Este auto ya esta alquilado! ")


autos = {
    "ID1":"PEUGEOT 206",
        "Caracteristica1":{"Modelo":"2010", "Color":"Gris","Patente":"KAJ-154","Puertas":2},

    "ID2":"TOYOTA COROLLA",
        "Caracteristica2":{"Modelo":"2015","Color":"Blanco","Patente":"KHE-744","Puertas":4},

    "ID3":"RENAULT 12", 
        "Caracteristica3":{"Modelo":"2001","Color":"Rojo","Patente":"ABJ-994","Puertas":4},

    "ID4":"FIAT 600",
        "Caracteristica4":{"Modelo":"1995","Color":"Blanco","Patente":"ASD-123","Puertas":2},

    "ID5":"AUDI TT",
        "Caracteristica5":{ "Modelo":"2017","Color":"Negro","Patente":"BAT-222","Puertas":2}
}



