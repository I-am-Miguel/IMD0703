import sys
from PIL import Image

if __name__ == "__main__":

    message = sys.argv[1]
    picture = Image.open('mario.bmp')
    pix = picture.load()
    print(picture.size)
    print pix

    for palavra in message:
        print(palavra)

    
    #im = Image.open('dead_parrot.jpg') # Can be many different formats.
    #pix = im.load()
    #print im.size  # Get the width and hight of the image for iterating over
    #print pix[x,y]  # Get the RGBA Value of the a pixel of an image
    #pix[x,y] = value  # Set the RGBA Value of the image (tuple)
    #im.save('alive_parrot.png')
    
    picture.close()