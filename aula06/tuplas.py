print("-"*20)
print("{:^20}".format("Numeral para Extenso"))
print("-"*20)
numero = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove")
while True:
	escolha = int(input("Escolha um número entre 0 e 9: "))
	if escolha >= 0 and escolha <= 9:
		break
print(f"O número {escolha} por extenso é {numero[escolha]}")
print("-"*20)