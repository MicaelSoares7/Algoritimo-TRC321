nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
else:
    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")