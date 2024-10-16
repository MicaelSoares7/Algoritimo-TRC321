numero = int(input("Digite um número com 3 algarismos: "))

a = numero // 100
b = numero % 100 // 10
c = numero % 100 % 10

print(f"{c}{b}{a}")