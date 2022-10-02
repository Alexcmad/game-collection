import tkinter as tk
from random import choice
from PIL import Image, ImageTk

wins = [['r', 's'], ['s', 'p'], ['p', 'r']]
losses = [['s', 'r'], ['p', 's'], ['r', 'p']]
state = []

window = tk.Tk()

x = 0
y = 0

# Initializing Frames

fr_diff = tk.Frame(window)
for i in range(5):
    fr_diff.columnconfigure(i, minsize=60)
fr_diff.pack()

fr_main = tk.Frame(window)
fr_main.columnconfigure(1, minsize=175)
fr_main.columnconfigure(0, minsize=(175 / 3))
fr_main.columnconfigure(2, minsize=(175 / 3))
for i in range(3):
    fr_main.rowconfigure(i, minsize=(175 / 3))
fr_main.pack()

fr_rps = tk.Frame(window)
for i in range(3):
    fr_rps.columnconfigure(i, minsize=100)
fr_rps.rowconfigure(0, minsize=50)
fr_rps.pack()

# Initializing the Widgets to be used

# All images used
img_rock = tk.PhotoImage(file="venv/Pictures/Rock.png")  # Rock image
img_scissors = tk.PhotoImage(file="venv/Pictures/Scissors.png")  # Scissors image
img_paper = tk.PhotoImage(file="venv/Pictures/paper.png")  # Paper image
img_win = tk.PhotoImage(file="venv/Pictures/Hank Happy.png")  # Win image
img_lose = tk.PhotoImage(file="venv/Pictures/Hank Angy.png")  # Loss image
img_draw = tk.PhotoImage(file="venv/Pictures/2683921581879129.png")  # Draw image

# Rock Paper and Scissors buttons
btn_rock = tk.Button(fr_rps)
btn_paper = tk.Button(fr_rps)
btn_scissors = tk.Button(fr_rps)

moves = {
    btn_rock: "r",
    btn_paper: "p",
    btn_scissors: "s"
}

# Difficulty Buttons
btn_easy = tk.Button(fr_diff)
btn_normal = tk.Button(fr_diff)
btn_hard = tk.Button(fr_diff)
btn_insane = tk.Button(fr_diff)

lbl_diff = tk.Label(fr_diff, text="Difficulty:", anchor='e')
lbl_diff.grid(row=0, column=0, sticky='e')

lbl_display = tk.Label(fr_main)

player_rounds = [0, 0, 0]
bot_rounds = [0, 0, 0]
for i in range(3):
    player_rounds[i] = tk.Label(fr_main)
    bot_rounds[i] = tk.Label(fr_main)


def victory():
    lbl_display['image'] = img_win


def defeat():
    lbl_display['image'] = img_lose


def draw():
    lbl_display['image'] = img_draw



def player(event):
    global x, state
    btn = event.widget

    if btn['state'] != tk.DISABLED and x <= 2:
        player_rounds[x]['image'] = btn['image']
        state.append(moves[btn])
        bot(moves[btn])
        x += 1
        # print(state)
    state.clear()


def bot(btn):
    global state
    r = btn
    loss = {
        "r": "p",
        "p": "s",
        "s": "r"
    }

    win = {
        "p": "r",
        "s": "p",
        "r": "s"
    }

    images = {
        "p": btn_paper["image"],
        "s": btn_scissors["image"],
        "r": btn_rock["image"]
    }

    if y == 0:
        r = win[btn]
        state.append(r)
        victory()
    elif y == 2:
        state.append(r)
        draw()
    elif y == 3:
        r = loss[btn]
        state.append(r)
        defeat()

    elif y == 1:
        r = choice('rpsprssrpprs')
        state.append(r)
        if state in wins:
            print("Win")
            victory()
        elif state in losses:
            print("Loss")
            defeat()
        else:
            draw()
            print("Draw")

    bot_rounds[x]['image'] = images[r]


def diff(event):
    btn = event.widget
    global y
    if btn['state'] != tk.DISABLED:
        btn['relief'] = tk.SUNKEN
        print("Button Pressed While Active")
        for j in fr_diff.winfo_children():
            j['state'] = tk.DISABLED
        for j in fr_rps.winfo_children():
            j['state'] = tk.NORMAL

        if btn == btn_easy:
            y = 0
        elif btn == btn_normal:
            y = 1
        elif btn == btn_hard:
            y = 2
        elif btn == btn_insane:
            y = 3
    else:
        print("Button Pressed While Disabled")


def initialize():
    btn_easy.config(text="Easy")
    btn_easy.grid(row=0, column=1, sticky='ew')
    btn_easy.bind("<Button>", diff)

    btn_normal.config(text="Normal")
    btn_normal.grid(row=0, column=2, sticky='ew')
    btn_normal.bind("<Button>", diff)

    btn_hard.config(text="Hard")
    btn_hard.grid(row=0, column=3, sticky='ew')
    btn_hard.bind("<Button>", diff)

    btn_insane.config(text="Insane")
    btn_insane.grid(row=0, column=4, sticky='ew')
    btn_insane.bind("<Button>", diff)

    btn_rock.config(image=img_rock, state=tk.DISABLED)
    btn_rock.grid(row=0, column=0, sticky='nsew')
    btn_rock.bind('<Button>', player)

    btn_paper.config(image=img_paper, state=tk.DISABLED)
    btn_paper.grid(row=0, column=1, sticky='nsew')
    btn_paper.bind('<Button>', player)

    btn_scissors.config(image=img_scissors, state=tk.DISABLED)
    btn_scissors.grid(row=0, column=2, sticky='nsew')
    btn_scissors.bind('<Button>', player)

    lbl_display.config(image='', relief=tk.SUNKEN)
    lbl_display.grid(column=1, row=0, rowspan=3, sticky='nsew')

    for j in range(3):
        player_rounds[j].config(image='', relief=tk.SUNKEN)
        player_rounds[j].grid(column=0, row=j, sticky='nsew')
        bot_rounds[j].config(image='', relief=tk.SUNKEN)
        bot_rounds[j].grid(column=2, row=j, sticky='nsew')


initialize()
window.mainloop()
