from PIL import Image, ImageDraw, ImageFont
import textwrap


def main():

    catString = "Books about plants or gardening"
  
    # Wrap this text.
    wrapper = textwrap.TextWrapper(width=14)
    editedString = wrapper.fill(text=catString)

  
    im = Image.open("bingocardgraphic.jpeg")
    draw = ImageDraw.Draw(im)
    
    font_size = 12
    font = ImageFont.truetype("Arial Black.ttf", size=font_size)
    draw.text((80, 240), editedString, font=font, align = "center", fill ="black", anchor = "mm")

    im.show()
    #im.save(output_path)



##def TextMaker(string):
##    words = string.split()
##    print(words)
##    numWords = len(words)
##    print(numWords)
##    counter = 0
##    finalString = ''
##    for word in words:
##        numChar = len(word)
##        if numChar > 14:
##            word = word[0:13] + '-\n' + word[13:]
##            finalString.join(word)
##            counter = len(word[13:])
##            break
##        if counter + numChar >14:
##            finalString.join("\n")
##            finalString.join(word)
##            counter = numChar
##        if counter + numChar < 14:
##            finalString.join(word)
##            counter += numChar

####    return finalString
       # if numChar <= 14:
        #    finalString.join(word)
        #    counter += numChar
        
        
        
        
    
    
    
