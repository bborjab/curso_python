class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

# Crear objetos de la clase Persona
persona1 = Persona("Ana", 30)
persona2 = Persona("Luis", 25)

persona1.saludar()
persona2.saludar()
¿Qué son los métodos en una clase?
Los métodos son funciones definidas dentro de una clase que operan sobre los objetos de la misma. En el ejemplo anterior, saludar es un método de la clase Persona.

¿Cómo manejar una cuenta bancaria con POO?
Un ejemplo práctico de POO es la gestión de una cuenta bancaria. Creamos una clase BankAccount con métodos para depositar y retirar dinero, así como para activar y desactivar la cuenta.

Ejemplo de clase BankAccount
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual: {self.balance}")
            else:
                print("Fondos insuficientes")
        else:
            print("No se puede retirar, cuenta inactiva")
    
    def deactivate(self):
        self.is_active = False
        print("La cuenta ha sido desactivada")
    
    def activate(self):
        self.is_active = True
        print("La cuenta ha sido activada")

# Crear objetos de la clase BankAccount
cuenta1 = BankAccount("Ana", 500)
cuenta2 = BankAccount("Luis", 1000)

cuenta1.deposit(500)
cuenta2.withdraw(100)
cuenta1.deactivate()
cuenta1.deposit(200)
cuenta1.activate()
cuenta1.deposit(200)