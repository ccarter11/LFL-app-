# READING TXT FILES

from random import sample

def main():

    # Open adultCategories.txt file and read from it
    # Splits each newline and omits "/n" from being in the list
    with open('adultCategories.txt','r',encoding="utf8") as file:
        adultCatList = file.read().splitlines()
        print(adultCatList)

    with open('kidCategories.txt','r',encoding="utf8") as file:
        kidCatList = file.read().splitlines()
        #print(kidCatList)

    #Sample 24 random elements from list (does not repeat elements)
        
    adultCatRandom = sample(adultCatList,24)
    print(adultCatRandom)

    kidCatRandom = sample(kidCatList,24)
    print(kidCatList)
   

    # Now must plot strings from list into GUI
    
