from veiculo.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calc_ipva(self):
        return self.preco * 0.5
  