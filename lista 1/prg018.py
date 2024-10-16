salario = float(input("Digite o seu salário fixo: "))
valor = float(input("Digite o valor das vendas: "))

salario_final = salario + (valor * (4/100))

print("O salário final é: %5.2f" % salario_final)