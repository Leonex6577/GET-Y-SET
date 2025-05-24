#Tapia Hernandez Jose Alejandro
class Computadoras:
    def __init__ (self, __cpu, __tarjeta_video, __placa_madre ):
        self.__cpu = __cpu
        self.__tarjeta_video = __tarjeta_video
        self.__placa_madre = __placa_madre
        
    def get_cpu(self):
        print(self.__cpu)
    
    def get_tarjeta_video(self):
        print(self.__tarjeta_video)
        
    def get_placa_madre(self):
        print(self.__placa_madre)
        
    def set_cpu(self, cpu):
        self.__cpu = cpu
        
    def set_tarjeta_video(self, tarjeta_video):
        self.__tarjeta_video = tarjeta_video
    
    def set_placa_madre(self, placa_madre):
        self.__placa_madre = placa_madre
        
gaimer = Computadoras("Ryzen 2600", "nvidia1660", "Asus")

gaimer.get_cpu()

gaimer.set_cpu("Intel i9")

gaimer.get_cpu()

gaimer.get_tarjeta_video()

gaimer.set_tarjeta_video("Nvidia5090")

gaimer.get_tarjeta_video()

gaimer.get_placa_madre()

gaimer.set_placa_madre("Asus Pro")

gaimer.get_placa_madre()