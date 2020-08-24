from tkinter import * #importamos libreria Tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from CodigoClasesCarRental import *
from datetime import date
import calendar
import time

"""TKINTER"""
#-----Funciones-TKINTER-----------------------------------------

def ingreso():
    global cuadro1
    try:
        cuadro2.destroy()
    except:
        None
    cuadro1=Frame(root)
    cuadro1.pack(fill="both",expand="True")
    fondo=Label(cuadro1,image=bg).place(x=0,y=0)
    tiempo = Label(cuadro1,text=str(time.strftime("%d/%m/%Y          ~Program create by Grupo 6 - Informatorio")),font=("EuroRoman",20),bg="green").place(x=10,y=620)
    ingreso = Button(cuadro1,text="Ingresar",font=("Arial",30),bg="yellow",command=pantalla_principal).place(x=250,y=520)
    salir = Button(cuadro1,text="Salir",font=("Arial",30),bg="red",command=quit).place(x=450,y=520) 

def pantalla_principal():
    global cuadro2
    try:
        try:
            cuadro1.destroy()
        except:
            None
        try:
            cuadroAlquilar.destroy()
        except:
            None
        try:  
            cuadroEditar.destroy()
        except:
            None
        try:
            cuadroMostrar.destroy()
        except:
            None
        try:
            cuadroDevolver.destroy()
        except:
            None
    except:
        messagebox.showerror("HA OCURRIDO UN ERROR","REINICE EL PROGRAMA :(")
    cuadro2=Frame(root)
    cuadro2.pack(fill="both",expand="True")
    fondo2=Label(cuadro2,image=bg2).place(x=0,y=0)
    #-----BOTONES----------------------------------------------------------------------
    alquilar_autos = Button(cuadro2,text="Alquilar Autos",font=("Arial",25),bg="#4BFCFF",command=alquilar).place(x=500,y=200)
    mostrar_autos = Button(cuadro2,text="Autos disponibles",font=("Arial",25),bg="#4BFCFF",command=mostrar).place(x=600,y=300)
    edita_autos = Button(cuadro2,text="Editar Alquiler",font=("Arial",25),bg="#4BFCFF",command=editar).place(x=700,y=400)
    devolver_alquiler = Button(cuadro2,text="Devolver alquiler",font=("Arial",25),bg="#4BFCFF",command=devolver).place(x=800,y=500)
    Salir = Button(cuadro2,text="Salir",font=("Arial",20),bg="red",command=quit).place(x=650,y=575)
    regresar_inicio = Button(cuadro2,text="Regresar",font=("Arial",20),bg="green",command=ingreso).place(x=500,y=575)

