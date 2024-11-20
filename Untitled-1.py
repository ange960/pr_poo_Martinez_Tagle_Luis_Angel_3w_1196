class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultados(self):
        if self.nota >= 7:
            print("Has APROBADO guapeton eres el mejor en todo!")
        else:
            print("Has REPROBADO otra vez hermano echale mas ganas !")

# Crear instancias de la clase Estudiante
estudiante1 = Estudiante("valentin ", 4)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("luis angel martinez tagle osea yo ", 10)
estudiante2.imprimir()
estudiante2.resultados()
