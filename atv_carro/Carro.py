from veiculo.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, ano, preco):
        super().__init__(modelo, ano, preco)
    
    def desconto(self):
        return self.preco * 0.5

  