import tkinter as tk
from random import choice

width = 300
mark = 'X'
bot = 'O'

window = tk.Tk()
# List containing all winning combinations of moves.
winning = [[0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8]]


def choose_mark(event):
    """
    Choose Mark function
    Event: Marker Button Click

    Allows the player to choose either X or O
    The bot will choose the other mark
    In the future, X will always start first
    """
    global mark, bot
    mark = event.widget["text"]
    if mark == 'O':
        bot = 'X'
    else:
        bot = 'O'

    for x in buttons:
        x["state"]=tk.ACTIVE
        x["relief"]=tk.RAISED
        x["borderwidth"] = 3

    event.widget["state"]=tk.DISABLED


def player_move(event):
    """
    Player Move Function
    event: Grid Button Click

    When the player clicks a button to move:
        Deduce which button was clicked
        Check if the button is DISABLED or ENABLED

        If the button is ENABLED:
            Add the index of the button to the list of moves made by player
            Remove the button from the list of available moves
            Change the Mark of the button to the chosen Marker
            Change the button state to DISABLED
            Check if one of the winning combinations is a subset of the moves made

            If a subset is found:
                TBI: Go to End Game function

        Go to the Bot Move function
    """
    button_pressed = event.widget
    print(str(button_pressed) + " Pressed While " + button_pressed["state"])

    if not (button_pressed["state"] == tk.DISABLED):
        for i in range(9):
            if button_pressed == buttons[i]:
                player_moves.append(i)
                print(player_moves)

        button_pressed["text"] = mark
        button_pressed["state"] = tk.DISABLED
        available_moves.remove(button_pressed)
        print(buttons)

        for i in winning:
            if set(i).issubset(player_moves):
                game_end(1)

        if available_moves:
            bot_move()


def bot_move():
    """
    Bot Move Function

    Choose the bot's move from the list of available moves
    Change the text on the button the bot used to move to the bot's marker
    Disable the button the bot used to move and remove it form the list of available moves

    Add the move the bot made the the list of all moves made by the bot
    """
    if available_moves:
        computer = choice(available_moves)
        computer["text"] = bot
        available_moves.remove(computer)
        computer["state"] = tk.DISABLED

    for i in range(9):
        if computer == buttons[i]:
            bot_moves.append(i)
            print(bot_moves)

    for i in winning:
        if set(i).issubset(bot_moves):
            game_end(0)

    print("Bot Moved")


def game_end(x):
    print("Game End")
    for widget in window.winfo_children():
        widget.destroy()
    initialize()


def  initialize():
    global window, buttons, available_moves, player_moves, bot_moves

    buttons = []  # List containing all the buttons on the grid for easy reference
    available_moves = []  # List containing all the moves that are available to the player or bot
    player_moves = []  # List containing all the moves the player has made
    bot_moves = []  # List containing all the moves the bot has made



    fr_mark = tk.Frame(width=width, height=30, master=window, borderwidth=5)
    fr_mark.columnconfigure(1, minsize=100)
    fr_mark.columnconfigure(2, minsize=100)
    fr_mark.pack()
    lbl_mark = tk.Label(text="Choose To Start:", master=fr_mark)
    lbl_mark.grid(row=0, column=0, sticky='e')

    btn_X = tk.Button(text="X", master=fr_mark)
    btn_X.grid(row=0, column=1, sticky='nsew', padx=5)
    btn_X.bind("<Button>", choose_mark)

    btn_O = tk.Button(text="O", master=fr_mark)
    btn_O.grid(row=0, column=2, sticky='nsew', padx=5)
    btn_O.bind("<Button>", choose_mark)

    fr_grid = tk.Frame(width=width, height=width, master=window, borderwidth=10)
    fr_grid.pack()

    i = 0
    for x in range(3):
        for y in range(3):
            button = tk.Button(text="", master=fr_grid, state= tk.DISABLED, relief=tk.GROOVE)
            button.grid(row=x, column=y, sticky='nsew')
            button.bind("<ButtonRelease>", player_move)
            available_moves.append(button)
            buttons.append(button)
        fr_grid.columnconfigure(x, minsize=50)
        fr_grid.rowconfigure(x, minsize=50)
    window.mainloop()


initialize()
