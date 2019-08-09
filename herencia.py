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

        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", 
            self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculos): #Esta clase esta heredando todo lo que tiene la clase Vehiculos
    pass

miMoto=Moto("Honda", "CBR") #Hay que pasar los parametros solicitados en la clase Vehiculos en el Constructor

miMoto.estado()