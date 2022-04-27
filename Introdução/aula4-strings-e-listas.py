#lista é o mesmo que array. Caso o título confunda alguém. String são letras mesmo, só que ao mesmo tempo, toda string é uma array (lista) de letras. Então podemos exibir as letras nas posições que quisermos.
frase = 'Oi, tudo bem?'
#a lista a seguir tem 4 nomes.
#caso não saiba, as listas (arrays) começam em 0, não em 1. Ou seja, para mostrar o primeiro nome da lista, temos que exibir a posição 0 e não a posição 1, entendeu?
lista_nomes = ['Moisés', 'Aarão', 'Melquesedek', 'Abraão']
#exibindo os nomes com exemplos. Veja que começo mostrando a posição 0
print(lista_nomes[0]) # Vai mostrar Moisés
print(lista_nomes[1]) # Vai mostrar Aarão

#Agora mostrando como seria para exibir as strings da variável frase, que não foi declarada como uma array, mas ao mesmo tempo, ela é automáticamente como explicado no primeiro comentário.
print(frase[12]) # mostra só a interrogação
print(frase[0:5]) # mostra do O até o T
print(frase[0:13:2]) # pula os passos. Para você entender melhor, seria assim: 0 é o início, 13 é o número de items no array, o último parâmetro é de quantos em quantos vamos exibir. Ou seja, se colocar 1, ele mostra a letra uma a uma, ou seja, a frase toda. Se colocar 2, ele mostra uma e pula uma, e assim sucessivamente.

#MAIS RECURSOS DE STRING
#mostrar tudo minúsculo
print(frase.lower())
#mostrar tudo maiusculo
print(frase.upper())
#separar a frase pela vírgula
print(frase.split(','))

#Tem alguns detalhes ainda sobre a lista. Por exemplo, e se não soubermos quantos items tem na lista?
print(lista_nomes[-1]) # -1 vai mostrar o último item. -2 o penúltimo e por aí vai.

#Agora vamos adicionar um novo valor na lista de nomes
print(lista_nomes) # imprimindo a lista antes de adicionar mais um nome
lista_nomes.append('Maria') # adicionando Maria na lista.
print(lista_nomes) # mostrando a lista atualizada.
#apagando um valor especifico
lista_nomes.remove('Moisés') # removendo um valor
print(lista_nomes)
#inserir em uma posição escolhida.
lista_nomes.insert(0,'Isaias') #Colocando um novo nome na posição 0.
print(lista_nomes)
#Alterando o valor de uma posição específica
lista_nomes[0] = "Eliseu" # trocando o Isaias que definimos acima por Eliseu
print(lista_nomes)
#para buscar palavras repetidas, podemos usar o lista_nomes.count('valor repetido'), mas não temos nada repetido no nosso exemplo. Vamos adicionar algo repetido e mostrar a contagem.
lista_nomes.append('Maria')
contar_marias = lista_nomes.count('Maria')
print(lista_nomes, "com", contar_marias, "Marias")
#Também podemos limpar a lista
lista_nomes.clear()
print(lista_nomes)