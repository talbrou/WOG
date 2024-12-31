import sys

def welcome():
    print('insert username:')
    username = input()
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey')


def start_play():
    choosing_msg = """
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
    guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    """
    print(choosing_msg)
    game = int(input())
    if 1 <= game and game <= 3:
        print(f'You chose game: {game}')
    else:
        sys.exit('error: insert a number between 1-3')
    print("Select a difficulty level between 1 and 5")
    difficulty = int(input())
    if 1 <= difficulty and difficulty <= 5:
        print(f'You chose difficulty level: {difficulty}')
        return game, difficulty
    else:
        sys.exit('error: insert a number between 1-5')