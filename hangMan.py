from random import choice
word_bank = ['pokemon', 'cow', 'lissandra', 'mississippi', 'pterodactyl', 'cowboy', 'giselle','hentai', 'anime', 'fan',
             'caramel', 'apple', 'orange', 'banana', 'grape', 'honey', 'mouse', 'cat', 'dog', 'bird', 'painting',
             'movie', 'plant', 'animal']


def initialize():
    global solution, answer, life
    solution = str.upper(choice(word_bank))
    answer = list('_' * len(solution))
    life = 5
    main()


def find_letter(word, letter):
    return [idx for idx, value in enumerate(word) if value == letter]


def main():
    draw(life)
    print('Lives: ' + str(life))
    print(answer)

    if ''.join(answer) == solution:
        print("You WIN!!!")
        print('The answer was: ' + solution + "!")
        if (input("Play Again?: ")) == 'yes':
            initialize()
        return
    if life == 0:
        print("You LOSE!")
        print('The answer was: ' + solution + "!")
        if (input("Play Again?: ")) == 'yes':
            initialize()
        return
    guessing()


def guessing():
    global life
    guess = str.upper(input("Enter a letter: "))
    if list.count(answer, guess) > 0:
        print("You guessed this already")
        life -= 1
    index = find_letter(solution, guess)
    if not index:
        print("Nope!")
        life -= 1
    else:
        for x in index:
            answer[x] = guess
    main()


def draw(x):
    match x:
        case 4:
            print(' _____   ')
            print(' |   |   ')
            print(' |       ')
            print(' |       ')
            print(' |       ')
            print('/|\      ')
        case 3:
            print(' _____   ')
            print(' |   |   ')
            print(' |   O   ')
            print(' |       ')
            print(' |       ')
            print('/|\      ')
        case 2:
            print(' _____   ')
            print(' |   |   ')
            print(' |   O   ')
            print(' |   |   ')
            print(' |       ')
            print('/|\      ')
        case 1:
            print(' _____   ')
            print(' |   |   ')
            print(' |   O   ')
            print(' |  /|\  ')
            print(' |       ')
            print('/|\      ')
        case 0:
            print(' _____   ')
            print(' |   |   ')
            print(' |   O   ')
            print(' |  /|\  ')
            print(' |  / \  ')
            print('/|\      ')
        case 5:
            print(' _____   ')
            print(' |      ')
            print(' |       ')
            print(' |       ')
            print(' |       ')
            print('/|\      ')
        case _:
            print('Some error occurred')
    return


initialize()

