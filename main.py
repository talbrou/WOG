from app import *
from guess_game import Guess_game
from currency_roulette_game import Currency_roulette_game, Currency_convertor

welcome()

# run start_play function
start_play_answers = start_play()
game = start_play_answers[0]
difficulty = start_play_answers[1]

Guess_game.play(difficulty)
