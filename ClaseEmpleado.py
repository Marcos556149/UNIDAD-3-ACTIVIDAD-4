class Empleado:
    __DNI= ''
    __nombre= ''
    __direccion= ''
    __telefono= ''
    def __init__(self,dn='',nom='',dir='',tel=''):
        self.__DNI= dn
        self.__nombre= nom
        self.__direccion= dir
        self.__telefono= tel
    def getSueldo(self):
        pass
    def getDNI(self):
        return self.__DNI
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
