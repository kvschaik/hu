names = ["Tinus", "Barrie", "Hans"]

snacks = []

for name in names:
	name_len = len(name)
	print(f'Hi {name}, the length of your name is {name_len}')
	snack = input(f'{name}, what is your favourite snack?')
	snacks.append(snack)

index = 0
for name in names:
    print(f'{name} likes {snacks[index]}' )
    index = index + 1
