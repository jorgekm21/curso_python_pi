from tkinter import *

root = Tk()
"""
IntVar() guarda los datos almacenados de tipo entero en el sistema, funciona para independizar los radiobuttons

Label es una simple etiqueta de texto para los radiobuttons

Radiobutton() se especifica como primer parametro el sitio donde quieras que aparezca (root por ejemplo)
y se le puede enviar el parametro text para indicar lo que quieres que diga, variable sirve para captar la variable
que domina y value es para darle un valor a esa variable cuando se tenga pulsado sobre ese radiobutton

.pack() sirve para poder empaquetar o renderizar el objeto que se esta creando
"""
varOpcion=IntVar()

def imprimir():
    # print(varOpcion.get())
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido Masculino")
    elif varOpcion.get()==2:
        etiqueta.config(text="Has elegido Femenino")
    else:
        etiqueta.config(text="Has elegido otras opciones")

Label(root, text="Genero: ").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Otras Opciones", variable=varOpcion, value=3, command=imprimir).pack()


etiqueta=Label(root)
etiqueta.pack()




root.mainloop()