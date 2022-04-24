#operadores lógicos são tipo "verdade" ou "mentira"
#True ou False são valores do tipo boolean. True pode também ser escrito como 1, e False pode ser 0.
verdadeirooufalso = False
#Se for verdade, então mostrar que é verdade, se vc alterar o valor cai que é mentira.
if verdadeirooufalso == True:
    print('É verdade que a variável é TRUE')
else:
    print('É mentira que a variável é TRUE')
#Agora mais comparações para fixar melhor.
n1 = 50
n2 = 31
#se n1 for maior que n2 então mostra que ele é maior, se não, mostra que o n2 é maior que o n2.
if n1 > n2:
    print(n1, 'é maior que', n2)
else:
    print(n2, 'é maior que', n1)
#Os tipos de comparações que podemos usar para levantar se é verdadeiro ou falso são:
# == (igual)
# != (não igual, ou seja, diferente. O ! costuma servir como inversão de valor, se algo for TRUE e receber um ! antes, ele vira FALSE, ou se algo for FALSE ele vira TRUE)
# > (maior)
# < (menor)
# >= (maior ou igual)
# <=(menor ou igual)
#tem também as "concatenações" quando queremos comparar duas coisas diferentes,
# and (E) or (OU)
if n1 > n2 and n2 == 30:
    print('n1 maior que n2 e n2 igual a 30')
else:
    print('Errou')
#a diferença entre and e or é que se usar OR e uma das condições forem verdade, então todo o IF será verdade. Se usar o AND então tudo tem que ser verdade para o IF ser verdade.