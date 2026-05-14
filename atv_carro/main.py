from car.Carro import Carro
from moto.Moto import Moto

if __name__ == "__main__":
    carro = Carro("Toyota", "Corolla", 2020)
    moto = Moto("Yamaha", "MT-07", 2021, 689)

    print(f"Modelo: {carro.modelo}, Ano: {carro.ano}")
    print(f"IPVA: {carro.calc_ipva()}")
    print(f"Desconto: {carro.desconto()}")

    print(f"Modelo: {moto.modelo}, Ano: {moto.ano}, Cilindrada: {moto.cilindrada}cc")
    print(f"IPVA: {moto.calc_ipva()}") 