# TIK TAK TOE A MEK
from random import choice
grid = []
moves = []
columns = (0, 1, 2)
rows = (0, 3, 6)
player = 'X'
bot = 'O'


def initialize():
    global player, grid, bot, moves
    grid = list('_' * 9)
    moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    print(f"[1], [2], [3]\n[4], [5], [6]\n[7], [8], [9]\nAbove is what number to enter to place your marker")
    player = input("Do you want to be X or O?: ")
    if player == 'O' or 'o' or '0':
        bot = 'X'
    else:
        bot = 'O'

    game_loop()


def show_game():
    print(grid[0], grid[1], grid[2])
    print(grid[3], grid[4], grid[5])
    print(grid[6], grid[7], grid[8])


def game_loop():
    show_game()
    placer = int(input("Where do you want to place: "))-1
    if placer in moves:
        grid[placer] = player
        moves.remove(placer)
    else:
        input("This Move Is Unavailable. Press Enter To Continue....")
        game_loop()
    for x in columns:
        if grid[x] == grid[x + 3] == grid[x + 6] == player:
            win()
        elif grid[x] == grid[x + 3] == grid[x + 6] == bot:
            lose()

    for x in rows:
        if grid[x] == grid[x + 1] == grid[x + 2] == player:
            win()
        if grid[x] == grid[x + 1] == grid[x + 2] == bot:
            lose()

    if (grid[0] == grid[4] == grid[8] == player) or (grid[2] == grid[4] == grid[6] == player):
        win()
    elif (grid[0] == grid[4] == grid[8] == bot) or (grid[2] == grid[4] == grid[6] == bot):
        lose()
    bot_move()
    game_loop()


def win():
    show_game()
    if input("YOU WIN!!! Play again?: ") == 'yes':
        initialize()
    else:
        exit()


def lose():
    show_game()
    if input("You Lose Play again?: ") == 'yes':
        initialize()
    else:
        exit()


def bot_move():
    try:
        move = int(choice(moves))
        moves.remove(move)
        grid[move] = bot
    except IndexError:
        print("OUT OF MOVES!")
    return


initialize()
