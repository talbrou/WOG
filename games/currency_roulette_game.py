import requests
import random
import sys
from currency_converter import CurrencyConverter


def get_money_interval(difficulty):
	c = CurrencyConverter()
	currency = (c.convert(1, 'USD', 'ILS'))
	interval = 10 - difficulty
	return currency, interval


def get_guess_from_user(random_amount):
	while True:
		try:
			user_guess = float(input(f'Guess the converted value of {random_amount}USD to ILS'))
			return user_guess
		except:
			print('Invalid input. Please enter a valid number')
		
		
def compare_results(difficulty, random_amount):
	currency_and_interval = get_money_interval(difficulty)
	currency = currency_and_interval[0]
	converted_amount = currency*random_amount
	user_guess = get_guess_from_user(random_amount)
	interval = int(currency_and_interval[1])
	print(f'You guessed: {user_guess}. The answer is: {converted_amount}')
	if (user_guess < converted_amount and user_guess + interval < converted_amount) or (user_guess > converted_amount and user_guess - interval > converted_amount):
		return False
	else:
		return True


def play(difficulty):
	random_amount = random.randint(1, 100)
	get_money_interval(difficulty)
	return compare_results(difficulty, random_amount)