from Paradigm import Paradigm
from AlternativeParadigm import AlternativeParadigm
# define some constants
START_PARADIGM = "s"

DEMO_TRIAL_CONFIG = [ ('Number', 1), ('Character', 1) ]

def OnUserInputRequired(prompt): # actual implementation of how the user input should be performed
    return input(prompt)

'''The application entry point'''
if __name__ == "__main__":
    
    #paradigmInstance = Paradigm() # create an instance
    paradigmInstance = AlternativeParadigm(OnUserInputRequired) # an example for slightly different paradigm implementation
    paradigmInstance.setup(DEMO_TRIAL_CONFIG)

    userInput = None
    while userInput != START_PARADIGM:
        userInput = input("Press s to start the paradigm\n>") 
        
    paradigmInstance.start()
   
