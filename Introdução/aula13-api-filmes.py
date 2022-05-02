#importando bibliotecas
import requests
import json
#função para buscar filmes
def requisicao (titulo):
    apiKey = '' #PEGUE SUA CHAVE NO SITE DA API E COLOQUE AQUI DENTRO
    try:
        #fazendo a requisição GET. Tem que pegar a APIkey no site.
        req = requests.get('http://www.omdbapi.com/?apikey='+apiKey+'&t=' + titulo)
        #Mostrando os dados do filme em um dicionário
        dicionario = json.loads(req.text)
        #Retornando os dados do filme
        return dicionario
    except:
        #Se der erro ele mostra o erro e não retorna nada.
        print('Erro na conexão')
        return None
#Função para mostrar os dados do filme
def mostrar_dados(filme):
    print('Titulo: ', filme['Title'])
    print('Ano: ', filme['Year'])
    print('Diretor: ', filme['Director'])
    print('Atores: ', filme['Actors'])
    print('Nota: ', filme['imdbRating'])

#definindo comando para parar a aplicação
sair = False
while not sair:
    op = input('Escreva o nome do filme ou SAIR para fechar: ')

    if op == "SAIR":
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            mostrar_dados(filme)