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

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


if __name__ == '__main__':
    objPersona1 = Persona(nombre='Karla', apellido='Paz', edad=15, cedula='0123456789', correo='kperez@mail.com')
    print(objPersona1.__str__())

    # print(objPersona1._apellido)
    # print(objPersona1._edad)
    # objPersona1._nombre = 'Maria'
    # print(objPersona1._nombre)
    print(objPersona1.nombre)
    objPersona1.nombre = 'Fernanda'
    print(objPersona1.nombre)
    # print(objPersona1._nombre)