def alquilar():
    global cuadroAlquilar, cargaCUIT, cargaNOMBRE, cargaPASSWORD
    try:
        cuadro2.destroy()
    except:
        None
    cuadroAlquilar=Frame(root)
    cuadroAlquilar.pack(fill="both",expand="True")
    fondo3=Label(cuadroAlquilar,image=bg3).place(x=0,y=0)
    cuadroCliente=Frame(cuadroAlquilar,bg="blue")
    cuadroCliente.place(x=100,y=150)

    cargaCUIT = StringVar()
    etiquetaCUIT = Label(cuadroCliente,text="CUIT:",font=("Verdana",20)).grid(row=0,column=0,pady=5)
    entradaCUIT = Entry(cuadroCliente,justify="center",font=("Consolas",20),width=15,textvariable=cargaCUIT)
    entradaCUIT.grid(row=1,column=0,pady=5)

    cargaNOMBRE = StringVar()
    etiquetaNOMBRE = Label(cuadroCliente,text="NOMBRE:",font=("Verdana",20)).grid(row=2,column=0)
    entradaNOMBRE = Entry(cuadroCliente,justify="center",font=("Consolas",20),width=15,textvariable=cargaNOMBRE)
    entradaNOMBRE.grid(row=3,column=0,pady=5)

    cargaPASSWORD = StringVar()
    etiquetaPASSWORD = Label(cuadroCliente,text="PASSWORD:",font=("Verdana",20)).grid(row=4,column=0)
    entradaPASSWORD = Entry(cuadroCliente,justify="center",show="*",font=("Consolas",20),width=15,textvariable=cargaPASSWORD)
    entradaPASSWORD
    entradaPASSWORD.grid(row=5,column=0,pady=5)
    def limite(cargaPASSWORD):
        if len(entradaPASSWORD.get()) > 0:
            cargaPASSWORD.set(entradaPASSWORD.get()[4])
    cargaPASSWORD.trace("w", lambda *args: limite(cargaPASSWORD))

    Login = Button(cuadroCliente,text="LOGIN",font=("Arial",16),bg="brown",command=lambda:crearUsuario())
    Login.grid(row=6,column=0,pady=5)

    def crearUsuario():
        primerUsuario = alquilerAuto(cargaCUIT.get(), cargaPASSWORD.get(),cargaNOMBRE.get(), None, None, None)
        primerUsuario.agregarCliente()
        formularioAlquilar()
        entradaCUIT.config(state="readonly")
        entradaNOMBRE.config(state="readonly")
        entradaPASSWORD.config(state="readonly")
        Login.config(state=DISABLED)

    def formularioAlquilar():
        cuadroFormulario=Frame(cuadroAlquilar,bg="yellow")
        cuadroFormulario.place(x=400,y=150)
        etiquetaAUTO = Label(cuadroFormulario,text="ELIGE UN AUTO:",font=("Verdana",15)).grid(row=0,column=0,pady=5,columnspan=3)
        desplegableAUTOS = ttk.Combobox(cuadroFormulario,state="readonly")
        desplegableAUTOS.grid(row=1,column=0,pady=5,columnspan=3)
        desplegableAUTOS["values"] = [autos.get("ID1"),
                                    autos.get("ID2"), 
                                    autos.get("ID3"),
                                    autos.get("ID4"),
                                    autos.get("ID5")]
        opcion = IntVar()
        etiquetaOPCION = Label(cuadroFormulario,text="ELIGE UNA OPCIÓN:",font=("Verdana",15)).grid(row=2,column=0,pady=5,columnspan=3)
        opcion1 = Radiobutton(cuadroFormulario,text="DIA",variable=opcion, value=1).grid(row=3,column=0,pady=5)
        opcion2 = Radiobutton(cuadroFormulario,text="HORAS",variable=opcion, value=2).grid(row=3,column=1,pady=5)
        opcion3 = Radiobutton(cuadroFormulario,text="KMS",variable=opcion, value=3).grid(row=3,column=2,pady=5)

        cargaCANTIDAD = StringVar()
        etiquetaCANTIDAD = Label(cuadroFormulario,text="CANTIDAD:",font=("Verdana",14)).grid(row=4,column=0,pady=5,columnspan=3)
        entradaCANTIDAD = Entry(cuadroFormulario,justify="center",font=("Consolas",20),width=10,textvariable=cargaCANTIDAD).grid(row=5,column=0,pady=5,columnspan=3)
        botonAlquilar = Button(cuadroFormulario,text="ALQUILAR",font=("Arial",15),bg="green",command=lambda:crearAlquiler())
        botonAlquilar.grid(row=6,column=0,pady=5,columnspan=3)

        def crearAlquiler():
            primerfactura = alquilerAuto(cargaCUIT.get(), None,None,desplegableAUTOS.get(), opcion.get(), cargaCANTIDAD.get())
            primerfactura.factura()
            cuadroCliente.destroy()
            cuadroFormulario.destroy()


    Salir = Button(cuadroAlquilar,text="Salir",font=("Arial",20),bg="red",command=quit).place(x=650,y=575)
    regresar_inicio = Button(cuadroAlquilar,text="Regresar",font=("Arial",20),bg="green",command=pantalla_principal).place(x=500,y=575)

