import random

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""

        alpha = 'abcdefghijklmnopqrstuvwxyz'
        i = 0
        nine_letters = []
        while i < 9:
            position = random.randrange(0,25)
            nine_letters.append(alpha[position])
            i = i + 1

        self.grid = nine_letters


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        pass # TODOpoetry run
