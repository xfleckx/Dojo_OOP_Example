from BaseTrial import BaseTrial

class NumberTrial(BaseTrial):
    """description of class"""

    def __init__(self):
        self._instruction = "Please guess a number between 0-9"
        self.availableValues = [0,1,2,3,4,5,6,7,8,9]