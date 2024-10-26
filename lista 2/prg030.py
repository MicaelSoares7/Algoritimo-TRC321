'''prg030 - Escreva um programa que leia o nome e o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

nome1 = input("Digite o nome do produto: ")
preco1 = float(input("Digite o preço do primeiro produto: "))

nome2 = input("Digite o nome do produto: ")
preco2 = float(input("Digite o preço do primeiro produto: "))

nome3 = input("Digite o nome do produto: ")
preco3 = float(input("Digite o preço do primeiro produto: "))


if preco1 >= preco2 and preco1 >= preco3 and preco2 >= preco3:
    print(f'{nome3} é o pruduto mais barato! R$ {preco3}')
else:
    if preco1 >= preco2 and preco1 >=preco3 and preco3 >= preco2:
        print(f'{nome2} é o pruduto mais barato! R$ {preco2}')
    else:
        if preco2 >= preco1 and preco2 >= preco3 and preco1 >= preco3:
            print(f'{nome3} é o pruduto mais barato! R$ {preco3}')
        else:
            if preco2 >= preco1 and preco2 >= preco3 and preco3 >= preco1:
                print(f'{nome1} é o pruduto mais barato! R$ {preco1}')
            else:
                if preco3 >= preco1 and preco3 >= preco2 and preco1 >= preco2:
                    print(f'{nome2} é o pruduto mais barato! R$ {preco2}')
                else:
                    print(f'{nome1} é o pruduto mais barato! R$ {preco1}')