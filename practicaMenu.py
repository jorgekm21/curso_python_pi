from tkinter import *

root=Tk()

barraMenu=Menu(root) # Declara Menu
root.config(menu=barraMenu, width=300, height=300) # Asigna Menu

# Composicion del Menu Archivo
archivoMenu=Menu(barraMenu, tearoff=0) # tearoff=0 Funciona para eliminar lineas punteadas del menu
archivoMenu.add_command(label="Nuevo") # .add_command() Funciona para agregar un submenu
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator() # .add_separator() Funciona para agregar un separador, lo que permite dividir el menu en grupos
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

# Composicion del Menu Edicion
archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu) # .add_cascade Permite agregar elementos a un menu
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()