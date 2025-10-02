class Produto:
    def __init__(self,nome,marca,modelo,preco):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.__inicia_prod()
        

    def mostrar_dados(self): ## METODO GET
        return f' Nome: {self.nome} | Marca: {self.marca} | Modelo: {self.modelo} | Preço: {self.preco}'
        
    def __inicia_prod(self): ## METODO PRIVADO
        print("Produto Inicializado com Sucesso!")

        
if __name__ == "__main__":
    prod1 = Produto("Notebook","Dell","Core i9",9000)
    print("Executando do proprio Arquivo")
    
