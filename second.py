def Second(mas, pole):
	for i in range(9):
		if mas[i] == 0:
			mas[i] = 2
			pole[i].invoke()
			break
