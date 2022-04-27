#Criando uma classe.
class Veiculo():
    #O método init passa ele mesmo como parâmetro, é o construtor da Classe (Objeto)
    def __init__(self, cor, rodas, marca, tanque):
        #Definindo as variáveis dentro de SELF (Objeto)
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
#SEMPRE AO CRIAR UM MÉTODO NA CLASSE TEM QUE USAR O SELF COMO PARÂMETRO, NÃO ESQUECER
    def abastecer(self, litros):
        self.tanque += litros # aumentando o valor do tanque com o valor de litros passados.
        return self.tanque