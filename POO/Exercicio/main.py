#Os exercícios passados foram bem mais simples que esse, por isso esse é o único exercício que tem aqui. E o único que fiz até agora.
'''
Essas três aspas servem para fazer comentários de muitas linhas
Estamos fazendo um esquema meio que de dados bancários.
Vamos cadastrar o cliente, e gerenciar a conta e tals. Bem simples mesmo.
'''
#Importando as classes
from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Melque', '123.456.789-10', 80) # Criando o cliente. Passando nome, cpf e idade
print (cliente1) #Mostrando os dados segundo o retorno da STR na classe

conta_melque = Conta(cliente1, 10.50, 1000) # Criando conta

print(conta_melque.cliente.nome, conta_melque.consulta_saldo())

conta_melque.depositar(9840.40) #Depositando o dinheiro

print(conta_melque.consulta_saldo())

conta_melque.sacar(300) #Retirando Dinheiro

print(conta_melque.consulta_saldo())

conta_melque.sacar(1200) #Retirando mais um dinheirinho

print(conta_melque.consulta_saldo())