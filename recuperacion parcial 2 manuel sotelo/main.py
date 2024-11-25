from cliente import cliente
from paquete import paquete
from envios import envio


def add_client():
    nombre=   input("ingrese el nombre del cliente: ")
    apellido= input("ingrese el apellido del cliente: ")
    id=       input("ingrese el numero de cedula del cliente: ")
    direccion=input("ingrese el estado de envio: ").lower()
    telefono= input("ingrese el telefono del cliente: ")
    return cliente(nombre,apellido,id,direccion,telefono)

def tipo_de_paquete():
    peso:float=input("ingrese el peso del paquete en KG")
    return paquete(peso)

while True:
    response=input(""" bienvenido, que desea hacer?
1.calcular envio
0. salir
""")
    if int(response) == 0:
        break
    else:
        pass
    client=add_client()
    package=tipo_de_paquete()
    data_envio=envio(client,package)

    