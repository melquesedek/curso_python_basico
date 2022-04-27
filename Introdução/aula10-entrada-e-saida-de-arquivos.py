#Abrir arquivo existente
open("a102.txt")
#Se for usar caminhos completos, ex: open("C:\windows") precisa colocar duas barras, para escapar a string, ou seja, para ele identificar que é uma barra. Ficaria então: open("C:\\windows"). No linux pode ser a barra normal /

#Criar arquivo colocando o W na frente caso não exista, e se existir, ele sobrescreve
#(NOME DO ARQUIVO, MODO DE ABERTURA)
arquivo = open("a102.txt", 'w') # Se existir o arquivo, o w apaga tudo que está no arquivo.
#w = write, r = read, r+ = leitura, se existir, escrita, a = append, para adicionar mais dados
#b = bytes, para arquivos que não são de texto

#tipo do arquivo - variável
type(print(arquivo))
#escrevendo no arquivo, dá para usar loops para escrever normalmente.
for i in range(0, 100):
    arquivo.write("E aí, pessoal. " + str(i) + "\n")

#sobreescrever a variável para fazer a leitura, usando o modo READ
arquivo = open("a102.txt", "r")
print(arquivo.read())

print("==============================")

#sobreescrever a variável para fazer a leitura, usando o modo READ
arquivo = open("a102.txt", "r")
#Outro modo de ler
for linha in arquivo:
    print(linha)