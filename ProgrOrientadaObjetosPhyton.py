class saludo:
    #Metodo constructor 
    #Se usa para inicializar obj

    def __init__(self, dato_texto):
        self.mensaje= dato_texto 
        print(self.mensaje)

    def tomar_nombre(self):
        nombre_usuario=input("Escribe el nombre del usuario: ")
        return nombre_usuario
    
    def hacer_mensaje(self, dato_usuario):
        self.mensaje = "Hola usuario "+dato_usuario
        self.imprimir_mensaje(self.mensaje)
    
    def imprimir_mensaje(self, mensaje):
        print(mensaje)

    #Getter
    def get_mensaje(self):
        return self.mensaje
    
    #Setter
    def set_atributo(self, dato_nuevo_mensaje):
        self.mensaje = dato_nuevo_mensaje


    #***************************** Codigo principal *************************************

texto= "Hola Usuario"
#Se crea una instancia de saludo, con el constructor (que no es obligatorio siempre)
obj_mensaje = saludo(texto) 
#Se usa un metodo de la clase saludo
nombre_usuario = obj_mensaje.tomar_nombre()
#Metodo de funcion anidada que imprime mensaje
obj_mensaje.hacer_mensaje(nombre_usuario)