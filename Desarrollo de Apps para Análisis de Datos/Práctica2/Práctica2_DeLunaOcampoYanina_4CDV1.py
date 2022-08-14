"""
DATOS DEL CREADOR:
Alumno: De Luna Ocampo Yanina
Grupo: 4CDV1
Carrera: Licenciatura en Ciencia de Datos
Fecha: 12/03/2022
"""

import random

# Declaramos las variables que necesitaremos usar durante la practica
id = 0

class Cliente:

    nombre = []
    anioNac = []
    dinero = 0
    cuenta = []

    def __init__(self, nombre, anioNac):
        self.nombre = nombre
        self.anioNac = anioNac

    # Definimos las funciones que utilizaremos, todas las operaciones de los menus que aparezcan
    def createID(self):
        miID = []
        miID = random.random()
        print(miID)

    def nombre(self, nombre):
        nombre = input("Digite su nombre: ")
        apellido = input("Digite su apellido: ")
        print(nombre + apellido)

    def modNombre(self, nombre):
        nombre = input("Digita correctamente tu nombre: ")
        print("Tu nuevo nombre es: ", nombre)

    def anioNac(self, anioNac):
        anioNac = input("Digita tu anio de nacimiento: ")
        print(anioNac)

    def direccion(self):
        direccion = input("Digita tu direccion: ")
        print(direccion)

    def newClient(self, miID, nombre, apellido, anioNac, direccion, cuentasReg, noCuentas):

        print("---------Creara su cuenta.---------")

        self.createID
        self.nombre
        self.apellido
        self.anioNac
        self.direccion
        self.noCuentas

        tuCuenta = {'id':miID, 'Nombre':nombre, 'Apellido':apellido, 'anioNac':anioNac, 'Direccion':direccion, 'Cuenta':{'Saldo':0, 'numCuenta':noCuentas}}

        print("El usuario creado es: " + nombre, apellido + " con anio de nacimiento en " + anioNac + " y direccion en " + direccion + "\nSu identificador unico es: " + miID)
        input("Pulse Enter para continuar...")

        if not id in miID:
            cuentasReg.append(tuCuenta)
            # cuentasReg.append([id, nombre,apellido,anioNac,direccion,curp])
            id.append(miID)
            print("Cuenta creada.")
            return cuentasReg
        print("Ya existe un usuario con el mismo ID.")

        return cuentasReg

    # Modifica algun dato del cliente que haya digitado mal 
    def modClient(self):
        print("--")

    def noCuentas(self, cuenta):
        print(cuenta)




# print("--------------------------------------------------------------------------------------------------------------")

# Creamos nuestra clase banco 
class bank_account:
    print("...")
    # Crea una cuenta nueva de un cliente previamente registrado, se le notifica que ya tiene una cuenta bancaria 
    def newAccount(self, noCuentas):
        print("--")
        v = len(self.noCuentas)

        if v == 0:
            self.noCuentas[0]
        elif v == 1:
            self.noCuentas[1]

# Creamos nuestra clase operaciones bancarias 
class opBank:

    dinero = 0
    cuentasReg = []

    # Constructor
    def __init__(self, dinero, cuentasReg):
        self.dinero = dinero
        self.cuentasReg = cuentasReg

    # OperacionBancaria: retiro. 
    def wd(self, dinero):
        print("---")
        cantidad = float(input("Digita la cantidad a retirar: "))
        if cantidad > self.dinero:
            print("Saldo insuficiente. :(")
        else: 
            self.dinero -= cantidad

        if dinero >= 100000:
            print("Tu cuenta es considerada premium.")
        else:
            print("Tu cuenta es considerada estandar.")

    # OperacionBancaria: deposito. 
    def deposit(self, dinero):
        cantidad = float(input("Digita la cantidad a depositar: "))
        self.dinero += cantidad
        print(dinero)
        print("La cantidad se ha aniadido a su cuenta bancaria.")

        if dinero >= 100000:
            print("Tu cuenta es considerada premium.")
        else:
            print("Tu cuenta es considerada estandar.")

    # OperacionBancaria: genera el reporte del cuenta del cliente. 
    def reportAccount(self, cuentasReg):
        print("---")
        print(cuentasReg)

        for a in range(len(cuentasReg)):
            for b in range(len(cuentasReg)):
                print(cuentasReg[a][b])

    # Mostramos el saldo dentro de la cuenta 
    def mostrarSaldo(self, dinero):
        print("\nTu saldo disponible neto: ", dinero)

# clnt = Cliente()
# cuenta = bank_account

# Funcion menu para pasar todos los parametros y funciones necesarias 
def myMenu():

    print("\n---------------------Bienvenido a tu banco.--------------------- ")
    mist = 0
    while mist != 5:
        print("\nLas posibles operaciones dentro de tu cuenta bancaria son: ")
        print("\t1. Crear nuevo cliente.")
        print("\t2. Modificar datos de cliente.")
        print("\t3. Crear una nueva cuenta.")
        print("\t4. Operaciones bancarias.")
        print("\t5. Salir.")

        mist = int(input("\nDigita la opcion que desees para este modulo: "))

        if mist == 1:
            nom = "Yanina"
            yob = 2001
            clnt = Cliente(nom, yob)
            print(clnt.nombre)
            clnt.createID()

        if mist == 2:
            print("\nModificaras tus datos de cliente.")
            # modNombre(nombre)

        if mist == 3:
            print("\nCrearas una nueva cuenta bancaria.")

        if mist == 4:
            try:
                bankSln = 0
                while bankSln != 5:
                    print("\nLas operaciones posibles dentro de este modulo son: ")
                    print("\t1. Consultar saldo.")
                    print("\t2. Hacer retiros.")
                    print("\t3. Hacer depositos.")
                    print("\t4. Generar reporte de cuenta.")
                    print("\t5. Atras.")

                    bankSln = int(input("\nDigita la operacion deseada para este modulo: "))

                    if bankSln == 1:
                        print("---")
                        operaciones.mostrarSaldo(dinero=cantidad)

                    if bankSln == 2:
                        cantidad = 500
                        operaciones = opBank(cantidad)
                        operaciones.wd(dinero=cantidad)
                        
                    if bankSln == 3:
                        cantidad = 500000
                        operaciones = opBank(cantidad)
                        operaciones.deposit(dinero=cantidad)
                            
                    if bankSln == 4:
                        operaciones.reportAccount()

            except ValueError:
                print("\nOperacion incorrecta, intentelo nuevamente.")

        if mist == 5:
            print("El sistema salio con exito.")
            exit(5)


# Inicializamos el programa llamando a nuestra funcion menu
if __name__ == '__main__':
    myMenu()