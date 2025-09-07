class Calculador:
    
    def __init__(self, marca,color):
        self.marca=marca
        self.color=color
    
    def get_marca(self):
        return self.marca
    def get_color(self):
        return self.color
    
    def set_marca(self, marca):
        self.marca=marca       
    def set_color(self, color):
        self.color=color
            
    def sumar(self,a, b):
        return a+b
    
    def restar(self,a, b):
        return a-b
    
    def multiplicar(self,a, b):
        return a*b
    
    def dividir(self,a,b):
        return a/b
    
#------------------Codigo principal----------------------

calculadora= Calculador("casio", "gris")

seguir=True
print("Bienvenido, a la calculadora, aqui podra hacer operacion con dos numeros.")
print("A continuacion estan los numeros que debe presionar para usar la calculadora\n")
while(seguir):
    
    operacion=input("1 para sumar\n2 para restar\n3 para multiplicar\n4 para dividir\n5 para SALIR\n-")
    if(operacion=="5"):
        seguir=False
    else:
        a=int(input("\nDigite el primer digito: "))
        b=int(input("Digite el segundo digito: "))  
        if(operacion=="1"):
            resultado=calculadora.sumar(a,b)
        elif(operacion=="2"):
            resultado=calculadora.restar(a,b)
        elif(operacion=="3"):
            resultado=calculadora.multiplicar(a,b)
        elif(operacion=="4"):
            resultado=calculadora.dividir(a,b)
        
        print(f"El resultado es {resultado:.2f}\n")
