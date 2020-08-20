from testDB2 import *
# Prueba de renta de autos con DB


class carRental: 
      
      def __init__(self):
         self.verde = '\33[32m'
         self.rojo = '\33[31m'
         self.amarillo = '\33[33m'
         self.reset = '\u001b[0m' 
         self.km = ""
         self.horas = ""
         self.dias = ""
         self.lista = []
      
      def ejecutar(self):    
       ingreso = True  
       while(ingreso):   
              print("\nBienvenido a la renta de Autos")
              print("\nLas opciones son:\n 1- Alquilar auto \n 2- Mostrar autos rentados \n 3- Buscar Autos\
                 \n 4- Borrar Autos  \n 5- Actualizar cuit \n 6- Confirmar alquiler \n 7- Salir del sistema ")
              try:
                 self.opcion = int(input("\nDigite la operacion que desea realizar: ")) 
              except ValueError:
                 print(self.rojo+"\n::::: Error, ingrese solo numeros enteros :::::"+self.reset)
                 continue
  
              if (self.opcion == 7):
                   print(self.amarillo+"\nAdios ! ha salido del sistema de renta de autos"+self.reset) 
                   break
    
              if (self.opcion == 1):
                   self.Alquilar()    
              if (self.opcion == 2):
                   self.mostrarAutos()    
              if (self.opcion == 3):
                   self.buscarAutos()    
              if (self.opcion == 4):
                   self.editarAutos()     
              if (self.opcion == 5):
                   self.Actualizar()     
              if (self.opcion == 6):
                   self.confirmarAlquiler()     

# Metodo para alquilar autos                    
      def Alquilar(self):
                 print("")
                 try: 
                      print("\nIngrese 1 para alquilar por dia, 2 por hora y 3 por km")
                      opc = int(input("Quiere alquilar por dia , por hora o km ? ")) 
                      if (opc == 1):
                         self.cuit = input("Introduzca el CUIT: ")
                         self.dias = input("Introduzca los dias a alquilar el vehiculo: ")
                         self.dias = (self.dias +" dias")
                         insert(self.cuit,self.dias,None,None)
                         print(self.verde+"\nAlquiler añadido exitosamente"+self.reset) 
                      elif (opc == 2):
                         self.cuit = input("Introduzca el CUIT: ")
                         self.horas = input("Introduzca las horas a alquilar el vehiculo: ")
                         self.horas = (self.horas + " horas")  
                         insert(self.cuit,None,self.horas,None)
                         print(self.verde+"\nAlquiler añadido exitosamente"+self.reset)  
                      elif (opc == 3):
                         self.cuit = input("Introduzca el CUIT: ")
                         self.km = input("Introduzca los km de recorrido del vehiculo: ") 
                         self.km = (self.km + " kilometros") 
                         insert(self.cuit,None,None,self.km)
                         print(self.verde+"\nAlquiler añadido exitosamente"+self.reset) 
                 except ValueError:
                     print(self.rojo+"error, ingrese solo numeros"+self.reset)   

# Metodo para mostrar autos alquilados en lista 
      def mostrarAutos(self):
            selectALL()
                             
# editar seleccion                           
      def editarAutos(self):
           print("\nEstos son todos los autos alquilados")
           selectALL()
           print("\nQue alquiler de auto desea borrar ?")
           borrarCUIT = input("Ingrese su numero de CUIT para borrar: ") 
           delete(borrarCUIT) 
          

# Buscar un cuit especifico 
      def buscarAutos(self):
           print("\nBienvenido a la herramienta de busqueda")
           buscarCUIT = input("Ingrese el numero de CUIT para buscar: ") 
           select(buscarCUIT) 
           
# Actualizar un cuit especifico 
      def Actualizar(self):
           print("\nBienvenido a la herramienta de actualizacion")
           updateCUIT = input("Ingrese el numero de CUIT que desea buscar: ") 
           update(updateCUIT) 
  
      
# Confirmar seleccion 
      def confirmarAlquiler(self):
              print(self.amarillo+"Su alquiler se ha confirmado exitosamente"+self.reset)
              exit()                     

renta = carRental()
renta.ejecutar()




