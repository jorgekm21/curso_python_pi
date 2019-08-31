from tkinter import *

root=Tk()

miFrame=Frame(root, width=1000, height=900)

miFrame.pack()

miImagen=PhotoImage(file="logo.png")

Label(miFrame, image=miImagen).place(x=100, y=200) #Ubica un texto en cualquier sitio dentro de la ventana

""" 
Para el metodo Label maneja multiples parametros todos opcionales para poder modificar lo que se desea agregar, contiene principalmente texto:

    text: Texto que se muestra en el Label
    anchor: Controla la posicion del texto si hay espacio suficiente para el (center por defecto)
    bg: Color de fondo
    bitmap: Mapa de bits que se mostrara como grafico
    bd: Grosor del borde (2px por defecto)
    font: Tipo de fuente a mostrar
    fg: Color de la Fuente
    width: Ancho de label en caracteres (no en pixeles)
    height: Altura de label en caracteres (no en pixeles)
    image: Muestra imagen en el label en lugar de texto
    justify: Justificacion del texto del label

"""
root.mainloop()