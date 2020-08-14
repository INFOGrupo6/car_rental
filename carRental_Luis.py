
# Sistema de renta de vehiculos 
print("\nBienvenido a la renta de Autos!")
class carRental: 
      def __init__(self):
         self.lista = []
      
      def ejecutar(self):    
       ingreso = True  
       while(ingreso):   
              print("\nQue desea hacer?")
              print("Las opciones son:\n1- Alquilar un auto \n2- Mostrar autos rentados \n3- Editar Autos \n4- Confirmar alquiler \n5- Salir del sistema")
              try:
                 self.opcion = int(input("\nDigite la operacion que desea realizar: ")) 
              except ValueError:
                 print("\n::::: Error, ingrese solo numeros enteros :::::")
                 continue
  
              if (self.opcion == 5):
                   print("\nAdios! ha salido del sistema de renta de autos") 
                   break
              elif (self.opcion == 1):
                   self.Alquilar()    
              elif (self.opcion == 2):
                   self.mostrarAutos()    
              elif (self.opcion == 3):
                   self.editarAutos()     
              elif (self.opcion == 4):
                   self.confirmarAlquiler()     

# Metodo para alquilar autos                    
      def Alquilar(self):
                 try: 
                      print("\nIngrese | *1 -- alquilar por dia* | *2 -- por hora* | *3 -- por km*")
                      opc = int(input("Quiere alquilar por dia , por hora o km ?: ")) 
                      if (opc == 1):
                         self.cuit = int(input("Introduzca el CUIT: ")) 
                         self.dias = int(input("Introduzca los dias a alquilar el vehiculo: "))
                         self.lista.append(self.cuit)  
                         self.lista.append(self.dias)  
                      elif (opc == 2):
                         self.cuit = int(input("Introduzca el CUIT: ")) 
                         self.horas = int(input("Introduzca las horas a alquilar el vehiculo: ")) 
                         self.lista.append(self.cuit)  
                         self.lista.append(self.horas)  
                      elif (opc == 3):
                         self.cuit = int(input("Introduzca el CUIT: ")) 
                         self.km = int(input("Introduzca los km que va a recorrer con el vehiculo: ")) 
                         self.lista.append(self.cuit)  
                         self.lista.append(self.km)  
                 except ValueError:
                     print("ERROR!, ingrese solo numeros!")   
# Metodo para mostrar autos alquilados en lista 
      def mostrarAutos(self):
                 print("\n***___ Lista de Autos rentados ___***")
                 print("--------------------------")
                 cont = 0 #primer vuelta:1 /2da:2 /3ra:3
                 for i in self.lista:
                      cont += 1 
                      # Multiplos de 2 ponen barra 
                      if (cont % 2 == 0): #1era:1%2=0.2 /2da:2%2=3 /3era:2%3=0.66~
                          print("Cantidad de: " + str(i))
                          print("--------------------------")   
                      else:
                         print("El cuit es: " + str(i)) #1er:39310 /2da:horas-dias-km /3ra:otro cuit.
# editar seleccion                           
      def editarAutos(self):
                num = 0
                opc = 1
                print("\nBORRADO DE ALQUILERES!")
                for i in self.lista:
                     if (num % 2 == 0):
                        print("____________\nBorrar Opc:N°"+str(opc))
                        print("El cuit es:" + str(self.lista[num]))
                        opc+=1
                        num+=1   
                     else:
                        print("Cantidad:" + str(self.lista[num])+"\n")
                        num+=1
                #print(self.lista)
                print("\nQue alquiler de auto desea borrar ?")
                borrarCUIT = int(input("Ingrese su numero de CUIT como se muestra para borrar los registros: "))
                if (borrarCUIT not in self.lista): 
                    print("\n||||___Datos no encontrados, ingreselos nuevamente__||||")
                if (borrarCUIT in self.lista):
                    vecesCUIT = self.lista.count(borrarCUIT)
                    for ves in range(vecesCUIT):
                        self.lista.pop(self.lista.index(borrarCUIT)+1)
                        self.lista.remove(borrarCUIT)    
                    print("\n### Alquiler borrado exitosamente ###")
# Confirmar seleccion 
      def confirmarAlquiler(self):
              print("Su alquiler se ha confirmado exitosamente")
              exit()                     

renta = carRental()
renta.ejecutar()
























































































































































































































































































































































