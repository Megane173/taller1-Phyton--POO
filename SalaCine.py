class sala_cine:

    def __init__(self, asientos, pelicula):
        self.asientos= [False] * asientos
        self.pelicula=pelicula

    def imprimir_msg(self, txt):
        print(txt)
        
    def menu(self):
        seguir=True
        while(seguir):
            eleccion=input("-----------------------\nMENU\n1. Digite 1 para reservar un asiento\n2. Digite 2 para ver los asientos disponibles\n3. Digite 3 para salir\n")
            if(eleccion=="1"):
                self.reservar_asientos()
            elif(eleccion=="2"):
                self.imprimir_disponible()
            elif(eleccion=="3"):
                seguir=False
            
        
    def imprimir_disponible(self):
        msg=""
        for i in range(0, len(self.asientos)):
            if(self.asientos[i]==False):
                msg+="["+str(i+1) +"-disponible]"
            else:
                msg+="["+str(i+1) +"-ocupado]"
            if((i+1)%5==0):
                    msg+="\n"
            
        self.imprimir_msg(msg)
    
    def reservar_asientos(self):
        
        seguir= True
        while(seguir):
            reserv= int(input("Digite el asiento que quiere reservar, teniendo en cuenta que hay "+str(len(self.asientos))+" asientos: "))-1

            if(self.asientos[reserv]==True):
                self.imprimir_msg("Error: Ese asiento ya esta reservado\n")
            else:
                #Se reserva el asiento
                self.asientos[reserv] = True
                self.imprimir_msg("El asiento "+str(reserv)+" fue reservado con exito \n")
                #Se verifica si el usuario quiere seguir reservando asientos
                desicion= input("Digite 1 si quiere seguir reservando asientos: ")
                if(desicion != "1"):
                    seguir= False
    
    def getAsientos(self):
        return len(self.asientos)
    
    def getPelicula(self):
        return self.pelicula
            

#************** Codigo principal ***************************

sala = sala_cine(35,"Superman")
n_asientos= sala.getAsientos()
nom_pelicula= sala.getPelicula()
sala.imprimir_msg("Bienvenido, nuestra sala tiene "+str(n_asientos)+" asientos y esta proyectando la pelicula "+nom_pelicula)
sala.menu()
sala.imprimir_msg("\nSalida con exito, gracias por visitar nuestro cine")
