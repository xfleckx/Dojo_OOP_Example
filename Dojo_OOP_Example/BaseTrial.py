from random import randint

class BaseTrial(object):
    """A base class defines the common structure and behaviour of \
    a family of classes"""
   
    def __init__(self):
       self._instruction = None
       self.availableValues = []
       self.expectedValueFromGuessing = None

    def getInstruction(self):
        return self._instruction

    def expectAValue(self):
        randomIndex = randint(0, len(self.availableValues))
        self.expectedValueFromGuessing = self.availableValues[randomIndex]

    def expectedMatches(self, guess):
        return guess == self.expectedValueFromGuessing

