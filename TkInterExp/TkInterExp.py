from Tkinter import *
from time import time
import sys

class App:

    def __init__(self):
        self.root = Tk()
        self.updateRate = 30 #ms
        self.lastUpdateOnContinous = time()
        self.lastUpdateOnRenderLoop = time()
        self.root.after(self.updateRate, self.run_continous)

        #self.root.mainloop()
        
    def run_continous(self):
        self.root.after(self.updateRate, self.run_continous)
        current = time()
        delta = current - self.lastUpdateOnContinous
        self.lastUpdateOnContinous = current 

        self.UpdateAllElements(delta)

        print("Continous delta ", delta)    
       
    def getDeltaTime(self, lastUpdate):
        return delta

    def startRendering(self):
        while True:
            current = time()
            delta = current - self.lastUpdateOnRenderLoop
            self.lastUpdateOnRenderLoop = current     
            print("Renderloop delta ", delta)    
            self.root.update()
            self.root.update_idletasks()
            
if __name__ == "__main__":
    a = App()
    a.startRendering()