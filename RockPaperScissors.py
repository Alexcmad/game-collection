from random import choice
import tkinter as tk

r = 'ROCK'
p = 'PAPER'
s = 'SCISSORS'


class shoot:  # A class that for some reason is necessary to use when working with switch (match) cases.
    # Honestly would've saved 2 hours to just use elif.
    r = r
    p = p
    s = s


rps = [shoot.r, shoot.p, shoot.s]  # Making a List with all 3 possible Options
bot = str.upper(choice(rps))  # Variable to store the choice the computer randomly chose


# Function to be run if the player wins the match
def win():
    print("You Win!")
    print('Dumb Computer: ' + bot)
    playAgain = input("Do you wanna play again?: ")
    if str.upper(playAgain) == 'YES':
        choose_dif()
        return 0


# Function to be run if the player loses the match
def lose():
    print("You Lose!")
    print('Big Brain Computer: ' + bot)
    playAgain = input("Do you wanna play again?: ")
    if str.upper(playAgain) == 'YES':
        choose_dif()
    else:
        return 0


# Function to be run if the match is a tie
def tie():
    print("It's a Tie!")
    print('Ultra Instinct Computer: ' + bot)
    playAgain = input("Do you wanna play again?: ")
    if str.upper(playAgain) == 'YES':
        choose_dif()
    else:
        return 0


# Normal mode: Computer chooses rock paper scissors at random. Not rigged at all.
def normal(play):
    if bot == play:
        tie()
    elif bot == r:
        if play == p:
            win()
        else:
            lose()
    elif bot == p:
        if play == s:
            win()
        else:
            lose()
    elif bot == s:
        if play == r:
            win()
        else:
            lose()


# Easy mode: Computer always chooses the losing option. Rigged in the player's favor.
def easy(play):
    global bot
    match play:  # The aforementioned switch case that took way too much time.
        case shoot.r:
            bot = s
        case shoot.p:
            bot = r
        case shoot.s:
            bot = p
        case _:  # Default for debugging.
            print(play)
            print(shoot.r)
            print(shoot.p)
            print(shoot.s)
            print(r)
            print(p)
            print(s)
            return play

    win()


# Hard mode: Computer always chooses what the player chooses. Rigged to always tie.
def hard(play):
    global bot
    bot = play
    tie()


# Impossible mode: Computer always chooses the winning option. Rigged against the player.
def impossible(play):
    global bot
    match play:
        case shoot.p:
            bot = s
        case shoot.s:
            bot = r
        case shoot.r:
            bot = p
        case _:
            print(play)
            print(shoot.r)
            print(shoot.p)
            print(shoot.s)
            print(r)
            print(p)
            print(s)
            return play
    lose()


def choose_dif():  # Function to choose the difficulty as well as changing the names of rock paper and scissors.
    # Would be cleaner and generally more user-friendly as a menu
    dif = str.upper(input("Easy, Normal or Hard?: "))
    match dif:
        case 'HARD':
            hard(str.upper(input(r + ' ' + p + ' ' + s + ' ' + '!: ')))  # Would also be cleaner if I put these in the functions themselves.
        case 'NORMAL':
            normal(str.upper(input(r + ' ' + p + ' ' + s + ' ' + '!: ')))
        case 'EASY':
            easy(str.upper(input(r + ' ' + p + ' ' + s + ' ' + '!: ')))
        case 'IMPOSSIBLE':
            print(f"IMPOSSIBLE MODE FOUND\nIF YOU WIN YOU'RE A GOD\n\n")
            impossible(str.upper(input(r + ' ' + p + ' ' + s + ' ' + '!: ')))
        case 'SECRET':
            custom_stuff()


def custom_stuff():
    global r, p, s
    r = shoot.r = str.upper(input("What is new " + r + ": "))
    p = shoot.p = str.upper(input("What is new " + p + ": "))
    s = shoot.s = str.upper(input("What is new " + s + ": "))
    choose_dif()


choose_dif()

