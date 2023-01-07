#!/usr/bin/env python3

# I got tired of using a web converter like https://convertio.co/ to convert images,
# so I am making my own, it's still a work in progress as I add features and extra image formats.
# Original intent was to just make a function I could pass arguments to, but now I'm considering expanding use cases

# command is currently used to install modules with pip if not already installed
import subprocess, sys
command = subprocess.os.system

# asks the user if they want to install pillow if it isn't already installed
def ask():
    # strip() will remove extra spaces, lower() will lower the cases
    answer = input("Do you want to install pillow now? y/n?  ").strip().lower()
    # linux is for GNU/Linux
    if (answer == 'y') and (sys.platform == 'linux'):
        command("pip3 install pillow")
    # win32 will work regardless if the windows is 32 or 64 bit
    elif (answer == 'y') and (sys.platform == 'win32'):
        command("pip install pillow")
    # darwin is for mac
    elif (answer == 'y') and (sys.platform == 'darwin'):
        command("pip3 install pillow")
    elif (answer == 'n'):
        print("You need pillow to run this, exiting")
        quit()
    else:
        print("please use y/n")
        ask()
        

# We need PIL (from pillow)
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
# I was using opencv-python and webptools but those modules were giving "permission denied" errors
try:
    from PIL import Image
except(ImportError):
    print("You need the pillow module to use this")
    ask()


def convert_image(path_to_image_being_converted, format_we_want_image_to_be_in):

    # Below is the docstring that will show up if you do help(convert_image) in a terminal like iPython
    '''
    def convert_image(path_to_image_being_converted, format_we_want_image_to_be_in):
    
    
    convert_image function will convert an image to a given format.
    The arguments should be pretty self explanatory.
    
    path_to_image_being_converted is the path, example:
    /home/user/Pictures/image.jpg
    
    format_we_want_image_to_be_in is, well, the format you want to convert the image to.
    
    So far you can do:
    from .jpg to .png
    from .png to .jpg
    
    from .jpg to webp
    from webp to .jpg
    
    from png to webp
    from webp to .png
    
    '''
    # image_type is the image extension, like .jpg, webp, etc...
    # we grab the last 4 characters of filename with an index to find out if
    # it's .jpg, jpeg, webp, etc.
    image_type = path_to_image_being_converted[-4:]
    

    # list of available image formats
    # might add more
    available_image_format_list = ["jpeg", "webp", ".jpg", ".png"]

    # Check if the requested format is available, if it isn't
    # then we say it isn't and quit
    if image_type not in available_image_format_list:
        print("Sorry, that format not is not available")
        quit()
    
    # from jpg to png
    # tested, it works fine
    if (image_type == ".jpg") & (format_we_want_image_to_be_in == ".png"):
        try:
            image = Image.open(path_to_image_being_converted).convert("RGB")
            return image.save("{}.png".format(path_to_image_being_converted), "png")
        except(OSError):
            print("OSError was raised\n")
            print("PIL (pillow) gives an OSError when file can't be opened")
            print("this usually happens when you try to convert a corrupted file")
            quit()
    
    # from png to jpg
    # THIS DOES NOT WORK YET
    # Does not work yet
    # /usr/lib/python3/dist-packages/PIL/Image.py in save(self, fp, format, **params)
    # 1981             save_handler = SAVE_ALL[format.upper()]
    # 1982         else:
    # -> 1983             save_handler = SAVE[format.upper()]
    # 1984 
    # 1985         if open_fp:
    # KeyError: 'JPG'
    
    elif (image_type == ".png") & (format_we_want_image_to_be_in == ".jpg"):
        try:
            image = Image.open(path_to_image_being_converted).convert("RGB")
            return image.save("{}.jpg".format(path_to_image_being_converted), "jpg")
        except(OSError):
            print("OSError was raised\n")
            print("PIL (pillow) gives an OSError when file can't be opened")
            print("this usually happens when you try to convert a corrupted file")
            quit()
        
    # from .jpg to webp
    # tested it with gthumb, it works!
    
    # You can't use imgage viewer on Debian to open webp
    # you need to use gthumb to test | https://packages.debian.org/search?keywords=gthumb
    # sudo apt install gthumb
    elif (image_type == ".jpg") & (format_we_want_image_to_be_in == "webp"):
        try:
            image = Image.open(path_to_image_being_converted).convert("RGB")
            return image.save("{}.webp".format(path_to_image_being_converted), "webp")
        except(OSError):
            print("OSError was raised\n")
            print("PIL (pillow) gives an OSError when file can't be opened")
            print("this usually happens when you try to convert a corrupted file")
            quit()
            
    # from webp to .jpg
    # Does not work yet
    # /usr/lib/python3/dist-packages/PIL/Image.py in save(self, fp, format, **params)
    # 1981             save_handler = SAVE_ALL[format.upper()]
    # 1982         else:
    # -> 1983             save_handler = SAVE[format.upper()]
    # 1984 
    # 1985         if open_fp:
    # KeyError: 'JPG'

    elif (image_type == "webp") & (format_we_want_image_to_be_in == ".jpg"):
        try:
            image = Image.open(path_to_image_being_converted).convert("RGB")
            return image.save("{}.jpg".format(path_to_image_being_converted), "jpg")
        except(OSError):
            print("OSError was raised\n")
            print("PIL (pillow) gives an OSError when file can't be opened")
            print("this usually happens when you try to convert a corrupted file")
            quit()
            
    # from webp to .png
    # convert_image('/home/ueser/test/chad.jpg.webp', '.png')
    # Works fine
    elif (image_type == "webp") & (format_we_want_image_to_be_in == ".png"):
        try:
            image = Image.open(path_to_image_being_converted).convert("RGB")
            return image.save("{}.png".format(path_to_image_being_converted), "png")
        except(OSError):
            print("OSError was raised\n")
            print("PIL (pillow) gives an OSError when file can't be opened")
            print("this usually happens when you try to convert a corrupted file")
            quit()
            
            
    else:
        print("Sorry, an error occured, or that conversion is not available due to unsupported format")
        
        
        
        
        
