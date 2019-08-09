class Coche():

    def desplazamiento(self):

        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):

        print("Me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):

        print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(vehiculo): #Polimorfismo!! Asigna un objeto a distintas clases, cambiando su comportamiento

    vehiculo.desplazamiento() #Llega y define a cual metodo desplazamiento tiene que consultar
    # 3 - Detecta a cual pertenece y manda a ejecutar el metodo desplazamiento que le pertenezca al tipo de objeto cada vez que llega aca

miVehiculo=Moto() # 1 - Se Crea objeto de tipo Camion

desplazamientoVehiculo(miVehiculo) # 2 - Se envia a la funcion desplazamientoVehiculo para su procesamiento