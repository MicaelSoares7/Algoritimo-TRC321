'''prg032 - Escreva um programa que receba o custo diário de transporte, o salário por dia de um
funcionário e a quantidade de dias que este trabalhou no mês. Seu programa deve calcular o
desconto do vale transporte considerando que este desconto seja o menor valor entre 6% do
seu salário ou o valor do vale transporte. Dica: Calcule o custo de transporte e o salário mensal
do funcionário para efetuar os cálculos do desconto do vale transporte.'''

custo_transporte = float(input("Digite o custo diário de transporte: "))
salario = float(input("Digite o salario por dia: "))
qtd_dias = int(input("Digite a quantidade de dias que trabalhou no mês: "))

custo = custo_transporte + (salario*qtd_dias)

desconto = (custo) * 6/100

print("O desconto do vale transporte é de: R$", desconto)