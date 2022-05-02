import requests
#Python já tem PIP embutido. Para usar pacotes e bibliotecas
#Para usar requisições precisa instalar com o PIP o pacote requests
#Há vários tipos de requisiões (POST,GET são as mais comuns). Só solocar na frente de requests
texto = None
#Site https://putsreq.com/ gera uma API para tesar requisição
#Passando dados no cabeçalho, note que usamos um dicionário, então enviamos chave e valor ao cabeçalho.
cabecalho = {'User-agent': 'Windows 14',
            'Referer' : 'https://www.google.com',
            'CF_IPcountry' : 'US'
            }
#Abaixo criamos um cookie para armazenar na máquina
meus_cookies = {'Ultima-visita' : '10-10-2022'}
#Simulamos o envio de dados
dados = {'username' : 'Melque',
         'password' : 'senha'}
#Iniciamos a requisição com o try para nos devolver caso dê algum erro. Para testar a requisição enviada, acesse o site do putsreq no endereço que está gerado para ver a comunicação e os headers.
try:
    #Dando o comando com GET, para enviar os dados por URL
    #requisicao = requests.get('https://putsreq.com/Db0W2q2quEuYety8W4uj')
    #Dando o comando POST para enviar os dados "ocultos"
    requisicao = requests.post('https://putsreq.com/Db0W2q2quEuYety8W4uj', headers=cabecalho, cookies=meus_cookies, data=dados)
    #Gravando a requisição em uma variável. O .text é o que mostra o retorno da requisição.
    texto = requisicao.text
except Exception as e:
    print("Requisição deu erro:", e)
    
print(texto)