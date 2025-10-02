class Cachorro:
    def __init__(self,nome,peso,cor):
        self.nome = nome
        self.peso = peso
        self.cor = cor

    def latir(self):
        print(f'{self.nome} AU AU AU') 

    def comer(self):
        print(f'{self.nome} comendo...')   

dog1 = Cachorro("Pingo",15,"branca")
dog2 = Cachorro("Zeus",10,"preto")

print("O cachorro pesa ",dog1.peso)
dog1.peso = 20
dog1.latir()
dog1.comer()
print("O cachorro pesa ",dog1.peso)
dog2.latir()
        