#bingo card program 


#import bingo data
from graphics import *

win = GraphWin("Card", 600, 900)
img = Image(Point(300,450), "bcgraphic.gif")
img.draw(win)


xo=147-((147-41)/2)
yo=292-((292-188)/2)
xm=106
ym=104

#generate list of midpoints
s=[]

for i in range(0,4):
    for j in range(0,4):
        x=xo + i*xm
        y=yo + j*ym
        pnt=Point(x,y)
        s.append(pnt)
print(s) 
    



