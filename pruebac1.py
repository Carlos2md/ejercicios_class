class persona():
    def __init__(self, nombre, apellido, edad, altura, ciudad):
        self.name=nombre
        self.last_name=apellido
        self.age=edad
        self.tall=altura
        self.city=ciudad

    def saludar(self):
        print(f"Hola mi nombre es {self.name} tengo {self.age} y vivo en {self.city}")

    def cumple(self):
        self.age+=1

    def mudar(self,ciudad):
        self.city=ciudad

persona1= persona("Juan", "Gonzalez", 25, 1.8, "Pasto")
persona2= persona("Carlos", "Muñoz", 40, 1.7, "Pasto")
print(persona1.name)
print(persona1.last_name)
print(persona2.name)
print(persona2.last_name)

persona1.saludar()
persona2.saludar()
persona1.cumple()
print(persona1.age)
persona2.mudar("Barranquilla")
persona2.saludar()
