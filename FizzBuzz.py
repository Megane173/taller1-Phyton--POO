class Calculadora:
    
    def __init__(self, marca):
        self.marca=marca
        
    def isFizzBuzz(self, numero):
        
        if(numero%3==0 and numero%5==0):
            return "FizzBuzz"
        elif(numero%3==0):
            return "Fizz"
        elif(numero%5==0):
            return "Buzz"
        
        return str(numero)
    
    #-----------Codigo principal-----------
    
    
obj_calculadora=Calculadora("casio")
msg=""

for i in range(100):
    
    msg+=" "+obj_calculadora.isFizzBuzz(i+1)
    
print(msg)