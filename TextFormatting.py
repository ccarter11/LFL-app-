
from graphics import *

def main():
    win = GraphWin("My Window", 600, 900)
    #win = win.setBackground(color_rgb(0,0,0))

    txt = Text(Point(300,450),"What's up?")
    txt.draw(win)
    
    win.getMouse()
    win.close()

                            
    
