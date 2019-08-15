from tkinter import * #Libreria para manejo de graficos
#La extension del archivo pyw permite abrir la ventana sin que se abra el panel de la consola

raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,0) #Si es 0 no permite redimensionar la pantalla, 1 si lo permite

# raiz.iconbitmap("gato.ico") #Cambia el favicon de la ventana

raiz.geometry("640x480") #Resolusion inicial de la ventana

raiz.config(bg="blue") #Color de fondo de ventana

raiz.mainloop() #Muestra la ventana principal