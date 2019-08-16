from tkinter import * #Libreria para manejo de graficos
#La extension del archivo pyw permite abrir la ventana sin que se abra el panel de la consola

raiz=Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(1,0) #Si es 0 no permite redimensionar la pantalla, 1 si lo permite

# raiz.iconbitmap("gato.ico") #Cambia el favicon de la ventana

raiz.geometry("640x480") #Resolusion inicial de la ventana

raiz.config(bg="blue") #Color de fondo de ventana

miFrame=Frame() #Crea el frame que contiene los componentes de la pagina

miFrame.pack() #Empaqueta el frame
#Side indica donde se muestra el paquete entre arriba, abajo, izquierda y derecha
#Anchor muestra el paquete en un punto cardinal N,S,E,W
#Fill expande el paquete a lo largo de un eje X, Y, Both
#Expand Permite expandir el paquete

miFrame.config(bg="red")

miFrame.config(width="630", height="470")

miFrame.config(bd=10) #Tamaño del borde del frame

miFrame.config(relief="sunken")
#Groove, Sunken

miFrame.config(cursor="pirate") #Cambia el cursor

raiz.mainloop() #Muestra la ventana principal