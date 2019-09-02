from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar() #Indica que esa variable es una cadena de caracteres

cuadroNombre=Entry(miFrame, textvariable=minombre) #Cuadro de entrada de texto
cuadroNombre.grid(row=0, column=1, padx=10, pady=10) #Grid ubica el cuadro donde 0, 0 es la esquina superior izquierda
cuadroNombre.config(fg="red", justify="center") #Centra el texto dentro del contenido de la entrada de texto en el centro y asigna el color rojo

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="*") # Show hace que no muestre las letras del contenido, pero si un caracter opcional. Ideal para las contraseñas

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10) # Row = Fila, Column = Columna

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=10, pady=10) # Padx y Pady es el Padding o espacioado de los elementos

textoComentario=Text(miFrame, width=16, height=5) #Crea el cuadro de texto grande
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew") #Se adapta al tamaño del area de escritura con el sticky

textoComentario.config(yscrollcommand=scrollVert.set) #Seguimiento del posicionador de la barra de desplazamiento

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) #Sticky pega el elemento en un punto cardinal

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Contraseña:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

def codigoBoton():
    minombre.set("Jorge")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()


raiz.mainloop()