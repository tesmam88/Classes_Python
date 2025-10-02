class Triangulo:
    def __init__(self,base:int,altura:int):
        self.__base = base  ##Private encapsulamento
        self.__altura = altura

    def calcular_area(self) -> float:
        area = (self.base * self.altura) / 2
        return area
    
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
    
    def set_altura(self,nova_altura:float):
        self.__altura =  nova_altura
    
t1 = Triangulo(9,15)
t2 = Triangulo(4,6)

t1.set_altura(55)
print(t1.set_altura)

