#!/usr/bin/python3

# I got tired of using a web converter like https://convertio.co/ to convert images,
# so I am making my own, it's still a work in progress as I add features and extra image formats.
# Original intent was to just make a function I could pass arguments to, but now I'm considering expanding use cases

import subprocess
command = subprocess.os.system

# We need PIL and cv2 to convert from Webp to Jpeg
try:
    from PIL import Image
except(ImportError):
    print("You need to install pillow")
    print("Run 'pip3 install pillow' to install it on GNU/Linux")
    print("Run 'pip install pillow' to install it on Windows")
    quit()

try:
    import cv2
except(ImportError):
    print("You need to install cv2")
    print("Run 'pip3 install opencv-python' to install it on GNU/Linux")
    print("Run 'pip install opencv-python' to install it on Windows")
    quit()
    
# we need to import cwebp from webptools to convert from jpeg to webp
try:
    from webptools import cwebp
except(ImportError):
    print("You need to install webptools")
    print("Run 'pip3 install webptools' to install it on GNU/Linux")
    print("Run 'pip install webptools' to install it on Windows")
    quit()

def convert_image(path_to_image_being_converted, format_we_want_image_to_be_in):
    '''
    convert_image will convert an image to a given format.
    Available formats are: jpeg
    
    '''
    # image_type is the image extension, like .jpg, .webp, etc...
    # we grab the last 4 characters of filename to find out if
    # it's .jpg, jpeg, webp, etc.
    image_type = path_to_image_being_converted[-4:]
    

    # list of available image formats
    available_image_format_list = ["jpeg", "webp"]

    # Check if the requested format is available, if it isn't
    # then we say it isn't and quit
    if image_format not in image_format_list:
        print("Sorry, that format not is not available")
        quit()
    
    # from webp to jpeg
    if (image_type == "webp") & (format_we_want_image_to_be_in == "jpeg"):
        image = cv2.imread(path_to_image)
        #OpenCV uses BGR color space by default
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        Image.fromarray(image).save("{}.jpeg".format(path_to_image_being_converted), "jpeg")
        
    # from .jpg to webp
    elif (image_type == ".jpg") & (format_we_want_image_to_be_in == "webp"):
       cwebp(input_image=path_to_image_being_converted, output_image="{}.webp".format(path_to_image_being_converted), option="-q 80", logging="-v")
        
