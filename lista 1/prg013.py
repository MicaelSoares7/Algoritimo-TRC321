x1, y1 = input("Digite o valor de x1 e y1: ").split(',')
x2, y2 = input("Digite o valor de x2 e y2: ").split(',')

x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)

distancia = ((x2-x1)**2 + (y2-y1)**2)**1/2

print("A distância entre eles é:", distancia)