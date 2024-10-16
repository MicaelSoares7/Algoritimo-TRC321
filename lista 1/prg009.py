#Escreva um programa que calcule o tempo de uma viagem de carro. 
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Digite a distância em km a percorrer: "))
velocidade = float(input("Digite a velocidade média esperada: "))

tempo = distancia / velocidade

print("O tempo de viagem é", tempo, "horas.")