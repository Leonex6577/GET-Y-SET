#TAPIA HERNANDEZ JOSE ALEJANDRO
class Computadoras:
    __cpu = "Ryzen_6500"
    __tarjeta_grafica = "Nvidia_1660"
    __placa_madre = "Asus"

gaimer = Computadoras()
print(gaimer.__cpu)
gaimer.__cpu = "Intel Core i9"
print(gaimer.__cpu)

print(gaimer.__tarjeta_grafica)
gaimer.__tarjeta_grafica = "Nvidia_6090"
print(gaimer.__tarjeta_grafica)

print(gaimer.__placa_madre)
gaimer.__placa_madre = "Asus pro"
print(gaimer.__placa_madre)
#ESTE ES SIMILAR PERO DISTINTO A SER VARIABLES ESTATICOS, DEJANDO DESDE EL INICIO QUE SIGNIFICARAN LAS VARIABLES DE LA CLASE COMPUTADORAS CREANDO EL OBJETO QUE LA TENGA Y LUEGO PODER CAMBIARLOS DE MANERA MAS SENCILLA
