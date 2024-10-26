'''
prg028 - Escreva um programa que leia o nome, gênero e estado civil de uma pessoa. Caso a
pessoa seja casada e do gênero “F”, peça também o tempo do casamento em anos.
'''

nome = input("Digite o nome: ")
genero = input("Genero: ")
estado_civil = input("Estado civil: ")

if estado_civil == "casada" and genero == "F":
    tempo_casamento = int(input("Digite o seu tempo de casamento em anos: "))
    print(f"{nome}, gênero: {genero}, estado civil: {estado_civil}, tempo do casamento: {tempo_casamento}.")
else:
    print(f"{nome}, gênero: {genero}, estado civil: {estado_civil}.")

