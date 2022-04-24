print('Hello World\nSegundaLinha\tTecla Tab')
nome = 'Melque'
print('Nome:', nome)
idade = 27
tipo_nome = type(nome)
tipo_idade = type(idade)

print(tipo_nome)
print(idade)
print(tipo_idade)
altura = 1.75
tipo_altura = type(altura)
print('Altura: ' + str(altura))
print(tipo_altura)

entrada = input('Escreva algo \n')
print('Você escreveu', entrada)

n1 = int(input('Número 1'))
n2 = int(input('Número 2'))
#comentário
resultado = n1 + n2
potencia = 10 ** 2
print(n1, "+", n2, "=", resultado, 'e 10 elevado a 2 =', potencia)