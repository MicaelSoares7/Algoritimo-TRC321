'''prg035 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do
aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os
inferiores ou iguais, de 15%.'''

salario = float(input("Digite o salario: "))
if salario > 1250:
    aumento = (salario*(10/100))
    novo_salario = aumento + salario
else:
    aumento = (salario*(15/100))
    novo_salario = aumento + salario

print("O salario recebeu um aumento de R$", aumento, "e o novo salario é R$", novo_salario)