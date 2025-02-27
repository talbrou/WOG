import os
import sys

if os.name == 'nt': 
    SCORES_FILE_NAME = "scoring/scores.txt"
else:
    SCORES_FILE_NAME = "/scoring/scores.txt"

BAD_RETURN_CODE = "null"

def Screen_cleaner():
    os.system('cls')