def mostrar():
    global cuadroMostrar
    try:
        cuadro2.destroy()
    except:
        None
    cuadroMostrar=Frame(root)
    cuadroMostrar.pack(fill="both",expand="True")
    fondo3=Label(cuadroMostrar,image=bg3).place(x=0,y=0)

    conexion = sqlite3.connect('car_rental.db')
    CursorRental = conexion.cursor()
    CursorRental.execute("SELECT AUTO FROM FACTURA")
    
    autoID1caracteristicas = Label(cuadroMostrar,text=(autos["Caracteristica1"].items()),font=("Arial",20),bg="yellow")
    autoID1caracteristicas.place(x=129,y=50)
    autoID1 = Label(cuadroMostrar,image=ID1_A)
    autoID1.place(x=50,y=0)

    autoID2caracteristicas = Label(cuadroMostrar,text=(autos["Caracteristica2"].items()),font=("Arial",20),bg="yellow")
    autoID2caracteristicas.place(x=129,y=170)
    autoID2 = Label(cuadroMostrar,image=ID2_A)
    autoID2.place(x=50,y=120)

    autoID3caracteristicas = Label(cuadroMostrar,text=(autos["Caracteristica3"].items()),font=("Arial",20),bg="yellow")
    autoID3caracteristicas.place(x=129,y=270)
    autoID3 = Label(cuadroMostrar,image=ID3_A)
    autoID3.place(x=50,y=240)

    autoID4caracteristicas = Label(cuadroMostrar,text=(autos["Caracteristica4"].items()),font=("Arial",20),bg="yellow")
    autoID4caracteristicas.place(x=129,y=390)
    autoID4 = Label(cuadroMostrar,image=ID4_A)
    autoID4.place(x=50,y=360)

    autoID5caracteristicas = Label(cuadroMostrar,text=(autos["Caracteristica5"].items()),font=("Arial",20),bg="yellow")
    autoID5caracteristicas.place(x=129,y=510)
    autoID5 = Label(cuadroMostrar,image=ID5_A)
    autoID5.place(x=50,y=480)

    for auto in CursorRental:
        #print(f"los autos ocupados son: {auto[0]}")
        if autos.get("ID1") == auto[0]:
            autoID1.config(image=ID1_R)
            autoID1caracteristicas.config(bg="grey")
        elif autos.get("ID2") == auto[0]:
            autoID2.config(image=ID2_R)
            autoID2caracteristicas.config(bg="grey")
        elif autos.get("ID3") == auto[0]:
            autoID3.config(image=ID3_R)
            autoID3caracteristicas.config(bg="grey")
        elif autos.get("ID4") == auto[0]:
            autoID4.config(image=ID4_R)
            autoID4caracteristicas.config(bg="grey")
        elif autos.get("ID5") == auto[0]:
            autoID5.config(image=ID5_R)
            autoID5caracteristicas.config(bg="grey")

    Salir = Button(cuadroMostrar,text="Salir",font=("Arial",20),bg="red",command=quit).place(x=650,y=575)
    regresar_inicio = Button(cuadroMostrar,text="Regresar",font=("Arial",20),bg="green",command=pantalla_principal).place(x=500,y=575)

def editar():
    global cuadroEditar
    try:
        cuadro2.destroy()
    except:
        None
    cuadroEditar=Frame(root)
    cuadroEditar.pack(fill="both",expand="True")
    fondo3=Label(cuadroEditar,image=bg3).place(x=0,y=0)
    CUITvar = StringVar()
    inputCUIT = Label(cuadroEditar,text="INGRESE SU CUIT:",font=("Arial",20)).place(x=500,y=100)
    entryCUIT = Entry(cuadroEditar,justify="center",font=("Consolas",20),width=17,textvariable=CUITvar).place(x=500,y=150)
    IDvar = StringVar()
    inputIDF = Label(cuadroEditar,text="INGRESE SU N° FACTURA:",font=("Arial",20)).place(x=500,y=200)
    entryIDF = Entry(cuadroEditar,justify="center",font=("Consolas",20),width=17,textvariable=IDvar)
    entryIDF.place(x=500,y=250)

    verDATOS = Button(cuadroEditar,text="VER",font=("Arial",18),bg="green",command=lambda:buscar()).place(x=550,y=300)


    CANTIDADvar = StringVar()
    etiquetaCANTIDAD = Label(cuadroEditar,text="Agrega más cantidad y disfruta!",font=("Arial",18),bg="yellow").place(x=500,y=370)
    entryCANTIDAD = Entry(cuadroEditar,justify="center",font=("Consolas",20),textvariable=CANTIDADvar)
    entryCANTIDAD.place(x=500,y=420)

    botonACTUALIZAR = Button(cuadroEditar,text="Actualizar",font=("Arial",18),bg="#4BFCFF",command=lambda:update()).place(x=550,y=470)

    def buscar():
        try:
            conexion = sqlite3.connect('car_rental.db')
            CursorRental = conexion.cursor()
            CursorRental.execute("SELECT ID,CLIENTE,CANTIDAD FROM FACTURA WHERE ID="+ IDvar.get())
            for cantidad in CursorRental:
                if CUITvar.get() == str(cantidad[1]):                     
                    CANTIDADvar.set(cantidad[2])
                else:
                    messagebox.showwarning("Upss...","N° de factura no coincide con su cuenta!. ")
                idVER = cantidad[0]
            if IDvar.get() != str(idVER):
                messagebox.showwarning("Weep","N° de factura no encontrada!. ")
            conexion.commit()
        except:
            messagebox.showerror("Weep","Factura no encontrada!. ")

    def update():
        try:
            conexion = sqlite3.connect('car_rental.db')
            CursorRental = conexion.cursor()
            CursorRental.execute("UPDATE FACTURA SET CANTIDAD='"+ CANTIDADvar.get() +
                    "'WHERE ID="+ IDvar.get())
            conexion.commit()
            messagebox.showinfo("OK!","Actulizaste con exito la cantidad!") 
        except:
            messagebox.showerror("Weep","Algo salio mal!. ")
   

    Salir = Button(cuadroEditar,text="Salir",font=("Arial",20),bg="red",command=quit).place(x=650,y=575)
    regresar_inicio = Button(cuadroEditar,text="Regresar",font=("Arial",20),bg="green",command=pantalla_principal).place(x=500,y=575)

