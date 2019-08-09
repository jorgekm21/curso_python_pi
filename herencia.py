class Vehiculos():

    def __init__(self, marca, modelo): #Constructor de Clase Padre Vehiculos
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):

        self.enmarcha=True

    def acelerar(self):

        self.acelera=True

    def frenar(self):

        self.frena=True

    def estado(self):

        print("\nMarca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", 
            self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos): #Si hereda de moto entonces Furgoneta podria hacer caballito (?)

    def carga(self, cargar):

        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta esta vacia"

class Moto(Vehiculos): #Esta clase esta heredando todo lo que tiene la clase Vehiculos

    hcaballito=""

    def caballito(self): #Comportamiento adicional que posee la clase Moto

        self.hcaballito="Voy haciendo el caballito"

    def estado(self): #Este comportamiento sustituye el que posee la clase padre por preferencia. Primero se carga esta cuando se emplea la herencia
    #O Mejor dicho, se sobreescribe

        print("\nMarca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", 
            self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class VElectricos(): #No hereda de nadie

    def __init__(self):
        self.autonomia=100

    def cargar_Energia(self):
        self.cargando=True

#-----------------------------------------------------------------------------------------------------------------------------------------------------

miMoto=Moto("Honda", "CBR") #Hay que pasar los parametros solicitados en la clase Vehiculos en el Constructor

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

class BicicletaElectrica(VElectricos,Vehiculos): #Herencia de multiples clases
    pass

miBici=BicicletaElectrica() #Hereda del primer constructor que se le indico en la clase