from BaseTrial import BaseTrial
from string import ascii_lowercase

class CharacterTrial(BaseTrial):
    """description of class"""

    def __init__(self):
        self._instruction = "Please guess a character from a-z"
        self.availableValues = ascii_lowercase
