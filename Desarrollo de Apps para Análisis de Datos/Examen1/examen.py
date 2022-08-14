"""1. Los atributos de los objetos deben ser capturadores en el respectivo constructor. Ejemplo: input("Proporciona el ID de empleado: ").
2. Deben existir dos tipos de empleados: Sustancial y de Apoyo. Los primeros deben tener un salario de $30,000 y los segundos de $20,000."""

class Empleado():

    def __init__(self):

        self.id = input("Proporciona el ID del empleado: ")
        self.profesion = input("Proporciona la profesión del empleado: ")
        self.salario = 30000
        self.tipo = input("Qué tipo de empleado eres: ")
        if self.tipo == "Sustancial":
            self.salario
        else:
            self.salario - 10000


class Persona(Empleado):

    def __init__(self):
        Empleado.__init__(self)
        self.curp = input("Proporcione su CURP: ")
        self.nombre = input("Proporciona su nombre: ")


class Empresa(Empleado):

    def __init__(self):
        Empleado.__init__(self)
        self.nombreEm = input("Proporcione el nombre de la empresa: ")
        self.industria = input("Proporcione la industria: ")


emp = Empleado()
per = Persona()
fab = Empresa()