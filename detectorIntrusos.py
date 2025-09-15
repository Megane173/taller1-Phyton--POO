import random as r
import time 

class Sensor:
    
    def __init__ (self, marca, nombre):
        self.estado=0
        self.marca=marca
        self.nombre=nombre

        
    def escanear_zona(self):
        return r.randint(0,1)
    
    def imprimir_deteccion(self, deteccion_actual):
        if(deteccion_actual):
            print("Se ha detectado algo en "+self.nombre)
        else: 
            print("No se ha detectado nada en "+self.nombre)
        
class Alarma:
    
    def __init__ (self, marca):
        self.estado="Apagado"
        self.marca=marca
    
    def prender(self):
        self.estado="Prendido"
        print("\n-La alarma se ha prendido")
        
    def apagar(self):
        self.estado="Apagado"
        print("\n-La alarma se ha apagado")
        
#------------Codigo Principal------------------


obj_sensor1=Sensor("Schigun", "sensor 1")
obj_sensor2=Sensor("Schigun", "sensor 2")
obj_sensor3=Sensor("Schigun", "sensor 3")
obj_alarma=Alarma("Schigun")
seguir=True
print("Bienvenido, a continuacion se empezara el monitoreo")

while(seguir):
    
    estado_dia=r.randint(0,1)#0noche y 1dia
    
    act_sensor1=obj_sensor1.escanear_zona()
    act_sensor2=obj_sensor2.escanear_zona()
    act_sensor3=obj_sensor3.escanear_zona()
    
    if(estado_dia==0 and (act_sensor1+act_sensor2+act_sensor3)>1):
        obj_alarma.prender()
    
    obj_sensor1.imprimir_deteccion(act_sensor1)
    obj_sensor2.imprimir_deteccion(act_sensor2)
    obj_sensor3.imprimir_deteccion(act_sensor3)
    
    desicion=input("\nDigite un 1 en caso de que quiera prender la alarma, o digite un 0 si quiere apagar la alarma: ")
    if(desicion=="1"):
        obj_alarma.prender()
    elif(desicion=="0"):
        obj_alarma.apagar()
    
    time.sleep(2.5)
    
    