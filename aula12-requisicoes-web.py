import requests
#Python já tem PIP embutido. Para usar pacotes e bibliotecas
#Para usar requisições precisa instalar com o PIP o pacote requests
#Há vários tipos de requisiões. Só solocar na frente de requests
texto = None
cabecalho = {'User-agent': 'Windows 14',
            'Referer' : 'https://www.google.com',
            'CF_IPcountry' : 'US'
            }
meus_cookies = {'Ultima-visita' : '10-10-2022'}
dados = {'username' : 'Melque',
         'password' : 'senha'}
try:
    #requisicao = requests.get('https://putsreq.com/Db0W2q2quEuYety8W4uj')
    requisicao = requests.post('https://putsreq.com/Db0W2q2quEuYety8W4uj', headers=cabecalho, cookies=meus_cookies, data=dados)
    texto = requisicao.text
except Exception as e:
    print("Requisição deu erro:", e)
print(texto)