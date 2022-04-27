from veiculo import Veiculo
#Usando Veiculo como classe Pai
class Carro(Veiculo):
    def __init__(self, cor, rodas, marca, tanque):
        Veiculo.__init__(self, cor, rodas, marca, tanque)

    def abastecer(self,litros):
        #Mostrando erro se o valor no tanque for maior que o limite.
        #Esse erro só existe na classe Carro, não em veículos.
        #O Carro só "herda" os outros valores/parâmetros do pai
        if self.tanque + litros > 50:
            print("Erro: Não vai caber não, mano.")
        else:
            self.tanque += litros