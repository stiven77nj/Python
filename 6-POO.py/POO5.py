class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def descripcion(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Direccion: ",self.direccion)


class Empleado(Persona): # Un empleado siempre es una persona, pero una persona no simpre es un empleado
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, direccion_empleado):
        super().__init__(nombre_empleado,edad_empleado,direccion_empleado) # Llamamos el metodo init de la clase padre
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario)
        print("Antiguedad: ",self.antiguedad," anios")


empleado1 = Empleado(8000000,7,"Nicolas",19,"Colombia")
empleado1.descripcion()
print(isinstance(empleado1, Empleado)) # Objeto empleado1 es de la clase Empleado
print(isinstance(empleado1, Persona)) # Onjeto empleado1 es tambien una Persona
