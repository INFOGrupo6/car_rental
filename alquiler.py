class Alquiler:
    def __init__(self,nroAlquiler,cuitCliente):
         self.nroAlquiler=nroAlquiler
         self.cuitCliente=cuitCliente        

    def DescuentoMiercoles(self,precio):
        precio = precio - 50
        return precio
    def Tiempo(self,precio,horas):
         TiempoUsado=int(input("Ingrese el verdadero tiempo usado"))
         if TiempoUsado > horas:
             return precio * 2


class Hora(Alquiler):
     def __init__(self,nroAlquiler,cuitCliente,horas):
         self.tipo="Alquiler por horas"
         self.horas= horas
         self.precio= horas * 100
         super().__init__(nroAlquiler,cuitCliente)             

class Dias(Alquiler):
     def __init__(self,nroAlquiler,cuitCliente,dias):
         self.tipo="Alquiler por dias"
         self.dias= dias
         self.precio= dias * 2000
         super().__init__(nroAlquiler,cuitCliente)

class Kilometros(Alquiler):
     def __init__(self,nroAlquiler,cuitCliente):
         self.tipo="Alquiler por kilometros"
         self.precio= 100 
         super().__init__(nroAlquiler,cuitCliente)
Alquileres=[]
def Menu():
    menu=True
    while menu== True:
        valor=0
        try:
            print("Hola Buenos dias!! Este es el sistema de alquileres de auto del INFORMATORIO eligi una opcion")
            print("Presione 1 para ingresar alquilar un auto ")
            print("Presione 2 si desea ver los autos alquilados")
            print("Presione 3 si desea si desea volver el auto")
            print("Presione 4 si deseas salir")
            ingreso=int(input("Escriba el numero aqui\t"))
            if ingreso ==1 :
                valor+=1
                cuit=input("Por favor ingrese si numero de cuit\n")
                print("seleccion que tipo de contratacion que desea\n\t Por hora presione 1 \n\t Por dia presione 2 \n\t Por kilometro presione 3")
                seleccion=int(input("Ingrese el valor aqui "))
                if seleccion==1:
                    horarios=int(input("por favor ingrese la cantidad de horas que desea utilizar el servicio \t"))
                    alquiler=Hora(valor,cuit,horarios)
                    diaActual=int(input("Si hoy es miercoles presione 1 de lo contrario presione cualquier numero:\t"))
                    if diaActual == 1:
                        descuento=alquiler.DescuentoMiercoles(alquiler.precio)   
                        alquiler.precio=descuento
                    print("Gracias por utilizar el servicio de alquiler del informatorio")
                if seleccion==2:
                    horarios=int(input("por favor ingrese la cantidad de dias que desea utilizar el servicio "))
                    alquiler=Dias(valor,cuit,horarios)
                    diaActual=int(input("Si hoy es miercoles presione 1 de lo contrario presione cualquier numero:\t"))
                    if diaActual == 1:
                        descuento=alquiler.DescuentoMiercoles(alquiler.precio)   
                        alquiler.precio=descuento
                    print("Gracias por utilizar el servicio de alquiler del informatorio")    
                if seleccion==3:
                    alquiler=Kilometros(valor,cuit)
                    diaActual=int(input("Si hoy es miercoles presione 1 de lo contrario presione cualquier numero:\t"))
                    if diaActual == 1:
                        descuento=alquiler.DescuentoMiercoles(alquiler.precio)   
                        alquiler.precio=descuento        
                Alquileres.append(alquiler)    
                print("Gracias por utilizar el servicio de alquiler del informatorio")
            if ingreso ==2 :
                print("los alquileres son los siguientes")
                for x in Alquileres:
                    print("CUIT: ",x.cuitCliente, "Numero alquiler: ", x.nroAlquiler, " Tipo: ", x.tipo,"\n")
            if ingreso ==3:
                c=-1
                valorcuit=input("ingrese su numero de cuit ")
                for y in Alquileres:
                   c+=1 
                   if y.cuitCliente == valorcuit:    
                        if x.tipo == "Alquiler por horas":
                            horasreales=int(input("Ingrese la cantidad de horas reales que utilizo"))
                            if horasreales > x.horas:
                                valorReal = x.precio * 2        
                                print("Usted debe pagar ",valorReal)
                            else:
                                print("Usted debe pagar ",x.precio)
                        if x.tipo == "Alquiler por dias" :
                            horasreales=int(input("Ingrese la cantidad de dias reales que utilizo"))
                            if horasreales > x.horas:
                                valorReal = x.precio * 2        
                                print("Usted debe pagar ",valorReal)
                            else:
                                print("Usted debe pagar ",x.precio)
                        if x.tipo == "Alquiler por kilometros":
                           horasreales=int(input("Ingrese la cantidad de kilometros reales que utilizo "))
                           print(x.precio)
                           pagarkilometros= x.precio + horasreales * 10
                           print("Usted debe pagar ",pagarkilometros)          
                        Alquileres.pop(c)
                   else:
                     print("Ingreso mal el valor")             
            if ingreso == 4:
                print("Hasta la proxima")
                menu= False
        except:
            print("Ingreso mal los valores por favor empiece de nuevo")        
if __name__ == "__main__":
    Menu()
