#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

dias *= 24 * 60 * 60
horas *= 60 * 60
minutos *= 60 

total_segundos =  dias + horas + minutos + segundos

print("O total em segundos é:", total_segundos)
