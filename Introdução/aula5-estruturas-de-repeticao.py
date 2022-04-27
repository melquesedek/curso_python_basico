#repetições são comandos que rodam X vezes até que a condicional de vezes acabe.
nomes = ['Moisés', 'Aarão', 'Melquesedek', 'Abraão']
#mostrando tamanho do array
print(len(nomes))
#FOR executa enquanto tiver valores a mostrar, independente da quantidade de vezes. Ele varre o array separando os dados
for nome in nomes:
    print(nome)

#Outra forma de usar o array, é com contadores. Exemplo:
contador = range(10) # range é o mesmo que alcance.
for i in contador:
    print (i) # mostre o número. Nota, ele começa em 0

#WHILE é um comando que roda enquanto uma condicional for verdadeira, e não com contador necessáriamente. Por exemplo:
i = 0
while i <= 10: # enquanto o i for menor ou igual a 10, então ele vai exibir. É diferente de um contador que vai executar x vezes determinadas, esse executa enquanto a condicional for verdadeira
    print('i menor que 10', i)
    i += 1
#CUIDADO COM LOOPS INFINITOS
#SE A CONDICIONAL FOR SEMPRE TRUE, O WHILE PODE EXECUTAR PARA SEMPRE (GERALMENTE DÁ ERRO)