'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

import random as r
import time

class AireAcondicionado:
    
    def __init__ (self, marca, sensorMarca):
        self.estado=0
        self.marca=marca
        self.obj_sensor=Sensor(sensorMarca)
        self.estado="Apagado"
    
    def prender(self):
        self.estado="Prendido"
        
    def apagar(self):
        self.estado="Apagado"
        
    def get_temperatura(self):
        return self.temperatura
        
    def monitorear(self, obj_habitacion):
        
        temperatura=self.obj_sensor.obtener_temp(obj_habitacion)
        humedad=self.obj_sensor.obtener_humedad(obj_habitacion)
        
        if((temperatura>28 and humedad>60) or temperatura>30):
            self.prender()
        else:
            self.apagar()
            
        print("Escaneo completado, \n-Temperatura actual de "+str(temperatura)+" c°")
        print("-Humedad actual de la habitacion= "+str(humedad)+"%")
        print("-Estado del Aire Acondicionado= "+self.estado)

class Habitacion:
    
    def __init__(self, nombre):
        self.nombre=nombre
        self.temp=0
        self.humedad=0
        
    def get_temperatura(self):
        self.temp=r.randint(15,36)
        return self.temp
        
    def get_humedad(self):
        self.humedad=r.randint(1,100)
        return self.humedad
        
    def set_temperatura(self, temp):
        self.temp=temp
        
    
        
class Sensor:
    
    def __init__(self, marca):
        self.marca=marca
        self.tempDetec=0
        
    def obtener_temp(self, obj_habitacion):
        return obj_habitacion.get_temperatura()
        
    def obtener_humedad(self, obj_habitacion):
        return obj_habitacion.get_humedad()
        
        
#-----------------Codigo principal--------------------------


obj_habitacion=Habitacion("Sala de estudio")
obj_aire_acond=AireAcondicionado("Mabe", "Toshiba")

seguir=True
print("Bienvenido, a continuacion se empezara el monitoreo")

while(seguir):
    obj_aire_acond.monitorear(obj_habitacion)
    time.sleep(5)
    
    