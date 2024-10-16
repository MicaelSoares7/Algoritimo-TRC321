km_percorrido = float(input("Digite a quantidade de km percorrido pelo carro alugado: "))
dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))

preco = (dias * 60) + (0.15 * km_percorrido)

print("O preço a pagar é", preco)