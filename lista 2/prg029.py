'''prg029 - Escreva um programa que 3 números inteiros quaisquer. Seu programa deve informar
estes números em ordem crescente.'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terçeiro número: "))


if n1 >= n2 and n1 >= n3 and n2 >= n3:
    print(f'A ordem crescente é {n3} , {n2} e {n1}')
else:
    if n1 >= n2 and n1 >=n3 and n3 >= n2:
        print(f'A ordem crescente é {n2} , {n3} e {n1}')
    else:
        if n2 >= n1 and n2 >= n3 and n1 >= n3:
            print(f'A ordem crescente é {n3} , {n1} e {n2}')
        else:
            if n2 >= n1 and n2 >= n3 and n3 >= n1:
                print(f'A ordem crescente é {n1} , {n3} e {n2}')
            else:
                if n3 >= n1 and n3 >= n2 and n1 >= n2:
                    print(f'A ordem crescente é {n2} , {n1} e {n3}')
                else:
                    print(f'A ordem crescente é {n1} , {n2} e {n3}')