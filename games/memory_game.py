import random
import time
from scoring.utils import *


def generate_sequence(difficulty):
    i = 0
    generated_list = []
    while i < difficulty:
        generated_list.append(random.randint(1, 101))
        i += 1
    return generated_list


def get_list_from_user(difficulty, generated_list):
    Screen_cleaner()
    print(f'Are you ready to see your sequence? Focus, because it will not be up there for long!')
    time.sleep(3)
    count = 3
    while count > 0:
        print(f'In {count} seconds...')
        time.sleep(1)
        count -= 1
    time.sleep(0.7)
    print(generated_list)
    time.sleep(0.7)
    Screen_cleaner()

    print(f'Enter the {difficulty} numbers list with a comma between each number:')
    while True:
        try:
            raw_list = input()
            user_list = f'[{raw_list}]'
            processed_list = eval(user_list)
            return processed_list
        except:
            print('Invalid input! Please enter a valid list!')


def is_list_equal(difficulty, generated_list, processed_list):
    if generated_list == processed_list:
        return True
    else:
        return False


def play(difficulty):
    generated_list = generate_sequence(difficulty)
    processed_list = get_list_from_user(difficulty, generated_list)
    print(f'Original sequence: {generated_list}')
    print(f'Your sequence: {processed_list}')
    return is_list_equal(difficulty, generated_list, processed_list)
