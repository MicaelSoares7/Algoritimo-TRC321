#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar.

preco = float(input("Digite o preço de uma mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = preco * (desconto / 100)
preco_pagar = preco - valor_desconto

print("O valor do desconto é:", valor_desconto)
print("O preço a pagar é:", preco_pagar)