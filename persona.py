class Persona:

    def __init__(self, nombre:str, apellido:str, cedula:str, correo:str, edad:int = None, vip:bool = False, fecha_nacimiento= None):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._cedula = cedula
        self._correo = correo
        self._vip = vip
        self._fecha_nacimiento = fecha_nacimiento

    # def __str__(self):
    #     return (f'Persona [nombre: {self._nombre}, apellido: {self._apellido}, '
    #             f'cedula: {self._cedula}, correo: {self._correo}, edad={self._edad}, vip? def __str__(self):
    #         return f'Persona {self.__dict__.__str__()}':{self._vip}, '
    #             f'fecha_nacimiento: {self._fecha_nacimiento}]')

    def __str__(self):
        return f'Persona {self.__dict__.__str__()}'




if __name__ == '__main__':
    objPersona1 = Persona(nombre='Karla', apellido='Paz', edad=15, cedula='0123456789', correo='kperez@mail.com')
    print(objPersona1.__str__())
    print(objPersona1._nombre)
    print(objPersona1._apellido)
    print(objPersona1._edad)

    p2 = Persona(nombre='Armando', cedula='0125874693', apellido='Perez', edad=20, correo='aperez@mail.com')
    print(p2)
    print(p2._nombre)
    print(p2._apellido)
    print(p2._edad)

    p3 = Persona('Luis', 'Perez', '9876543120', 'lperez@mail.com', vip=True)
    print(p3._nombre)
    print(p3._correo)
    print(p3._vip)

    p4 = Persona(nombre='Maria', apellido='Paz', correo='mpaz@mail.com', edad='cinco', cedula='0123456789')
    print(p4._edad)

    p5 = Persona(nombre='M', apellido='L', correo='g', cedula='5')
    print(p5)
