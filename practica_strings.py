""" nombreusuario=input("Introduce tu nombre de usuario: ")

print("El nombre es: ", nombreusuario.upper()) #Pone variable en mayusculas
print("El nombre es: ", nombreusuario.lower()) #Pone variable en minusculas
print("El nombre es: ", nombreusuario.capitalize()) #Pone la primera letra en mayusculas """

""" edad=input("Introduce la edad: ")

print(edad.isdigit()) #Inidica si el valor introducido es un digito """

edad=input("Introduce tu edad: ")

while(edad.isdigit())==False:

    print("Por favor, introduce un valor numerico")
    edad=input("Introduce tu edad: ")

if (int(edad)<18):

    print ("No puedes pasar")

else:

    print ("Puedes pasar")