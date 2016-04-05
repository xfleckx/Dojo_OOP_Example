from BaseTrial import BaseTrial
from NumberTrial import NumberTrial
from CharacterTrial import CharacterTrial

class Paradigm:
    """A example implementation of a paradigm context"""
    def __init__(self):
        """the optional constructor of our paradigm implementation"""
        self._trials = [] # private variables _ convention

    def setup(self, expectedTrials):
        for expectedTrial in expectedTrials:
            for _ in range(expectedTrial[1]): # idiomatic way of doing something n times '_' is used for an unused variable
                self._createAndAppendThe(expectedTrial[0])

    def _createAndAppendThe(self, expectedTrial): # these if statements can also be reduced but advanced stuff - example for overriding the paradigm class
            if expectedTrial == "Number":
                newNumberTrial = NumberTrial()
                self._trials.append(newNumberTrial)
            elif expectedTrial == "Character":
                newCharacterTrial = CharacterTrial()
                self._trials.append(newCharacterTrial)
            else:
                raise ValueError("Expected Trial Type not implemented") # exceptions are also Objects 

    def start(self):
        """Begin the paradigm with the first trial"""
        for trial in self._trials:
            self._run(trial)

    def _run(self, trial:BaseTrial): # a function annotation to give the programmer more infos about how the function should be used!
        trial.expectAValue()
        userInput = self._expectUserInputFor(trial)
        if trial.expectedMatches(userInput):
            self._reportCorrectGuessOn(trial)
        else:
            self._reportWrongGuessOn(trial)

    # example for bad abstraction... paradigm knows where the user input comes from...
    def _expectUserInputFor(self, trial):
        return input(trial.getInstruction() + "\n>")

    # TODO callbacks her just publishing a formated string... the paradigm doesn't care how to safe
    def _reportWrongGuessOn(self, trial): 
        print("Wrong")

    def _reportCorrectGuessOn(self, trial):
        print("Correct")