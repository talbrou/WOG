import random, sys

class Guess_game:
    def generate_number(difficulty):
        secret_number = random.randint(0, difficulty)
        print(f'random number is: {secret_number}')
        return secret_number

    def get_guess_from_user(difficulty):
        print(f'insert a number between 0 and {difficulty}:')
        guess_from_user = int(input())
        if 0 <= guess_from_user and guess_from_user <= difficulty:
            print(f'You guessed: {guess_from_user}')
        else:
            sys.exit('error: insert a number within the range')
        return int(guess_from_user)

    def compare_results(secret_number, guess_from_user):
        if secret_number == guess_from_user:
            ismatch = True
        else:
            ismatch = False
        return ismatch

    def play(difficulty):
        secret_number = int(Guess_game.generate_number(difficulty))
        guess_from_user = int(Guess_game.get_guess_from_user(difficulty))
        result = Guess_game.compare_results(secret_number, guess_from_user)
        if result:
            print("You win!!!!")
        else:
            print("You lose :(")

