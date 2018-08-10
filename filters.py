# user interface that people will use to interact with library
# import filters library into this script

from PIL import Image


# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    image = Image.open(filename)
    return image



# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(image):
    image.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(image, filename):
    image.save(filename, "jpeg")
    show_img(image)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(image):
    darkBlue = (0,51,76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 156)
    yellow = (252, 227, 166)

    image_list = image.getdata()
    image_list = list(image_list)
    recolored = []

    for pixel in image_list:
        intensity = pixel[0]+pixel[1]+pixel[2]
        if intensity < 102:
            recolored.append(darkBlue)
        elif intensity < 364:
            recolored.append(red)
        elif intensity < 546:
            recolored.append(lightBlue)
        else:
            recolored.append(yellow)
    new_image = Image.new("RGB",image.size)
    new_image.putdata(recolored)
    new_image.show()
    new_image.save("newImage.jpg","jpeg")
