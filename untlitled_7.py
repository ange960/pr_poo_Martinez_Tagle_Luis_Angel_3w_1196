class Universidad:
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carerra:
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carerra):
    def __init__(self, Nombre):

        Universidad.__init__(self, Nombre)

    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")


persona = Estudiante("Harvard")
persona.carrera("psicologia")
persona.datos("Mike", 19)
