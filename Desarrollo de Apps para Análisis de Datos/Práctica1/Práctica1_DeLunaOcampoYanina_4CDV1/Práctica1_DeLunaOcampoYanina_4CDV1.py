"""
Alumno: De Luna Ocampo Yanina
Grupo: 4CDV1
Carrera: Licenciatura en Ciencia de Datos
Fecha: 02/03/2022
"""

import random
 
saldo = 0
id = 0

# Crear clientes
clientes = []
noCuentas = 0
def crearCliente(id, clientes, noCuentas):
    nombre = input("Digite su nombre: ")
    apellido = input("Digite su apellido: ")
    anioNac = input("Digita tu anio de nacimiento: ")
    direccion = input("Digita tu dirección: ")
    tuCuenta = {'id':id, 'Nombre':nombre, 'Apellido':apellido, 'anioNac':anioNac, 'Direccion':direccion, 'Cuenta':{'Saldo':0, 'numCuenta':noCuentas}}
    # print(tuCuenta)
    clientes.append(tuCuenta)
    noCuentas += 1
    print("Cuenta creada")
    print("El usuario creado es: " + nombre, apellido + " con año de nacimiento en " + anioNac + " y direccion en " + direccion)
    numTarjeta()
    input("Pulse Enter para continuar...")
    return clientes, noCuentas

# Modificar datos del cliente
def modCliente():
    nom = input("Ingrese el nombre de la persona a modificar: ")
    buscar = id.__index__

# Crear nueva cuenta
def crearCuenta(nombre):
    nueNombre = input("Digite su nombre: ")
    nueApellido = input("Digite su apellido: ")
    NueAnioNac = input("Digita tu anio de nacimiento: ")
    direccion = input("Digita tu dirección: ")
    nueCuenta = {'id':id, 'Nombre':nueNombre, 'Apellido':nueApellido, 'anioNac':NueAnioNac, 'Direccion':direccion, 'Cuenta':{'Saldo':0, 'numCuenta':noCuentas}}
    # print(tuCuenta)
    clientes.append(nueCuenta)
    noCuentas += 1
    print("Cuenta creada")
    print("El nuevo usuario creado es: " + nueNombre, nueApellido + " con año de nacimiento en " + NueAnioNac + " y direccion en " + direccion)
    numTarjeta()
    
    if(nueNombre == nombre):
        print("Ya tienes una tarjeta registrada, se ha añadido a tu cuenta.")
    else:
        input("Pulse Enter para continuar...")
        return clientes, noCuentas

# Crear nueva cuenta
cuentaCreada = [] 
def numTarjeta():
    numCard = ""
    for i in range(6):
        numCard += str(random.randrange(0,10))
    cuentaCreada.append(numCard)
    print("Tu número de tarjeta es: ", numCard + " y su saldo actual es de: ", saldo)
    print(cuentaCreada)
    numSeg = input("Digite un NIP para su tarjeta: ")

def deposito(saldo):
    print("Procederemos a hacer un depósito a tu cuenta bancaria.\n")
    user = input("¿Cuál es su nombre?: ")
    tarjeta = int(input("Digite el número de su tarjeta: "))
    print(user)
    print(tarjeta)
    cantidad = float(input("Digite la cantidad que desea añadir a su cuenta: "))
    saldo += cantidad
    print("\nCantidad depositada: ", cantidad)
    print("Su saldo final ", saldo)

    if saldo >= 100000:
        print("Tienes cuenta Premium:)\n")
    else:
        print("Tu cuenta es estándar.\n")
    

def retiro():
    print("Procederemos a hacer un retiro se su cuenta bancaria.\n")
    user = input("¿Cuál es su nombre?: ")
    tarjeta = int(input("Digite el número de su tarjeta: "))
    print(user)
    print(tarjeta)
    wd = float(input("Digite la cantidad que desea retirar: "))
    if saldo >= wd:
        saldo -= wd
        print("\nTu retiro es: ", wd)
    else:
        print("\nNo tienes dinero suficiente para el retiro :(")

    if saldo <= 100000:
        print("Tu cuenta sigue siendo premium.")
    else:
        print("Tu cuenta ahora es estándar.")
   
def mostrarSaldo(saldo):
    print("\nTu saldo disponible neto: ", saldo)


print("------------------------------------------------------------")


print("\nBienvenido a tu banco :)\n")

op = 0
while op != 5:
    print("\nLas posibles opciones dentro de este módulo son: ")
    print("\t1. Crear nuevo cliente.")
    print("\t2. Modificar datos de cliente.")
    print("\t3. Crear una nueva cuenta.")
    print("\t4. Operaciones bancarias.")
    print("\t5. Salir.")

    op = int(input("\nDigita la opción que desees para este módulo: "))

    if op == 1:
        print("\nHarás la creación de un nuevo cliente.")
        crearCliente(id, clientes, noCuentas)
        id += 1

    if op == 2:
        print("\nModificarás tus datos de cliente.")
        modCliente()

    if op == 3:
        print("\nCrearás una nueva cuenta bancaria.")
        crearCuenta(nombre)

    if op == 4:
        print("\nHa entrado a operaciones bancarias.")
        print("Para este módulo pediremos tu número de tarjeta dado y tu NIP.\n")

        tarjOsh = int(input("Ingresa el número de tu tarjeta: "))
        nipSeg = input("Digita tu NIP correctamente: ")

        # intentos = 0
        # while intentos < 3:
        #     nipSeg = input("Digita tu NIP correctamente: ")
        #     try:
        #         nipSeg = int(nipSeg)
        #     except ValueError:
        #         print("Debes ingresar un valor entero.")
        # print("Has ingresado erroneamente tus datos 3 veces, cuenta bloqueada.")
        
        if nipSeg == nipSeg:
            opBanc = 0
            while opBanc != 5:
                print("Las opciones posibles dentro de este módulo son: ")
                print("\t1. Consultar saldo.")
                print("\t2. Hacer retiros.")
                print("\t3. Hacer depósitos.")
                print("\t4. Generar reporte de cuenta.")
                print("\t5. Salir.")

                opBanc = int(input("\nDigita la opción deseada para este módulo: "))

                if opBanc == 1:
                    print("---")

                if opBanc == 2:
                    retiro()

                if opBanc == 3:
                    deposito(saldo)

                if opBanc == 4:
                    mostrarSaldo()
        else:
            print("Por favor digita tus datos de forma correcta.")