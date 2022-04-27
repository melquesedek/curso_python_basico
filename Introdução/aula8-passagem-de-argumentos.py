#passando argumentos, tipo como se fosse dar um comando no CMD. Ex: python --help. No exemplo o --help é um argumento.
import sys
#importando a biblioteca sys
argumentos = sys.argv
print(argumentos)

#Exemplo melhor de uso conforme ensinado no curso:
def soma(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2

if argumentos[1] == 'soma':
    resp = soma(float(argumentos[2]),float(argumentos[3]))
elif argumentos[1] == 'sub':
    resp = sub(float(argumentos[2]),float(argumentos[3]))

print(resp)
#Dessa forma, ao chamar o script pela linha de comando, posso passar os parametros na linha, Ex:
# /bin/python /home/melque/python/aula8-passagem-de-argumentos.py sub 10 20
#O exemplo acima irá mostrar -10, que é a subtração de 10 - 20