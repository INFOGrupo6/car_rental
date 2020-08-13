
# Sistema de renta de vehiculos 

class carRental: 

      def __init__(self):
         self.verde = '\33[32m'
         self.rojo = '\33[31m'
         self.amarillo = '\33[33m'
         self.reset = '\u001b[0m' 
         self.lista = []

      def ejecutar(self):    
       ingreso = True  
       while(ingreso):   
              print("\nBienvenido a la renta de Autos")
              print("\nLas opciones son:\n 1- Alquilar auto \n 2- Mostrar autos rentados \n 3- Editar Autos\
                 \n 4- Confirmar alquiler \n 5- Salir del sistema ")
              try:
                 self.opcion = int(input("\nDigite la operacion que desea realizar: ")) 
              except ValueError:
                 print(self.rojo+"\n::::: Error, ingrese solo numeros enteros :::::"+self.reset)
                 continue
  
              if (self.opcion == 5):
                   print(self.amarillo+"\nAdios ! ha salido del sistema de renta de autos"+self.reset) 
                   break
    
              if (self.opcion == 1):
                   self.Alquilar()    
              if (self.opcion == 2):
                   self.mostrarAutos()    
              if (self.opcion == 3):
                   self.editarAutos()     
              if (self.opcion == 4):
                   self.confirmarAlquiler()     

# Metodo para alquilar autos                    
      def Alquilar(self):
                 print("")
                 try: 
                      print("\nIngrese 1 para alquilar por dia, 2 por hora y 3 por km")
                      opc = int(input("Quiere alquilar por dia , por hora o km ? ")) 
                      if (opc == 1):
                         self.cuit = int(input("Introduzca el CUIT: ")) 
                         self.dias = int(input("Introduzca los dias a alquilar el vehiculo: "))
                         self.lista.append(str(self.cuit)+ " CUIT")  
                         self.lista.append(str(self.dias)+ " dias")  
                      elif (opc == 2):
                         self.cuit = int(input("Introduzca el CUIT: ")) 
                         self.horas = int(input("Introduzca las horas a alquilar el vehiculo: ")) 
                         self.lista.append(str(self.cuit)+ " CUIT")  
                         self.lista.append(str(self.horas) + " horas")  
                      elif (opc == 3):
                         self.cuit = int(input("Introduzca el CUIT: ")) 
                         self.km = int(input("Introduzca los km de recorrido del vehiculo: ")) 
                         self.lista.append(str(self.cuit)+ " CUIT")  
                         self.lista.append(str(self.km) + " kilometros")  
                 except ValueError:
                     print(self.rojo+"error, ingrese solo numeros"+self.reset)   

# Metodo para mostrar autos alquilados en lista 
      def mostrarAutos(self):
                 print(self.amarillo+"\n&&&___ Lista de Autos rentados ___&&&"+self.reset)
                 print(self.amarillo+"--------------------------"+self.reset)
                 cont = 0
                 for i in self.lista:
                      cont += 1 
                      print(i) 
                      # Multiplos de 3 ponen barra 
                      if (cont % 2 == 0):
                          print(self.amarillo+"--------------------------"+self.reset)   
# editar seleccion                           
      def editarAutos(self):
                print(self.lista)
                print("\nQue alquiler de auto desea borrar ?")
                print("EJEMPLO 123 CUIT :")
                borrarCUIT = input("Ingrese su numero de CUIT espacio y la palabra CUIT como se muestra para borrar: ") 

                if (borrarCUIT in self.lista):
                    self.lista.remove(self.cuit)       
                    self.lista.remove(self.horas)       
                    self.lista.remove(self.km)       
                    self.lista.remove(self.dias)       
                    print(self.amarillo+"\n### Alquiler borrado exitosamente ###"+self.reset)
                if (borrarCUIT not in self.lista): 
                    print(self.rojo+"\n||||___Datos no encontrados, ingreselos nuevamente__||||"+self.reset)   
                
            
# Confirmar seleccion 
      def confirmarAlquiler(self):
              print(self.amarillo+"Su alquiler se ha confirmado exitosamente"+self.reset)
              exit()                     

renta = carRental()
renta.ejecutar()
























































































































































































































































































































































