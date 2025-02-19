import os
from utils import SCORES_FILE_NAME

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty) * 3 + 5
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read())
        TOTAL_SCORE = current_score + POINTS_OF_WINNING
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(TOTAL_SCORE))
    else:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(POINTS_OF_WINNING))
