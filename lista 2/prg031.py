'''prg031 - Escreva um programa que leia os valores da gasolina e do etanol de um determinado
posto de abastecimento de combustível. Seu programa deve verificar e informar qual
combustível é mais vantajoso para o cliente, considerando que o etanol rende 30% menos que
a gasolina.'''


gasolina = float(input("Digite o valor da gasolina: "))
etanol = float(input("Digite o valor do etanol: "))

if etanol < (0.7 * gasolina):
    print("Etanol é mais vantajoso")
else:
    print("Gasolina é mais vantajosa")