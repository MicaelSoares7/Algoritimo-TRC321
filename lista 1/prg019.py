ano_nasc = int(input("Digite o ano que você nasceu: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nasc

mes = idade*12
dias = idade*365
semanas = idade*52.1786

print("Sua idade em anos:", idade)
print("Sua idade em meses:", mes)
print("Sua idade em dias:", dias)
print("Sua idade em semanas:", semanas)