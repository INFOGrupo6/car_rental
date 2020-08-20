#codigo luis
# Sistema de renta de vehiculos 
print("\nBienvenido a la renta de Autos!")
class carRental: 
      def __init__(self):
         self.lista = []
         self.costos = []     
      def ejecutar(self):    
       global queDia
       queDia = input("Que día es hoy?: ")
       ingreso = True  
       while(ingreso):   
              print("\nQue desea hacer?")
              print("Las opciones son:\n1- Alquilar un auto \n2- Mostrar autos rentados \n3- Editar Autos \n4- Confirmar registros/mostrar Facturación \n5- Devolver auto\n6- Salir del sistema")
              try:
                 self.opcion = int(input("\nDigite la operacion que desea realizar: ")) 
              except ValueError:
                 print("\n::::: Error, ingrese solo numeros enteros :::::")
                 continue
  
              if (self.opcion == 6):
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
              elif (self.opcion == 5):
                   self.devolverAuto()

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
                         if queDia.lower() == "miercoles" and str(self.cuit)[:2] == "26":
                            self.costos.append((self.dias * 2000) - ((self.dias * 2000) / 20) - 50)
                         elif queDia.lower() == "miercoles" and str(self.cuit)[:2] != "26":
                            self.costos.append((self.dias * 2000) - 50)
                         elif queDia.lower() != "miercoles" and str(self.cuit)[:2] == "26":
                            self.costos.append((self.dias * 2000) - ((self.dias * 2000) / 20))
                            print(str(self.cuit)[:2])
                         else:
                            self.costos.append(self.dias * 2000)                       
                      elif (opc == 2):
                         self.cuit = int(input("Introduzca el CUIT: ")) 
                         self.horas = int(input("Introduzca las horas a alquilar el vehiculo: ")) 
                         self.lista.append(self.cuit)  
                         self.lista.append(self.horas)
                         if queDia.lower() == "miercoles" and str(self.cuit)[:2] == "26":
                            self.costos.append((self.horas * 100) - ((self.horas * 100) / 20) - 50)
                         elif queDia.lower() == "miercoles" and str(self.cuit)[:2] != "26":
                            self.costos.append((self.horas * 100) - 50)
                         elif queDia.lower() != "miercoles" and str(self.cuit)[:2] == "26":
                            self.costos.append((self.horas * 100) - ((self.horas * 100) / 20))
                         else:
                            self.costos.append(self.horas * 100) 
                      elif (opc == 3):
                         self.cuit = int(input("Introduzca el CUIT: ")) 
                         self.km = int(input("Introduzca los km que va a recorrer con el vehiculo: ")) 
                         self.lista.append(self.cuit)  
                         self.lista.append(self.km)  
                         if queDia.lower() == "miercoles" and str(self.cuit)[:2] == "26":
                            self.costos.append((self.km * 10 + 100) - ((self.km * 10 + 100) / 20) - 50)
                         elif queDia.lower() == "miercoles" and str(self.cuit)[:2] != "26":
                            self.costos.append((self.km * 10 + 100) - 50)
                         elif queDia.lower() != "miercoles" and str(self.cuit)[:2] == "26":
                            self.costos.append((self.km * 10 + 100) - ((self.km * 10 + 100) / 20))
                         else:
                            self.costos.append(self.km * 10 + 100)
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
                        print("________________\nBorrar Opc:N°"+str(opc))
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
#PARA DEVOLVER AUTO ALQUILADO:                    
      def devolverAuto(self):
          mostrar = self.mostrarAutos()
          print("\nQue alquiler de auto desea devoler?")
          devolverCUIT = int(input("Ingrese el numero de CUIT para devolverlo: "))
          devolverTime = int(input("Ingrese la cantidad de dias/horas/km que pidió en el registro: "))
          realTime = int(input("Ingrese la cantidad de dias/horas/km reales que realizó: "))
          if (devolverCUIT not in self.lista): 
                    print("\n||||___Datos no encontrados, ingreselos nuevamente__||||")
          if (devolverTime in self.lista):
              if realTime > devolverTime:
                  print("El usuario tiene que devolver el doble del dinero total!")
                  print(self.costos)

# Confirmar seleccion 
      def confirmarAlquiler(self):
              print("Su alquiler se ha confirmado exitosamente")
              print(f"el costo de este alquiler es de: ${self.costos[0]}")
              exit()                     

renta = carRental()
renta.ejecutar()






















































































































































































































































































































































