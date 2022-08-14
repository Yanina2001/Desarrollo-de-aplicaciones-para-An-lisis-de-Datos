"""
DATOS DEL CREADOR:
Alumno: De Luna Ocampo Yanina
Grupo: 4CDV1
Carrera: Licenciatura en Ciencia de Datos
Fecha: 19/03/2022
"""
# Funciones que usaré
import random 

# Varibales que usaré durante el programa
listaClientes = []
depositos = 0
retiros = 0

# Creo mi clase cliente
class Cliente():

    nombre = ""
    direccion = ""
    yob = 0
    cuentasNo = []
    idClt = ""

    # Constructor
    def __init__(self, recibeNombre, recibeYob):
        self.nombre = recibeNombre
        self.direccion = input("Digita tu dirección: ")
        self.yob = recibeYob
        self.idClt = random.randint(1000,9999)

    # Setters y Getters
    def getID(self):
        print("--")
        return self.idClt

    def getNombre(self):
        return self.nombre
    def setNombre(self, name):
        self.nombre = name

    def getDireccion(self):
        return self.direccion   
    def setDireccion(self, direction):
        self.direccion = direction

    def getYob(self):
        return self.yob

    def getCuenta(self):
        return self.cuentasNo
    def setCuenta(self):
        maximoC = len(self.cuentasNo)
        if maximoC == 1:
            acc = Cuenta()
            self.cuentasNo.append(acc)
        else:
            print("No puede haber más.")

    def verUser(self):
        print("\nTu ID es: ", self.getID())
        print("\nNombre de Cliente: ", self.getNombre())
        print("\nSu año de nacimiento es: ", self.getYob())
        print("\nSu dirección es: ", self.getDireccion())


# Creo mi clase cliente
class Cuenta():

    idAcc = ""
    typeOfAc = ""
    netBalance = 0
    giveNIP = 0

    # Constructor
    def __init__(self):
        print("--")
        self.idAcc = random.random(1,99)
        self.typeOfAc = "Estandar"
        self.netBalance = 0
        self.giveNIP = random.random(1,99)

    # Setters y Getters
    def getMyID(self):
        return self.idAcc
    
    def getType(self):
        return self.typeOfAc
    def setType(self, typeAcc):
        self.typeOfAc = typeAcc

    def getSaldo(self):
        return self.netBalance
    def setSaldo(self, totBalance):
        self.netBalance = totBalance
        if (totBalance >= 100000):
            self.setType("Premium")
        else:
            self.setType("Estandar")

    def getUrNIP(self):
        return self.giveNIP
    def setUrNIP(self, urNIP):
        self.giveNIP = urNIP

    def verDatos(self):
        print("\nId de cuenta: ", self.idAcc())
        print("\nTipo de cuenta: ", self.getType())
        print("\nSaldo de cuenta: ", self.getSaldo())
        print("\nNIP dado: ", self.getUrNIP())

# Creo mi clase operaciones bancarias
class opBank:

    dinero = 0
    cuentasReg = []

    def existeCliente(self):
        print("-_-")

    def mostrarSaldo(self):
        print("---")

    # OperacionBancaria: retiro. 
    def wd(self, idCli, idAcc, monto):
        print("---")
        """Aquí lo que hago es comparar y ver primero primero si el ID dado se encuentra en los existentes, de ahí vemos si el ID de cuenta es igual, 
        para así poder acceder a las operaciones bancarias en la cuenta correcta"""
        for objCli in listaClientes:
            if (objCli.getID == idCli):
                for objCuenta in objCli.getCuenta:
                    if (objCuenta.getidAcc == idAcc):
                        balance = objCuenta.getSaldo
                        actualBa = balance - monto
                        objCuenta.setSaldo(actualBa)

    # OperacionBancaria: deposito. 
    """Aquí lo que hago es comparar y ver primero primero si el ID dado se encuentra en los existentes, de ahí vemos si el ID de cuenta es igual, 
    para así poder acceder a las operaciones bancarias en la cuenta correcta"""
    def deposit(self, idCli, idAcc, monto):
        print("---")
        for objCli in listaClientes:
            if (objCli.getID == idCli):
                for objCuenta in objCli.getCuenta:
                    if (objCuenta.getidAcc == idAcc):
                        balance = objCuenta.getSaldo
                        actualBa = balance + monto
                        objCuenta.setSaldo(actualBa)

    # OperacionBancaria: genera el reporte del cuenta del cliente. 
    """Accedemos a lo mismo, pero para obtener el saldo."""
    def reportAccount(self, idCli, idAcc):
        print("---")
        for objCli in listaClientes:
            if (objCli.getID == idCli):
                for objCuenta in objCli.getCuenta:
                    if (objCuenta.getidAcc == idAcc):
                        return objCuenta.getSaldo


# Creo mi menú llamando las funciones
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
            nom = input("Digita el nombre a registrar: ")
            anio = input("Digita el anio de nacimiento: ")
            cliN = Cliente(nom, anio)
            idkID = cliN.getID()
            print("El ID dado es: ", idkID)
            listaClientes.append(cliN)
            cliN.verUser()

        if mist == 2:
            print("\nModificaras tus datos de cliente.")
            

        if mist == 3:
            print("\nCrearas una nueva cuenta bancaria.")
            antrID = input("Digite su ID de cuenta: ")
            for objCli in listaClientes:
                if (antrID == objCli.getID):
                    print("Ok, creación de cuenta permitida.")
                    objCli.setCuenta()

        if mist == 4:
            idPer = input("Digite su ID de Cliente: ")
            idAccount = input("Digite el ID de su Cuenta: ")
            opBk = opBank()

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
                        print("Consultará su saldo")
                        opBk.mostrarSaldo(idPer, idAccount)

                    if bankSln == 2:
                        print("Retirará dinero de su cuenta.")
                        opBk.wd(idPer, idAccount)
                        
                    if bankSln == 3:
                        print("Hará un depósito a su cuenta.")
                        opBk.deposit(idPer, idAccount)
                            
                    if bankSln == 4:
                        opBk.reportAccount(idPer, idAccount)

            except ValueError:
                print("\nOperacion incorrecta, intentelo nuevamente.")

        if mist == 5:
            print("El sistema salio con exito.")
            exit(5)


# Inicializamos el programa llamando a nuestra funcion menu
if __name__ == '__main__':
    myMenu()