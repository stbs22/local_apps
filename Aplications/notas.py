from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *

default = "300x100"

notas_input = []
columna_input = -1

Elementos = []

driver = webdriver.Chrome("chromedriver")
driver.get("https://notas.duoc.cl/Notas/")


def ventana_inicio():
    
    global inicio
    inicio=Tk()
    inicio.geometry("350x350")
    inicio.title("Automata")

    Label(text="Menu", bg="LightBlue", width="300", height="2").pack()
    Label(text="").pack() 

    global strNotas
    strNotas = StringVar()
    global intColumna
    intColumna = StringVar()
 
    global notas
    global columna
    Label(text="Notas: ").place(x = 48, y = 55)
    Label(text="Columna: ").place(x = 30, y = 79)

    notas = Entry(textvariable=strNotas)
    columna = Entry(textvariable=intColumna)
    notas.pack()
    columna.pack()

    Label(text="").pack()
    Button(text="Registrar Entradas", width=18, height=1, command=regInput).pack()
    Label(text="").pack()

    Button( text="Escanear Página", height="1", width="30", bg="LightGray", command=escaneo ).pack() 
    Label(text="").pack()

    Button( text="Subir Notas a la página", height="1", width="30", bg="LightGray", command=subir_nota ).pack() 
    Label(text="").pack()  

    Button( text="Terminar", height=1, width=10, bg="Gray", command=terminar).pack() 
    Label(text="").pack()  

    Button(text="Ver Notas", width=5, height=1, command = revisar).place(x = 0, y = 0)
    Button(text="Ayuda", width=5, height=1, command = ayuda).place(x = 283, y = 0)

    inicio.mainloop()

def escaneo():
  
  #Juego con Scamper
  #Revisar dimensiones y cantidad de alumnos

  texto("En desarrollo\n Si va a subir, favor no cambiar de página","Yellow",default)

def subir_nota():

  if(len(notas_input) == 0):
    texto("Entradas Vacías","Yellow",default)
  elif(len(Elementos) == 0):
    texto("Escaneo de página faltante o erroneo\n Elementos vacíos","Yellow",default)
  
  else:
    #Acceder a elementos y transcribir para lista notas_input
    texto("Notas Subidas","LightBlue",default)

def regInput():
  global notas_input, columna_input

  try: 
    if strNotas.get() == "":
      raise Exception("Sin Notas")
    if intColumna.get() == "":
      raise Exception("Sin columna")

    notas_input = strNotas.get().replace(",",".").split(sep=":")
    columna_input = int(intColumna.get())

    texto("Se han guardado "+str( len(notas_input) )+" nota(s)\n\n listo para subir en columna n°"+str(columna_input),"LightBlue","300x150")
  
  except Exception as e: 
    texto("Error de formato\n\nExcepción: "+str(e),"Red","300x150")

def revisar():
  if(len(notas_input) != 0):
    texto("Cantidad de Notas: "+str(len(notas_input))+"\nNotas desplegadas en consola\n\nPreparadas para columna "+str(columna_input),"LightBlue",default)
    print(notas_input)
  else:
    texto("Entrada de notas vacías","Yellow",default)

def ayuda():
  texto("Ubicar manualmente el curso objetivo en el Buscador.\n\nEscanear cuando buscador se encuentre en la página con la\n planilla correspondiente, el código debe registrar los elementos.\n\nPegar notas con COMAS separadas por \":\"\nEg: 3,2:6,4:5,5\n\nIndicar posición de Columna para subir notas\n(Contar SOLO COLUMNAS CON NUMEROS ALTERABLES\n y sucesivamente, contar a partir del numero 1)\n","LightBlue","400x300")

def terminar():
  driver.close()
  exit(0)

def texto(mensaje_texto,color,geometry):
    global mensaje
    
    def cerrar():
      mensaje.destroy()
    
    mensaje = Toplevel(inicio)
    mensaje.title("popup")
    mensaje.geometry(geometry) #300x200

    Label(mensaje,text="").pack()
    Label(mensaje, text=mensaje_texto, bg=color).pack()
    Label(mensaje, text="").pack()
    Button(mensaje, text="Volver", width=10, height=1, bg="LightGray", command=cerrar ).pack() 

try:

  ventana_inicio()  
  driver.close()

except Exception as e: #ValueError

    print("Algo salió Mal:\n",e)

    driver.close()