def devolver():
    global cuadroDevolver
    try:
        cuadro2.destroy()
    except:
        None
    cuadroDevolver=Frame(root)
    cuadroDevolver.pack(fill="both",expand="True")
    fondo3=Label(cuadroDevolver,image=bg3).place(x=0,y=0)

    my_date = date.today()
    hoy = calendar.day_name[my_date.weekday()]
    if hoy == "Monday":
        hoy = "Lunes"

    DIA = Label(cuadroDevolver,text="Hoy es " + hoy,font=("Arial",20),bg="yellow").place(x=800,y=20)

    CUITvar = StringVar()
    inputCUIT = Label(cuadroDevolver,text="INGRESE SU CUIT:",font=("Arial",20)).place(x=50,y=100)
    entryCUIT = Entry(cuadroDevolver,justify="center",font=("Consolas",20),width=17,textvariable=CUITvar).place(x=50,y=150)
    IDvar = StringVar()
    inputIDF = Label(cuadroDevolver,text="INGRESE SU N° FACTURA:",font=("Arial",20)).place(x=50,y=200)
    entryIDF = Entry(cuadroDevolver,justify="center",font=("Consolas",20),width=17,textvariable=IDvar)
    entryIDF.place(x=50,y=250)

    verDATOS = Button(cuadroDevolver,text="VER",font=("Arial",18),bg="green",command=lambda:buscar()).place(x=70,y=300)

    CANTIDADvar = StringVar()
    etiquetaCANTIDAD = Label(cuadroDevolver,text="INGRESE CANTIDAD REAL CONSUMIDA:",font=("Arial",18),bg="yellow").place(x=50,y=370)
    entryCANTIDAD = Entry(cuadroDevolver,justify="center",font=("Consolas",20),textvariable=CANTIDADvar)
    entryCANTIDAD.place(x=50,y=420)

    botonBORRAR = Button(cuadroDevolver,text="DEVOLVER ALQUILER",font=("Arial",18),bg="#4BFCFF",command=lambda:borrar()).place(x=50,y=470)

    def buscar():
        try:
            conexion = sqlite3.connect('car_rental.db')
            CursorRental = conexion.cursor()
            CursorRental.execute("SELECT ID,CLIENTE,CANTIDAD FROM FACTURA WHERE ID="+ IDvar.get())
            for cantidad in CursorRental:
                if CUITvar.get() == str(cantidad[1]):                     
                    CANTIDADvar.set(cantidad[2])
                else:
                    messagebox.showwarning("Upss...","N° de factura no coincide con su cuenta!. ")
                idVER = cantidad[0]
            if IDvar.get() != str(idVER):
                messagebox.showwarning("Weep","N° de factura no encontrada!. ")
            conexion.commit()
        except:
            messagebox.showerror("Weep","Factura no encontrada!. ")
      
    def borrar():
        try:
            calculos()
            conexion = sqlite3.connect('car_rental.db')
            CursorRental = conexion.cursor()
            pregunta = messagebox.askquestion("ATENCIÓN!","Estas seguro de devolver este alquiler?")
            if pregunta =="yes":
                CursorRental.execute("DELETE FROM FACTURA WHERE ID="+  IDvar.get())
                messagebox.showinfo("Listo!","Alquiler devuelto con exito!. ")
                cuadroDevolver.destroy()
                pantalla_principal()
            conexion.commit()
            frameCalculo.destroy()
            
        except:
            messagebox.showerror("Weep","Algo salio mal!. ")

    def calculos():
        global frameCalculo
        try:
            frameCalculo = Frame(cuadroDevolver)
            frameCalculo.place(x=600,y=100)
            etiquetaFACTURA = Label(frameCalculo,text="DETALLE FACTURA:",font=("Arial",20),bg="yellow").grid(row=0,column=0)
            conexion = sqlite3.connect('car_rental.db')
            CursorRental = conexion.cursor()
            CursorRental.execute("SELECT * FROM FACTURA WHERE ID="+ IDvar.get())
            deTABLA = CursorRental.fetchall()
            etiquetaCLIENTE = Label(frameCalculo,text="Cliente: "+deTABLA[0][1],font=("Arial",20),bg="yellow")
            etiquetaCLIENTE.grid(row=1,column=0)
            etiquetaAUTO = Label(frameCalculo,text="AUTO: "+deTABLA[0][2],font=("Arial",20),bg="yellow")
            etiquetaAUTO.grid(row=2,column=0)

            if deTABLA[0][3] == "1":
                opcionAlquilado = "DIAS"
                Precio = 2000 * int(deTABLA[0][4])
                if deTABLA[0][1][:2] == "26":
                    PrecioPARCIAL = Precio - (Precio / 20)
                else:
                    PrecioPARCIAL = Precio
            elif deTABLA[0][3] == "2":
                opcionAlquilado = "HORAS"
                Precio = 100 * int(deTABLA[0][4])
                if deTABLA[0][1][:2] == "26":
                    PrecioPARCIAL = Precio - (Precio / 20)
                else:
                    PrecioPARCIAL = Precio
            elif deTABLA[0][3] == "3":
                opcionAlquilado = "KM/S"
                Precio = (10 * int(deTABLA[0][4])) + 100
                if deTABLA[0][1][:2] == "26":
                    PrecioPARCIAL = Precio - (Precio / 20)
                else:
                    PrecioPARCIAL = Precio

            if int(CANTIDADvar.get()) > int(deTABLA[0][4]):
                PrecioTOTAL = str(PrecioPARCIAL * 2)
            else:
                PrecioTOTAL = str(PrecioPARCIAL)
            
        except:
            messagebox.showerror("Weep","Algo salio malX200000000!. ")

        try:
            etiquetaALQUILERPOR = Label(frameCalculo,text="ALQUILER POR "+str(opcionAlquilado),font=("Arial",20),bg="yellow")
            etiquetaALQUILERPOR.grid(row=3,column=0)
            etiquetaCANTIDADES = Label(frameCalculo,text="CANTIDAD:"+str(deTABLA[0][4]),font=("Arial",20),bg="yellow")
            etiquetaCANTIDADES.grid(row=4,column=0)
            etiquetaFECHA = Label(frameCalculo,text="FECHA:"+str(deTABLA[0][6]),font=("Arial",20),bg="yellow")
            etiquetaFECHA.grid(row=5,column=0)
            conexion = sqlite3.connect('car_rental.db')
            CursorRental = conexion.cursor()
            CursorRental.execute("UPDATE FACTURA SET PRECIO='"+ PrecioTOTAL + "'WHERE ID="+ IDvar.get())
            etiquetaPRECIO = Label(frameCalculo,text="PRECIO TOTAL A PAGAR:$"+PrecioTOTAL,font=("Arial",20),bg="yellow")
            etiquetaPRECIO.grid(row=6,column=0)        
            conexion.commit()
        except:
            messagebox.showerror("Weep","Algo salio malX9999!. ")

    Salir = Button(cuadroDevolver,text="Salir",font=("Arial",20),bg="red",command=quit).place(x=650,y=575)
    regresar_inicio = Button(cuadroDevolver,text="Regresar",font=("Arial",20),bg="green",command=pantalla_principal).place(x=500,y=575)

#-----Ventana-RAIZ----------------------------------------
root=Tk()
root.title("Alquiler de autos")
root.resizable(0,0)
root.geometry("1200x656")
root.iconbitmap("car_rental.ico")
bg=PhotoImage(file="background.png")
bg2=PhotoImage(file="background2.png")
bg3=PhotoImage(file="background3.png")
ID1_A=PhotoImage(file="autos/ID1_A.png")
ID2_A=PhotoImage(file="autos/ID2_A.png")
ID3_A=PhotoImage(file="autos/ID3_A.png")
ID4_A=PhotoImage(file="autos/ID4_A.png")
ID5_A=PhotoImage(file="autos/ID5_A.png")
ID1_R=PhotoImage(file="autos/ID1_R.png")
ID2_R=PhotoImage(file="autos/ID2_R.png")
ID3_R=PhotoImage(file="autos/ID3_R.png")
ID4_R=PhotoImage(file="autos/ID4_R.png")
ID5_R=PhotoImage(file="autos/ID5_R.png")
ingreso()
root.mainloop()
#------END------------------------------------------------