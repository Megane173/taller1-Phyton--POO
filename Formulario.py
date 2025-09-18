import tkinter as Ventana

class Formulario:

    def __init__(self):
        self.colorRojo="red"
        self.colorAmarillo="yellow"
        self.entryNombre=" "
        self.entryEdad=" "
        self.entryEmail=" "
        self.entryTelefono=" "
        self.entryDireccion=" "
        self.labelResultado=" "
        self.formulario=" "

    def iniciar_ventana(self):
        self.formulario=Ventana.Tk()
        self.formulario.title("Registro de cliente.")
        self.formulario.geometry("800x800")
        self.formulario.resizable(False, False)
        self.formulario.configure(bg="grey")
        self.formulario.configure(cursor="hand2")
        return self.formulario

    def iniciar_preguntas(self):

        labelNombre=Ventana.Label(self.formulario, text="Digite el nombre del cliente: ")
        labelNombre.configure(bg="white", fg="blue", font=("Arial", 14, "bold"))
        labelNombre.configure(borderwidth=2, relief="raised", width=30, height=1)
        labelNombre.configure(padx=10, pady=10, anchor="w")
        labelNombre.pack()

        self.entryNombre=Ventana.Entry(self.formulario)
        self.entryNombre.configure(bg="white", fg="black", font=("Arial", 16, "bold"), width=30)
        self.entryNombre.pack(padx=10, pady=10)

        labelEdad=Ventana.Label(self.formulario, text="Digite la edad del cliente: ")
        labelEdad.configure(bg="white", fg="blue", font=("Arial", 14, "bold"))
        labelEdad.configure(borderwidth=2, relief="raised", width=20, height=1)
        labelEdad.configure(padx=10, pady=10, anchor="w")
        labelEdad.pack()

        self.entryEdad=Ventana.Entry(self.formulario)
        self.entryEdad.configure(bg="white", fg="black", font=("Arial", 16, "bold"), width=30)
        self.entryEdad.pack(padx=10, pady=10)


        labelEmail=Ventana.Label(self.formulario, text="Digite el email del cliente: ")
        labelEmail.configure(bg="white", fg="blue", font=("Arial", 14, "bold"))
        labelEmail.configure(borderwidth=2, relief="raised", width=20, height=1)
        labelEmail.configure(padx=10, pady=10, anchor="w")
        labelEmail.pack()

        self.entryEmail=Ventana.Entry(self.formulario)
        self.entryEmail.configure(bg="white", fg="black", font=("Arial", 16, "bold"), width=30)
        self.entryEmail.pack(padx=10, pady=10)

        labelTelefono=Ventana.Label(self.formulario, text="Digite el telefono del cliente: ")
        labelTelefono.configure(bg="white", fg="blue", font=("Arial", 14, "bold"))
        labelTelefono.configure(borderwidth=2, relief="raised", width=30, height=1)
        labelTelefono.configure(padx=10, pady=10, anchor="w")
        labelTelefono.pack()

        self.entryTelefono=Ventana.Entry(self.formulario)
        self.entryTelefono.configure(bg="white", fg="black", font=("Arial", 16, "bold"), width=30)
        self.entryTelefono.pack(padx=10, pady=10)

        labelDireccion=Ventana.Label(self.formulario, text="Digite la direccion del cliente: ")
        labelDireccion.configure(bg="white", fg="blue", font=("Arial", 14, "bold"))
        labelDireccion.configure(borderwidth=2, relief="raised", width=30, height=1)
        labelDireccion.configure(padx=10, pady=10, anchor="w")
        labelDireccion.pack()

        self.entryDireccion=Ventana.Entry(self.formulario)
        self.entryDireccion.configure(bg="white", fg="black", font=("Arial", 16, "bold"), width=30)
        self.entryDireccion.pack(padx=10, pady=10)

        botonEnviar = Ventana.Button(self.formulario, text="Enviar", font=("Arial", 16, "bold"), command=self.tomar_datos)
        botonEnviar.configure(bg="blue", fg="white", width=30)
        botonEnviar.pack(padx=10, pady=30)


    def tomar_datos(self):
        aux_dato=self.entryNombre.get()
        self.imprimir_datos(aux_dato)

    def imprimir_datos(self, aux_dato):
        labelResultado = Ventana.Label(self.formulario, text=aux_dato)
        labelResultado.configure(bg = self.colorAmarillo)
        labelResultado.pack(padx=10, pady=10)