#from tkinter import *

def FirstTactic(mas, move):
	global count
	if move == 1:
		digit = 'X'
	else:
		digit = 'O'
	if count == 0:
		mas[1][1] = digit
	elif count == 1:
		if mas[0][0] == 0:
			mas[0][0] = digit
		elif mas[0][2] == 0:
			mas[0][2] = digit
		elif mas[2][0] == 0:
			mas[2][0] = digit
		elif mas[2][2] == 0:
			mas[2][2] = digit
	else:
		l = 1
		for i in range(3):
			for j in range(3):
				if mas[i][j] != 'X' and mas[i][j] != 'O':
					mas[i][j] = digit
					l = 0
					break
			if l == 0:
				break

	count += 1
def SecondTactic(mas, move):
	global count
	if move == 1:
		digit = 'X'
	else:
		digit = 'O'
	if count == 0:
		mas[1][1] = digit
	elif count == 1:
		if mas[0][1] == 0:
			mas[0][1] = digit
		elif mas[0][2] == 0:
			mas[0][2] = digit
		elif mas[2][1] == 0:
			mas[2][1] = digit
		elif mas[2][2] == 0:
			mas[2][2] = digit
	else:
		l = 1
		for i in range(1, 3):
			for j in range(1, 3):
				if mas[i][j] != 'X' and mas[i][j] != 'O':
					mas[i][j] = digit
					l = 0
					break
			if l == 0:
				break
	count += 1

x = 1
o = 0
def Cheker(mas):
	global k
	if mas[0][0] != 0 and mas[0][0] == mas[0][1] and mas[0][0] == mas[0][2]:
		print(mas[0][0] + " won")
		k = 0
	elif mas[1][0] != 0 and mas[1][0] == mas[1][1] and mas[1][0] == mas[1][2]:
		print(mas[1][0] + " won")
		k = 0
	elif mas[2][0] != 0 and mas[2][0] == mas[2][1] and mas[2][0] == mas[2][2]:
		print(mas[2][0] + " won")
		k = 0
	elif mas[0][0] != 0 and mas[0][0] == mas[1][0] and mas[0][0] == mas[2][0]:
		print(mas[0][0] + " won")
		k = 0
	elif mas[0][1] != 0 and mas[0][1] == mas[1][1] and mas[0][1] == mas[2][1]:
		print(mas[0][1] + " won")
		k = 0
	elif mas[0][2] != 0 and mas[0][2] == mas[1][2] and mas[0][2] == mas[2][2]:
		print(mas[0][2] + " won")
		k = 0
	elif mas[0][0] != 0 and mas[0][0] == mas[1][1] and mas[0][0] == mas[2][2]:
		print(mas[0][0] + " won")
		k = 0
	elif mas[0][2] != 0 and mas[0][2] == mas[1][1] and mas[0][0] == mas[2][0]:
		print(mas[0][2] + " won")
		k = 0
	
def Competitor():
	while(k):
		FirstTactic(mas, x)
		print(mas[0])
		print(mas[1])
		print(mas[2])
		SecondTactic(mas, o)
		print(mas[0])
		print(mas[1])
		print(mas[2])
		Cheker(mas)
k = 1
mas = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

count = 0

Competitor()