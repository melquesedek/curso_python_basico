#print é a saída para o console, é bem provável que também seja o que imprima na tela, ainda não cheguei nessa parte.
print('Hello World\nSegundaLinha\tTecla Tab') # \n pula a linha da string, e \t dá um tab no texto
nome = 'Melque'
print('Nome:', nome)
#variáveis não são tipadas, então o python identifica o tipo automaticamente.
idade = 27
#type serve para ver qual o formato da variável
tipo_nome = type(nome)
tipo_idade = type(idade)
print(tipo_nome)
print(idade)
print(tipo_idade)
altura = 1.75
tipo_altura = type(altura)
#concatenando com vírgula, automaticamente é adicionado um espaço no texto (como useu no print da variável nome), concatenando com + é possível quando o valor for string.
#no exemplo a seguir, transformei o float (altura) em string usando a função str()
print('Altura: ' + str(altura))
print(tipo_altura)
#input espera a entrada do usuário. O que o usuário colocar, irá gravar na variável. Se fosse fazer uma calculadora, provavelmente seria usado algo assim, acredito eu. Ou um formulário de cadastro, né?
entrada = input('Escreva algo \n')
print('Você escreveu', entrada)
n1 = int(input('Número 1'))
n2 = int(input('Número 2'))
#comentário
resultado = n1 + n2
potencia = 10 ** 2
print(n1, "+", n2, "=", resultado, 'e 10 elevado a 2 =', potencia)