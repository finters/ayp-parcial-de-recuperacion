from cliente import cliente
from paquete import paquete

class envio(cliente,paquete):
    def __init__(self):
        self.direccion=cliente.direccion
        self.peso=paquete.peso


    def calculadorEnvio(self):
        if self.peso<=7 and self.direccion=="districo captital":
            self.vehiculo="moto"
            self.costo=self.peso*2
            self.costo+=self.costo*0.35

        elif self.peso>7 and self.direccion=="districo captital":
            self.vehiculo="carro"
            self.costo=self.peso*3
            self.costo+=self.costo*0.35            

        elif self.direccion!="districo captital":
            self.vehiculo="van"
            self.costo=self.peso*4.5
            self.costo+=self.costo*0.35
            
        