
import games.currency_roulette_game as currency_roulette_game
import games.guess_game as guess_game
import games.memory_game as memory_game
from scoring import score


def welcome():
    print('enter username:')
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

    while True:
        try:
            game = int(input())
            if 1 <= game <= 3:
                print(f'You chose game: {game}')
                break
            else:
                print('Try Again: enter a number between 1-3')
        except ValueError:
            print("Invalid input. Please enter a number between 1-3")

    
    print("Select a difficulty level between 1 and 5")
    while True:
        try:
            difficulty = int(input())
            if 1 <= difficulty <= 5:
                print(f'You chose difficulty level: {difficulty}')
                break
            else:
                print('Try Again: enter a number between 1-5')
        except ValueError:
            print("Invalid input. Please enter a number between 1-5")

# start Memory Game
    if game == 1:
        result = memory_game.play(difficulty)
# start Guess Game
    elif game == 2:
        result = guess_game.play(difficulty)
# start Currency Roulette Game
    else:
        result = currency_roulette_game.play(difficulty)
# prompt result
    if result:
        score.add_score(difficulty)
        print("You win!!!!")
    else:
        print("You lose :(")
