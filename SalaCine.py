class sala_cine:

    def __init__(self, asientos, pelicula):
        self.boolean(asientos[asientos])
        self.pelicula=pelicula

    def imprimir_msg(txt):
        print(txt)

    def imprimir_disponible(self):
        msg=""
        for i in range(0, self.asientos.length-1):
            if(self.asientos[i]==False):
                msg+="El asiento "+ i +" esta disponible\n"
            
        self.imprimir_msg(msg)
    
    def reservar_asientos(self, asiento):
        
        seguir= True
        while(seguir):
            reserv= int(input("Digite el asiento que quiere reservar, teniendo en cuenta que hay "+self.asientos.length+" asientos"))

            if(self.asientos[reserv]==True):
                self.imprimir_msg("El asiento ya esta reservado")
            else:
                #Se reserva el asiento
                self.asientos[reserv] = True
                self.imprimir_msg("El asiento "+reserv+" fue reservado con exito")
                #Se verifica si el usuario quiere seguir reservando asientos
                desicion= input("Digite 1 si quiere seguir reservando asientos")
                if(desicion != 1):
                    seguir= False
            







#************** Codigo principal ***************************

sala = sala()
