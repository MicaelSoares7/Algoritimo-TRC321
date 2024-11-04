'''prg034 - Escreva um programa que leia três números e que imprima o maior e o menor.'''

n = [0,0,0]

for i in range(3):
    n[i] = int(input("Digite um número: "))

if n[0] >= n[1] and n[0] > n[2] and n[1] > n[2]:
    maior = n[0]
    menor = n[2]
else:
    if n[0] >= n[2] and n[0] > n[1] and n[2] > n[1]:
        maior = n[0]
        menor = n[1]
    else:
        if n[1] >= n[2] and n[1] > n[0] and n[2] > n[0]:
            maior = n[1]
            menor = n[0]
        else:
            if n[1] >= n[0] and n[1] > n[2] and n[0] > n[2]:
                maior = n[1]
                menor = n[2]
            else:
                if n[2] >= n[1] and n[2] > n[0] and n[1] > n[0]:
                    maior = n[2]
                    menor = n[0]
                else:
                    maior = n[2]
                    menor = n[1]

print("O maior é:", maior)
print("O menor é:", menor)