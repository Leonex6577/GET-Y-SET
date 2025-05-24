class Cuenta_banco:
    def __init__ ( self, __nombre, __saldo):
        self.__nombre = __nombre
        self.__saldo = __saldo
        
    def get_saldo(self):
        print(self.__saldo)
        
    def set_saldo(self, saldo):
        self.__saldo = saldo
        
    def get_nombre(self):
        print(self.__nombre)
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
cuenta_1 = Cuenta_banco("angel", 10000)

cuenta_1.get_saldo()

cuenta_1.set_saldo(5000)

cuenta_1.get_saldo()

cuenta_1.get_nombre()

cuenta_1.set_nombre("Roni")

cuenta_1.get_nombre()