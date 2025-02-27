import random


def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    print(f'enter a number between 0 and {difficulty}:')
    while True:
        try:
            guess_from_user = int(input())
            if 0 <= guess_from_user <= difficulty:
                print(f'You guessed: {guess_from_user}')
                return int(guess_from_user)
            else:
                print(f'Invalid input. Please enter a number between 0 and {difficulty}:')
        except ValueError:
            print(f'Invalid input. Please enter a number between 0 and {difficulty}:')


def compare_results(secret_number, guess_from_user):
    if secret_number == guess_from_user:
        return True
    else:
        return False


def play(difficulty):
    secret_number = int(generate_number(difficulty))
    guess_from_user = int(get_guess_from_user(difficulty))
    print(f'random number is: {secret_number}')
    result = compare_results(secret_number, guess_from_user)
    if result:
        return True
    else:
        return False

