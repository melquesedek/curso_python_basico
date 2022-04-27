class Cliente:
    #Criando classe Cliente e definindo os parâmetroa
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        #Retornando a string com os dados para printar na tela. O método STR é que retorna os textos
        return "Nome: " + self.nome + "\nCPF: " + self.cpf + "\nIdade: " + str(self.idade)