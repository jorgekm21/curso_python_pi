class Coche(): #Creacion de una clase

    def __init__(self): #Metodo de constructor, define las condiciones iniciales de los objetos
    # Cuando se crea un objeto se ejecuta automatica este metodo

        self.__largoChasis=250 #Parametros iniciales que siempre estaran en los objetos creados
        self.__anchoChasis=120
        self.__ruedas=4 #Con 2 guiones bajos, haces que la variable no sea accesible desde afuera de la clase, pero si desde adentro
        # Se conoce como encapsular una variable
        self.__enmarcha=False #Indica que el coche esta detenido

    def arrancar(self,arrancamos): #Creacion de metodo o comportamiendo del objeto

        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        # pass #Permite pasar de largo sin generar error

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

 #---------------------------------------------------------------------------------------------------------------------------       

miCoche=Coche() #Instanciar una clase, Ejemplarizar

print(miCoche.arrancar(True)) #Ejecuta el contenido dentro del metodo arrancar

miCoche.estado()

# Clase coche posee 4 propiedades y 2 comportamientos

print("----------------A continuacion creamos el segundo objeto---------------------") #Separador para guiar

miCoche2=Coche() #Segundo objeto creado

print(miCoche2.arrancar(False))

miCoche2.ruedas=2

miCoche2.estado() #Cuando se ejecuta se ve la diferencia al no haber ejecutado el metodo arrancar