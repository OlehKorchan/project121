from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Menu
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tkinter import filedialog as fd
import random
import first
import second

root = Tk()
root.title("Tic Tac Toe")
root.minsize(800, 600)
root.resizable(width=True, height=True)
text1 = ''
text2 = ''
mas = [0 for i in range(9)]
def Competitor():
	global win
	while not win:
		first.First(mas, pole)
		second.Second(mas, pole)
	

def FirstAlgo():
    global text1
    file_name = fd.askopenfilename()

    if file_name:
        f = open(file_name)
        #eval(f.read())
        text1 = f.read()
        print(text1)

def SecondAlgo():
    global text2
    file_name = fd.askopenfilename()

    if file_name:
        #eval(open(file_name).read())
        text2 = open(file_name).read()
        print(text2)

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
switch = ['X', 'O']
move = 0
win = False

def tic_tac_toe(n):
	global move
	global win

	pole[n]['bg'] = "silver"
	pole[n]['text'] = switch[move]
	pole[n].config(state='disabled')
	for i in range(8):
		for j in range(3):
			if vector[i][j] == n:
				vector[i][j] = switch[move]
	for index in range(8):
		if vector[index].count('X') == 3 or vector[index].count('O') == 3:
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

FirstAlgoText = Button(root, text = "Add algorithm 1", command = FirstAlgo)
FirstAlgoText.grid(row = 0, column = 4)

SecondAlgoText = Button(root, text = "Add algorithm 2", command = SecondAlgo)
SecondAlgoText.grid(row = 1, column = 4)

Compare = Button(root, text="Compare the algorithms", command=Competitor)
Compare.grid(row = 1, column = 5)

print(text1)
print(text2)

root.update()
root.mainloop()