# Team 3: Madison Ford, Clayton Carter, Garzain Kabir, Phillip Chandy

# Adult Bingo Card Generator

# Program that reads .txt file of adult bingo card categories and generetes a randomzied unique bingo card.


from PIL import Image, ImageDraw, ImageFont
import textwrap
from random import sample 

def readfile():

    # Open adultCategories.txt file and read from it
    # Splits each newline and omits "/n" from being in the list
    with open('adultCategories.txt','r',encoding="utf8") as file:
        adultCatList = file.read()
        adultCatList = adultCatList.splitlines()
        
    #Sample 24 random elements from list (does not repeat elements)    
    adultCatRandom = sample(adultCatList,24)
    return adultCatRandom


def setcoords():
    xo=80 # Middle x coord of first box
    yo=240 # Middle y coord of first box
    xm=105 # x length to middle of next box
    ym=105 # y length to middle of next box

#generate list of midpoints
    s=[]

    for i in range(0,5):
        for j in range(0,5):
            x=xo + i*xm
            y=yo + j*ym
            pnt= (x,y)
            s.append(pnt)
            
    #print(s) 
    return s

def main():
    img = Image.open( "bingocardgraphic.jpeg")
    draw = ImageDraw.Draw(img)
    font_size = 12
    font = ImageFont.truetype("Arial Black.ttf", size=font_size)
    wrapper=textwrap.TextWrapper(width=13)
    acats= readfile()
    coords = setcoords()
    
    
    for i in range(25):
        if (i <12):
            if len(acats[i]) > 50: # To prevent run-off make font smaller
                font = ImageFont.truetype("Arial Black.ttf", size=10)
            draw.text(coords[i], wrapper.fill(text =acats[i]), font = font , align ="center" , fill = "black", anchor ="mm")
            font = ImageFont.truetype("Arial Black.ttf", size=12)
        if(i>12):
            if len(acats[i-1]) > 50:
                font = ImageFont.truetype("Arial Black.ttf", size=10)
            draw.text(coords[i], wrapper.fill(text= acats[i-1]), font = font , align ="center" , fill = "black", anchor ="mm")
            font = ImageFont.truetype("Arial Black.ttf", size=12)
        
    img.show() #opens graphic in computer's default image previewer
    #im.save("Bingo Card.jpeg") #creates a new jpeg file


main()
