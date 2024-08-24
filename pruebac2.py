#Crear una clase llamada UsuarioBanco con los atributos:

#Nombre 
#Edad
#Cedula
#Telefono
#Saldo

#al crear una nueva instancia el saldo debe iniciar en cero
#la clase debe tener los siguientes metodos

#deposito: se debe especificar la cantidad que se debe depositar y agregarla a saldo
#retiro: se debe descontar del saldo, si no tiene fondos suficientes para el retiro se debe informar
#consultar saldo: que informe el saldo
class usuario_banco():
    def __init__(self, nombre, edad, cedula, telefono, saldo):
        self.name=nombre
        self.age=edad
        self.id=cedula
        self.phone=telefono
        self.balance=saldo

    def consultar_saldo(self):
        print(f"Señor usuario {self.name} su saldo es: {self.balance}")

    def deposito(self):
        cantidad=float(input("Ingrese lo que desea depositar: "))
        self.balance+=cantidad

    def retiro(self):
        cantidad=float(input("Ingrese lo que desea depositar: "))
        self.balance-=cantidad

usuario1= usuario_banco("Juan", 25, 1026555630, 3126500021, 0)
usuario2= usuario_banco("Carlos", 40, 87066330, 3008500321, 0)
print(usuario1.name)
print(usuario1.id)
print(usuario2.name)
print(usuario2.id)

usuario1.deposito()
usuario1.retiro()
usuario1.consultar_saldo()
