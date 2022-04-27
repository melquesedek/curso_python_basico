#Normalmente quando um programa dá erro, ele "trava", com o try e except a gente consegue fazer uma mensagem de erro ser exibida e não parar a execução.
#Para isso usamos o trye except, se liga no exemplo
try:
    a = 1200 / 0 # não é possível dividir por zero, então vamos mostrar o erro
except:
    print("Não dá para dividir por zero")
#Fazendo assim, ele mostra o erro e o script não para de rodar.
print("Programa continuou")


#O tipo de erro é: ZeroDivisionError nesse caso. Então podemos tratar esse erro diretamente, ignorando outros erros.
#No exemplo a seguir vou mostrar um erro diferente, mas passando pro except o tipo de erro, a mensagem exibida não será a que digitamos.
try:
    a()
    #Sem tratar esse erro específico, ou seja, não existe a função a(), e o except do NameError não foi tratado, então não será exibida mensagem e o programa irá parar.
except ZeroDivisionError:
    print("Não dá para dividir por zero")
#Fazendo assim, ele mostra o erro e o programa não irá mais rodar
print("Programa continuou")


b = 1200 / 0
# não é possível dividir por zero, então sem o except, o programa não continua
print("Programa continuou")

