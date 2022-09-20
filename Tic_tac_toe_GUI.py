import tkinter as tk
from random import choice

window = tk.Tk()
width = 300
mark = 'X'
bot = 'O'
buttons = []

def bot_move(move):
    computer = choice(buttons)
    computer["text"] = bot
    buttons.remove(computer)
    print("Bot Moved")



def choose_mark(event):
    global mark, bot
    mark = event.widget["text"]
    if mark == 'O':
        bot = 'X'
    else:
        bot = 'O'


def player_move(event):
    buttonPressed = event.widget
    print(str(buttonPressed) + " Pressed While " + buttonPressed["state"])

    if not(buttonPressed["state"] == tk.DISABLED):
        buttonPressed["text"] = mark
        buttonPressed["state"] = tk.DISABLED
        buttons.remove(buttonPressed)

        print(buttons)

        bot_move(buttonPressed)


fr_mark = tk.Frame(width=width, height=30, master=window, borderwidth=5)
fr_mark.columnconfigure(1, minsize=100)
fr_mark.columnconfigure(2, minsize=100)
fr_mark.pack()

lbl_mark = tk.Label(text="Marker:", master=fr_mark)
lbl_mark.grid(row=0, column=0, sticky='e')

btn_X = tk.Button(text="X", master=fr_mark)
btn_X.grid(row=0, column=1, sticky='nsew', padx=5)
btn_X.bind("<Button>", choose_mark)

btn_O = tk.Button(text="O", master=fr_mark)
btn_O.grid(row=0, column=2, sticky='nsew', padx=5)
btn_O.bind("<Button>", choose_mark)

fr_grid = tk.Frame(width=width, height=width, master=window, borderwidth=10)
fr_grid.pack()

i=0
for x in range(3):
    for y in range(3):
        button = tk.Button(text="", master=fr_grid)
        button.grid(row=x, column=y, sticky='nsew')
        button.bind("<ButtonRelease>", player_move)
        buttons.append(button)
    fr_grid.columnconfigure(x, minsize=50)
    fr_grid.rowconfigure(x, minsize=50)

window.mainloop()
