salario = float(input("Digite o seu salário fixo: "))
valor = float(input("Digite o valor das vendas: "))

comissao = valor * (4/100)
salario_final = salario + comissao

print(f"Comissão: R$ {comissao:.2f}")
print(f"O salário final é: R$ {salario_final:.2f}")