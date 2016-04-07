import pyglet
import tkinter as tk
from tkGUI import Application

app = Application()


window = pyglet.window.Window()

@window.event
def on_draw():

    print("fizz")
    window.clear()

def on_update(time):
    app.update_idletasks()
    app.update()

if __name__ == '__main__':
    pyglet.clock.schedule(on_update)
    pyglet.app.run()