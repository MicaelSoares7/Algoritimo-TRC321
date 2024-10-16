quantidade = int(input("Quantos cigarros fumados por dia? "))
anos = int(input("Por quantos anos fumou? "))

total_cigarros = quantidade * anos * 365
min = total_cigarros * 10

total = min / (24*60)

# print(f"Você perdeu aproximadamente {total:.2f} dias de vida devido ao fumo.")
print("Você perdeu", total, "dias de vida devido ao fumo.")