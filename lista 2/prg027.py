'''
prg027 - Escreva um programa baseado no prg026, mas inclua na leitura o percentual de
frequência do aluno. Se o aluno obtiver um percentual menor que 75, estará reprovado não
importando a sua média.
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
freq = int(input("Digite o percentual de frequência: "))

media = (nota1 + nota2) / 2

if freq < 75:
    print("Reprovado")
else:
    if media == 10:
        print("Aprovado com Distinção")
    else:
        if media >= 6:
            print("Aprovado")
        else:
            print("Reprovado")