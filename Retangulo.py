class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcula_area(self) :
        return self.base * self.altura

r1 = Retangulo(12,24) ## Instancia do Objeto 
print(r1.base)    
print(r1.altura)

r2 = Retangulo(8,12)


x = r1.calcula_area()
y = r2.calcula_area()
print("Area é: ",x)
print("Area é: ",y)
        
## self é pra acessar o atributo da classe        