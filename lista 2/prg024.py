'''
prg024 - Escreva um programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input("Digite uma letra: ")

if letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'U':
    print(f"A letra {letra} é vogal!")
else:
    print(f"A letra {letra} é consoante!")