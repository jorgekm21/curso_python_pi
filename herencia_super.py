class Persona():

    def __init__(self, nombre, edad, Lugar_residencia):

        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=Lugar_residencia

    def descripcion(self):

        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugar_residencia)

class Empleado(Persona): #Un Empleado siempre es una Persona

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #Llamando el metodo init de la clase padre, enviando los parametros completos

        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):

        super().descripcion() #Ejecuta el contenido de la funcion de la clase padre con el nombre indicado

        print("Salario:", self.salario, "\nAntiguedad: ", self.antiguedad) #Se ejecuta despues

Manuel=Empleado(1500, 15, "Manuel", 55, "Venezuela") #Al emplear super, hay que enviar todos los parametros

Manuel.descripcion()

print(isinstance(Manuel, Persona)) #Permite saber si un objeto pertenece a una clase en especifico