#Faça um programa que calcule o aumento de um salário. 
#Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do salário: "))
porcentagem_aumento = float(input("Digite a porcentagem do aumento: "))

aumento = salario * (porcentagem_aumento / 100)
salario_novo = salario + aumento

print("O salário novo é:", salario_novo)