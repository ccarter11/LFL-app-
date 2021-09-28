# READING TXT FILES

from random import sample
from graphics import *

def readfile():

    # Open adultCategories.txt file and read from it
    # Splits each newline and omits "/n" from being in the list
    with open('adultCategories.txt','r',encoding="utf8") as file:
        adultCatList = file.read()
        adultCatList = adultCatList.splitlines()
        print(adultCatList)

    #with open('kidCategories.txt','r') as file:
        #kidCatList = file.read().splitlines()
        #print(kidCatList)

    #Sample 24 random elements from list (does not repeat elements)
        
    adultCatRandom = sample(adultCatList,24)
    #print(adultCatRandom)

    #kidCatRandom = sample(kidCatList,24)
    #print(kidCatList)
    return adultCatRandom

    # Now must plot strings from list into GUI
#bingo card program 


#import bingo data

def setcoords():
   

    xo=147-((147-41)/2)
    yo=292-((292-188)/2)
    xm=106
    ym=104

#generate list of midpoints
    s=[]

    for i in range(0,5):
        for j in range(0,5):
            x=xo + i*xm
            y=yo + j*ym
            pnt=Point(x,y)
            s.append(pnt)
            
    #print(s) 
    return s
def main():
    win = GraphWin("Card", 600, 900)
    img = Image(Point(300,450), "bcgraphic.gif")
    img.draw(win)
    acats= readfile()
    coords = setcoords()
    lbls=[]
    #print(len(acats))
    #print(len(coords))
    for i in range(0,25):
        if (i <12):
            lbls.append(Text(coords[i],acats[i]))
        if(i>12):
            lbls.append(Text(coords[i],acats[i-1]))
    print(len(lbls))
    for i in range(0,24):
        lbls[i].draw(win)

        
    #txt = Text(Point(300,450),"What's up?")
    #txt.draw(win)


main()
