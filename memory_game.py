import random, sys, time, os

class Memory_game: 
    def generate_sequence(difficulty):
        i = 0
        generated_list = []
        while i < difficulty:
            generated_list.append(random.randint(1, 101))
            i += 1
        return generated_list
    
    def get_list_from_user(difficulty, generated_list):
        os.system('cls')
        print(f'Are you ready to see your {difficulty} numbers? Focus, because they will not be up there for long!')
        time.sleep(3)
        count = 5
        while count > 0:
            print(f'In {count} seconds...')
            time.sleep(1)
            count -= 1
        time.sleep(0.7)
        os.system('cls')
        print(generated_list)
        time.sleep(0.7)
        os.system('cls')
        try:
            raw_list = input(f'insert the {difficulty} long list with a comma between each number')
            user_list = f'[{raw_list}]'
            processed_list = eval(user_list)
            return processed_list
        except:
            sys.exit('error: Invalid input! Please enter a valid list!')
    
    def is_list_equal(difficulty, generated_list, processed_list):
        if generated_list == processed_list:
            return True
        else:
            return False

    def play(difficulty):
        generated_list = Memory_game.generate_sequence(difficulty)
        processed_list = Memory_game.get_list_from_user(difficulty, generated_list)
        print(f'Original numbers: {generated_list}')
        print(f'Your numbers: {processed_list}')
        return Memory_game.is_list_equal(difficulty, generated_list, processed_list)