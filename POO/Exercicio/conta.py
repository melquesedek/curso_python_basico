#Criando a classe Conta. Que será a conta do cliente
class Conta:
    #Recebemos o cliente, o saldo e o limite que ele possui.
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite
    #Método para depositar dinheiro. Só se for depositado mais que zero.
    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print("Foi depositado:", quant)
        else:
            print("Erro no deposito")
    #Método que exibe o saldo
    def consulta_saldo(self):
        return self.saldo
    #Método para tirar o dinheiro
    def sacar(self, quant):
        if self.saldo - quant < self.limite:
            print("Saldo insuficiente")
        else:
            self.saldo -= quant
            print("Foi sacado:", quant)