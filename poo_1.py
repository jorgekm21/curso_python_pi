class Coche(): #Creacion de una clase
    largoChasis=250 #Parametros iniciales que siempre estaran en los objetos creados
    anchoChasis=120
    ruedas=4
    enmarcha=False #Indica que el coche esta detenido

    def arrancar(self): #Creacion de metodo o comportamiendo del objeto
        self.enmarcha=True
        # pass #Permite pasar de largo sin generar error

    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

miCoche=Coche() #Instanciar una clase, Ejemplarizar

print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")
miCoche.arrancar() #Ejecuta el contenido dentro del metodo arrancar
print(miCoche.estado())

# Clase coche posee 4 propiedades y 2 comportamientos