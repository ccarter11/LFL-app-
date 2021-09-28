# READING TXT FILES

from random import sample

def main():

    # Open adultCategories.txt file and read from it
    # Splits each newline and omits "/n" from being in the list
    with open('adultCategories.txt','r') as file:
        adultCatList = file.read().splitlines()
        print(adultCatList)

    with open('kidCategories.txt','r') as file:
        kidCatList = file.read().splitlines()
        #print(kidCatList)

    #Sample 24 random elements from list (does not repeat elements)
        
    adultCatRandom = sample(adultCatList,24)
    print(adultCatRandom)

    kidCatRandom = sample(kidCatList,24)
    print(kidCatList)
    print("hi")

    # Now must plot strings from list into GUI
    
