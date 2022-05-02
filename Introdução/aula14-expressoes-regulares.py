#regular expression, ou regex, ou no python, só re.
#Serve para encontrar padrões em textos, como por exemplo, um email que tem TEXTO@TEXTO.TEXTO.TEXTO
import re
#Criando texto de teste
string_teste = "o gato é bonito, gatinho, gatão"
#buscando vazio no texto
padrao = re.search(r'ga\w\w',string_teste)
#\w busca letras. Exemplo, se eu colocar \w\w\w\w vai encontrar a primeira 4 letras consecutivas
if padrao:
#imprimindo o grupo. Ou seja, o que estamos buscando 
    print(padrao.group())
#Imprimindo o que é encontrado
    print(padrao)
else:
    print("padrão não encontrado")

#buscando todos os resultados, não só o primeiro
padrao2 = re.findall(r'ga\w*',string_teste)
# \w busca letras. Exemplo, se eu colocar \w\w\w\w vai encontrar as primeira 4 letras consecutivas
# * vai repetindo até satisfazer a busca.
# + precisa satisfazer a condição e ainda ter mais uma letra após
if padrao2:
    #nesse caso não usamos o group
#Imprimindo o que é encontrado
    print(padrao2)
else:
    print("padrão não encontrado")

    #Há muitas utilidades, é possível gerar padrões usando sites online, como o regex101.com
