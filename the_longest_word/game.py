# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""

        alpha = 'abcdefghijklmnopqrstuvwxyz'
        i = 0
        nine_letters = []
        while i < 9:
            position = random.randrange(0,25)
            nine_letters.append(alpha[position].upper())
            i = i + 1

        self.grid = nine_letters

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if len(word)==0:
            return False

        for letter in word:
            if letter not in self.grid:
                return False
            else:
<<<<<<< HEAD
                response = requests.get(f"https://dictionary.lewagon.com/{word}")
                json_response = response.json()
                return json_response['found']
=======
                return True
>>>>>>> 9b0a918202a7398bcca4ea548506eff30a434699
