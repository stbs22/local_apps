# CREANDO LOGIN CON PYTHON Y TKINTER
# A BASE DE ARCHIVOS EN DIRECTORIO LOCAL

#IMPORTAMOS LIBRERÍAS NECESARIAS.
from tkinter import *
import os

#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
    
    global ventana_principal
    
    ventana_principal=Tk()

    #DIMENSIONES DE LA VENTANA
    ventana_principal.geometry("300x250")

    #TITULO DE LA VENTANA
    ventana_principal.title("Login")

    Label(text="REGISTRO", bg="LightBlue", width="300", height="2").pack()
    
    #Espacio en blanco
    Label(text="").pack() 

    #BOTÓN "Acceder"
    Button( text="Acceder", height="2", width="30", bg="LightGray", command=login ).pack() 
    Label(text="").pack()
    
    #BOTÓN "Registrarse".
    Button( text="Registrarse", height="2", width="30", bg="LightGray", command=registro ).pack() 
    Label(text="").pack()  

    #BOTÓN "Cancelar".
    Button( text="Cancelar", height="1", width="10", bg="Gray", command=exit).pack() 
    Label(text="").pack()
    
    ventana_principal.mainloop()


def registro():

    global ventana_registro, nombre_usuario, clave, entrada_nombre, entrada_clave

    ventana_registro = Toplevel(ventana_principal); ventana_registro.title("Registro"); ventana_registro.geometry("300x250")
    
    #VARIABLE STRING COMO INPUT
    nombre_usuario = StringVar() 
    clave = StringVar() 
 
    Label(ventana_registro, text="Introduzca datos\n").pack()

    Label(ventana_registro, text="Nuevo Usuario *").pack()    
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario)
    entrada_nombre.pack()

    Label(ventana_registro, text="Contraseña *").pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*')
    entrada_clave.pack()
    
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack()

    Boton_Cancelar(ventana_registro)

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña\n").pack()
 
    global verifica_usuario
    global verifica_clave
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
    Label(ventana_login, text="Nombre usuario").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña").pack()

    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()

    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()
    Boton_Cancelar(ventana_login)

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()

    #BORRA INFORMACIÓN INGRESADA
    entrada_login_usuario.delete(0, END)
    entrada_login_clave.delete(0, END) 
 
    #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    lista_archivos = os.listdir() 

    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".
 
def exito_login():
    global ventana_exito

    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")

    Label(ventana_no_clave, text="").pack()
    Label(ventana_exito, text="Acceso exitoso master",bg="LightGreen").pack()
    Button(ventana_exito, text="OK", command=borrar_exito_login).pack()

#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave

    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")

    Label(ventana_no_clave, text="").pack()
    Label(ventana_no_clave, text="Contraseña incorrecta ", bg="red").pack()
    Label(ventana_no_clave, text="").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".


#VENTANA DE "Usuario no encontrado"
def no_usuario():
    global ventana_no_usuario

    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")

    Label(ventana_no_clave, text="").pack()
    Label(ventana_no_clave, text="Usuario no encontrado", bg="red").pack()
    Label(ventana_no_clave, text="").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_clave()".


#REGISTRO USUARIO
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
    
    #CREACION DE ARCHIVO CON "nombre" y "clave"
    file = open(usuario_info, "w") 
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
def borrar_no_clave():
    ventana_no_clave.destroy() 

def borrar_no_usuario():
    ventana_no_usuario.destroy()

def Boton_Cancelar(ventana_actual):
    Label(ventana_actual, text="").pack() 
    Button(ventana_actual, text="Cancelar", height="1", width="10", bg="Gray", command=ventana_actual.destroy ).pack() 


#EJECUCIÓN DE LA VENTANA DE INICIO
ventana_inicio()  
