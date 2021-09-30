# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar a casa ?'))
prestacao = casa / (anos * 12)
if prestacao <= 0.3 * salario:
    print('Empréstimo aprovado! A prestação é até 30% do seu salário. o valor da prestação é R${:.2f}.'.format(prestacao))
else:
    print('Empréstimo negado, pois a prestação é maior do que 30% do seu salário!')
