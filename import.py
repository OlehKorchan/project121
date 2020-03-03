from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Menu
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tkinter import filedialog as fd
import random
root = Tk()
root.title("Tic Tac Toe")
root.minsize(800, 600)
root.resizable(width=True, height=True)
text1 = ''
text2 = ''
def Competitor():
	pass
def FirstAlgo():
	global text1
	eval(text1)
def SecondAlgo():
	global text2
	eval(text2)
coordinate = (
	(0, 1, 2),(0, 3, 6),(1, 4, 7),
	(2, 5, 8),(3, 4, 5),(6, 7, 8),
	(0, 4, 8),(2, 4, 6)
	)
vector = [
	[0, 1, 2],[0, 3, 6],[1, 4, 7],
	[2, 5, 8],[3, 4, 5],[6, 7, 8],
	[0, 4, 8],[2, 4, 6]
		]
pole = [i for i in range(9)]
switch = ['X', 'Y']
move = 0
win = False
def tic_tac_toe(n):
	global move
	global win

	pole[n]['bg'] = "silver"
	pole[n]['text'] = switch[move]
	for i in range(8):
		for j in range(3):
			if vector[i][j] == n:
				vector[i][j] = switch[move]
	for index in range(8):
		if vector[index].count('X') == 3 or vector[index].count('Y') == 3:
			win = True
			for i in coordinate[index]:
		 		pole[i]['bg'] = 'green'
		 		print(i)
			break
	if win:
		for i in range(9):
			pole[i].config(state='disabled')
	if move == 0:
		move = 1
	else:
		move = 0

pole[0] = Button(root, command = lambda : tic_tac_toe(0), width=4, height=2, font=15)
pole[0].grid(row=0, column = 0)

pole[1] = Button(root, command = lambda : tic_tac_toe(1), width=4, height=2, font=15)
pole[1].grid(row=0, column = 1)

pole[2] = Button(root, command = lambda : tic_tac_toe(2), width=4, height=2, font=15)
pole[2].grid(row=0, column = 2)

pole[3] = Button(root, command = lambda : tic_tac_toe(3), width=4, height=2, font=15)
pole[3].grid(row=1, column = 0)

pole[4] = Button(root, command = lambda : tic_tac_toe(4), width=4, height=2, font=15)
pole[4].grid(row=1, column = 1)

pole[5] = Button(root, command = lambda : tic_tac_toe(5), width=4, height=2, font=15)
pole[5].grid(row=1, column = 2)

pole[6] = Button(root, command = lambda : tic_tac_toe(6), width=4, height=2, font=15)
pole[6].grid(row=2, column = 0)

pole[7] = Button(root, command = lambda : tic_tac_toe(7), width=4, height=2, font=15)
pole[7].grid(row=2, column = 1)

pole[8] = Button(root, command = lambda : tic_tac_toe(8), width=4, height=2, font=15)
pole[8].grid(row=2, column = 2)
#FirstAlgoText = Button(root, command=insert_text())
#FirstAlgoText.grid(row=0, column=4)
#SecondAlgoText = Button(root, command=insert_text())
#SecondAlgoText.grid(row = 0, column=6)
#pole[4].invoke()
root.update()
root.mainloop()