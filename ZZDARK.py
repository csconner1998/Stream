import os
from PIL import Image
def darken(imagePath,dir,number):
    # Open the image
    im = Image.open(imagePath)

    # Convert the image to RGBA format, which allows us to access the alpha channel
    im = im.convert("RGBA")

    # Get the width and height of the image
    width, height = im.size

    # Loop through all pixels in the image
    for x in range(width):
        for y in range(height):
            # Get the pixel at (x, y)
            pixel = im.getpixel((x, y))
            # Check if the pixel is transparent
            if pixel[3] == 0:
                # If the pixel is transparent, do nothing
                continue
            # If the pixel is not transparent, set it to black
            im.putpixel((x, y), (0, 0, 0, 255))

    # Save the modified image
    im.save("./dark/" + dir + str(number) + ".png")
    os.rename(imagePath, "./color/" + dir + str(number) + ".png")

dirNames = os.listdir("./color")
for dir in dirNames:
    images = os.listdir("./color/" + dir)
    for i in range(len(images)):
        print(images[i])
        darken("./color/" + dir + "/"+images[i],dir,i)