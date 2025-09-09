import random as r
import time 

class SistemaDomotico:
    
    def __init__(self,propietario):
        self.propietario=propietario
        
    def controlar_luz(self, obj_luz, hora, movimiento):
        
        estado_dia=""
        print("Inicio de control,")
        
        #Las 8Pm en adelante se considera de noche
        #Y las 6Am en adelante se considera dia
        if(hora>=20 or hora<6):
            estado_dia="noche"
        else:
            estado_dia="dia"
            
        
        if(estado_dia=="noche" and movimiento):
            obj_luz.prender()
        elif((estado_dia=="dia") or not movimiento):
            obj_luz.apagar()
        
        valorMov="" if movimiento else "no"
        print("Es de "+estado_dia+" y "+valorMov+" se detecto movimiento")
        print("Las luces se encuentran "+obj_luz.get_estado()+"\n")   
            
    
class Luz:
    
    def __init__(self, tipo, marca):
        self.tipo=tipo
        self.marca=marca
        self.estado="Apagado"
        
    def get_estado(self):
        return self.estado
    
    def prender(self):
        self.estado="prendidas"
        
    def apagar(self):
        self.estado="apagadas"
        
#----------Codigo principal--------------------

obj_luz=Luz("led", "Osram")
obj_sistem_Domot=SistemaDomotico("Wilson")

seguir=True
print("Bienvenido, a continuacion se empezara el monitoreo de la luz de la casa")

while(seguir):
    obj_sistem_Domot.controlar_luz(obj_luz, r.randint(1,24), r.randrange(2))
    time.sleep(10)        
        
    