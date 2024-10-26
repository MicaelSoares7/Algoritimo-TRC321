'''
prg023 - Escreva um programa que leia uma letra e caso a letra seja C, imprima “Casado”, caso
seja “S” imprima “Solteiro” e caso não seja nenhuma das duas, imprima “Estado Civil não
encontrado”.
'''

letra = input("Escreva uma letra que representa o seu Estado Civil: ")

if letra.upper() == 'C':
    print("Casado")

else:
    if letra.upper() == "S":
        print("Solteiro")

    else:
        print("Estado Civil não encontrado")