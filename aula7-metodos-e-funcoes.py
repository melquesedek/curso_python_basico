#Criando funções. Para quem já programa, vida que segue, se não souber o que é função é sacanagem.
#Mas caso não saiba, são comandos prontos que aceitam poucos parâmetros para fazer o trabalho. Ex abaixo
print("Teste")
#No exemplo, usei a função print() para mostrar no console um valor. Por trás do print() existe todo um código dedicado para fazer essa exibição

#Como criar uma função. Vamos criar uma função que soma 2 números.
def soma(n1, n2): # aqui criamos uma def (função) que vai receber dois números, n1  n2.
    resposta = n1 + n2 # Aqui estamos dizendo que a variável resposta receberá o resultado de n1 mais n2
    return resposta # retornamos o valor da resposta na função

#Vamos agora testar.
print(soma(10,13)) # irá exibir na tela a soma de 10 + 13
#Também podemos colocar o valor da soma em outra variável se for uma necessidade.
vinte = soma(10,10)

#funções podem receber várias coisas. Valores de qualquer tipo. Exemplo:
def lista_pessoas(lista_de_pessoas):
    for pessoa in lista_de_pessoas:
        print(pessoa)
    return True

quantidade_pessoas = range(2)
lista_de_pessoas = []
for i in quantidade_pessoas:
    lista_de_pessoas.append(input("Adicione um convidado. Pessoa " + str((i+1))))

lista_pessoas(lista_de_pessoas)

