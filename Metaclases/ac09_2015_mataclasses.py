from random import randint, choice

__author__ = 'figarrido'


NOMBRES = ['Karim', 'Christian', 'Belen', 'Patricio', 'Jaime',
           'Marco', 'Rodrigo', 'Felipe', 'Antonio', 'Ian']

TAREAS = ['Hacer el papeleo', 'Depositar los sueldos',
          'Descansar', 'Comer', 'Tomar cafe',
          'Organizar la reunion', 'Agregar datos al sistema',
          'Jugar con las sillas', 'Revisar CV\'s',
          'Marcar entrada']


def nuevo_empleado(self, employee):
    if isinstance(employee, Empleado):
        self.empleados[employee.id_empleado] = employee


def subir_sueldo(self, id_empleado, password):
    if self.boss.password == password:
        self.empleados[id_empleado].sueldo *= 2


def hacer_tarea(self, task):
    print('{} debe realizar {}'.format(self.nombre, task))
    print('Realizando tarea')
    print('Tarea finalizada')


class MetaEmpresa(type):
    def __new__(meta, nombre, base, classdict):
        if nombre != 'Empresa':
            raise NameError('El nombre esta malo')

        if nuevo_empleado.__name__ not in classdict:
            classdict[nuevo_empleado.__name__] = nuevo_empleado

        if subir_sueldo.__name__ not in classdict:
            classdict[subir_sueldo.__name__] = subir_sueldo

        return super().__new__(meta, nombre, base, classdict)

    def __call__(cls, *args, **kwargs):
        if 'empresa' in kwargs:
            empresa = kwargs['empresa']
            amount = sum([emp.sueldo for emp in empresa.empleados.values()])
            return 'El sueldo total es de {}'.format(amount)
        else:
            return super().__call__(*args, **kwargs)


class MetaPersona(type):
    def __new__(meta, nombre, base, classdict):
        if nombre not in ['Persona', 'Empleado', 'Jefe']:
            raise NameError('El nombre esta malo')

        classdict['__call__'] = hacer_tarea

        return super().__new__(meta, nombre, base, classdict)


class Empresa(metaclass=MetaEmpresa):

    def __init__(self, boss):
        self.boss = boss
        self.empleados = {}


class Persona(metaclass=MetaPersona):

    def __init__(self, nombre, edad, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return '{} is {} years old'.format(self.nombre, self.edad)


class Empleado(Persona):

    id_actual = 0

    def __init__(self, sueldo, **kwargs):
        super().__init__(**kwargs)
        self.sueldo = sueldo
        self.id_empleado = Empleado.id_actual
        Empleado.id_actual += 1
        self.tareas_realizadas = []

    def __str__(self):
        return super().__str__() + '\nID: {} - Sueldo: {}'.format(self.id_empleado, self.sueldo) + '\n'


class Jefe(Empleado):

    def __init__(self, **kwargs):
        self.password = 'Tu jefecito lindo'
        super().__init__(**kwargs)

if __name__ == '__main__':

    System = Empresa(Jefe(nombre='Pedro', edad=30, sueldo=1000000))

    """
    Agrega 10 empleados en la empresa
    """
    for _ in range(10):
        System.nuevo_empleado(Empleado(nombre=NOMBRES[_], edad=randint(20, 40),
                                       sueldo=randint(500000, 800000)))
    """
    Muestra a los empleados
    """
    for ID in System.empleados:
        print(System.empleados[ID])

    """
    Elige al azar al empleado del mes
    """
    empleado_del_mes = System.empleados[choice(list(System.empleados))]

    System.subir_sueldo(empleado_del_mes.id_empleado, 'Tu jefecito lindo')

    print('El empleado del mes es: {} y su sueldo quedo en ${}\n'.format(
        empleado_del_mes.nombre, empleado_del_mes.sueldo))

    """
    A cada empleado le asigna una tarea
    """
    for ID in System.empleados:
        System.empleados[ID](choice(TAREAS))

    print(Empresa(empresa=System))
