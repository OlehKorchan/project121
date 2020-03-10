def First(mas, pole):
	for i in range(9):
		if mas[i] == 0:
			mas[i] = 1
			pole[i].invoke()
			break

