from carro import Carro
from veiculo import Veiculo # importando a classe Veiculo de dentro do arquivo veiculo
#definindo o valor da variável como a classe Veiculo e passando os valores como argumentos
caminhao_rosa = Veiculo('rosa', 'Mercedez', 8, 20)
print(caminhao_rosa)
print(type(caminhao_rosa))
print(caminhao_rosa.tanque)
caminhao_rosa.abastecer(15) # Usando o método abastecer dentro da classe para aumentar o valor do tanque.
print(caminhao_rosa.tanque)

carro_rosa = Carro('rosa', 'Mercedez', 8, 20)
print(carro_rosa)
print(type(carro_rosa))
print(carro_rosa.tanque)
carro_rosa.abastecer(15) # Usando o método abastecer dentro da classe para aumentar o valor do tanque.
print(carro_rosa.tanque)