'''prg033 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso
ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso,
exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.'''

velocidade = float(input("Digite a velocidade do carro (km/h): "))

#multa = 0

if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade - 80) * 5

    # Caso fosse multado acada 80 km/h:
    # for i in range(velocidade//80):
    #    multa += 5
    
    if multa > 0:
        print("A multa foi de R$",multa)