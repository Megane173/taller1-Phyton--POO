import random as r
import time

class SensorTemperatura:
    
    def __init__ (self, marca):
        self.temperatura=0
        self.marca=marca
    
    def get_temperatura(self):
        self.escanear_temp()
        return self.temperatura
        
    def escanear_temp(self):
        self.temperatura=r.randint(-5,34)
        
class Controlador:
    
    def __init__(self, propietario):
        self.propietario=propietario
        
        
    def monitorear(self, obj_sen_tem, obj_ventilador, obj_calefac):
        temperatura=obj_sen_tem.get_temperatura()
        
        if(temperatura<10):
            if(obj_calefac.get_estado()=="Apagado"):
                obj_calefac.prender()
            if(obj_ventilador.get_estado()=="Prendido"):
                obj_ventilador.apagar()
        elif(temperatura>25):          
            if(obj_ventilador.get_estado()=="Apagado"):
                obj_ventilador.prender()
            if(obj_calefac.get_estado()=="Prendido"):
                obj_calefac.apagar()
        else:
            obj_calefac.apagar()
            obj_ventilador.apagar()
        
        print("Escaneo completado, \n-Temperatura actual de "+str(temperatura)+" c°")
        print("-Estado de ventilador= "+obj_ventilador.get_estado())
        print("-Estado de calefactor= "+obj_calefac.get_estado())
        
        
            
        
class Calefactor:
    
    def __init__(self, marca):
        self.marca=marca
        self.estado="Apagado"
        
    def get_estado(self):
        return self.estado
    
    def prender(self):
        self.estado="Prendido"
        
    def apagar(self):
        self.estado="Apagado"
    
class Ventilador:
    
    def __init__(self, marca):
        self.marca=marca
        self.estado="Apagado"
        
    def get_estado(self):
        return self.estado
    
    def prender(self):
        self.estado="Prendido"
        
    def apagar(self):
        self.estado="Apagado"
        
#-----------------Codigo principal--------------------------


obj_controlador=Controlador("Fermin")
obj_calefac=Calefactor("Mabe")
obj_ventilador=Ventilador("Samurai")
obj_sen_tem=SensorTemperatura("Wattco")

seguir=True
print("Bienvenido, a continuacion se empezara el monitoreo")

while(seguir):
    obj_controlador.monitorear(obj_sen_tem, obj_ventilador, obj_calefac)
    time.sleep(5)