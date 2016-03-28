from Paradigm import Paradigm
from NumberTrial import NumberTrial
from CharacterTrial import CharacterTrial

class AlternativeParadigm(Paradigm):
    """An example to demonstrate how overriding could be use to provide a 
       alternative implementation without a single line of duplicated code
    """

    def __init__(self, OnAwaitUserInput):
        self.OnAwaitUserInput = OnAwaitUserInput # uses callbacks to give the actual 
        return super().__init__()

    def _createAndAppendThe(self, expectedTrial): # a more generic implementation 
        newTrial = eval(expectedTrial+"Trial")()  # this is not secure... one typo ruins everything
        self._trials.append(newTrial)

    def _expectUserInputFor(self, trial):
        instructionForUserInput = trial.getInstruction()
        return self.OnAwaitUserInput(instructionForUserInput)


