from io import open

archivo_texto=open("archivo.txt", "r") #Crea el archivo txt de nombre archivo si no existe donde W es para escribir, R para leer, A para añadir mas lineas
#R+ para lectura y escritura

""" frase="Estupendo dia para estudiar Python \nel miercoles"

archivo_texto.write(frase) #Abre el archivo y escribe el contenido de frase

archivo_texto.close() #Cierra el archivo en memoria """

""" texto=archivo_texto.read() #Lee el contenido del archivo

archivo_texto.close()

print(texto) """

""" lineas_texto=archivo_texto.readlines() #Readlines convierte las lineas del texto en una lista

archivo_texto.close()

print(lineas_texto[1]) """

""" archivo_texto.write("\nsiempre es una buena ocasion para estudiar Python")

archivo_texto.close() """

print(archivo_texto.read())

archivo_texto.seek(11) #Mueve el cursos a una posicion en caracter exacta

print(archivo_texto.read(18)) #Lee hasta el caracter que se le indique