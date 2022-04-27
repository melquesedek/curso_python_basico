#Descobri que lista (List) é List e não array. Aparentemente o Python dá um nome diferente
#Ou seja, Abaixo uma lista de dados.
lista = ['dado1', 'dado2', 'dado3']
#Também tem a Tuple (Tupla) que é tipo a lista, só que com parenteses
tupla = ('dado1', 'dado2', 'dado3')
#A principal diferença é que a Tuple (Tupla) não é mutável, por exemplo, não dá para adicionar ou remover items. Se tiver X items, a Tuple vai continuar  com X items.

#Também existe o dicionário, Dict. É usado colchete ao invés da chave.
#Só que o dicionario tem chave e valor, exemplo abaixo
dicionario = {'dado1' : 'primeiro dado', 'dado2' : 'segundo dado', 'dado3': 'terceiro dado'}
#O dicionário parece com JSON para quem manja de JS.

#Conjunto é um dicionário só que só tem os valores dentro. Conjunto (Set) é dinâmico, pode adicionar ou remover items. Só a Tuple (Tupla) não pode.
conjunto = {'dado1','dado2'} # conjuntos não pode ter dados repetidos.
#conjuntos não são ordenados.

print(tupla)
print(tupla[0])

#O funcionamento são basicamente como uma lista, mas cada um com sua particularidade.