# Python_Image_Converter
## As of January 12th 2023, everything works now!
Please note .jpeg and .jpg are the exact same format, so there's no need to convert from .jpeg to .jpg and vice versa.
## Background
I got tired of using a web converter like https://convertio.co/ to convert images, so I made my own.
<br />
Everything works now, but I might update it later.

My initial intent when coding this was just simply making a function that I could import into iPython and then give the function the following arguments:
1. A path to the image I want to convert
2. A format I want to convert it in

As I began coding, I thought of more ideas and use cases. So currently debating myself if I should just leave this as a function or update features such as adding more image formats or adding a gui, the ideas are endless tbh. 

## To use
To use this you have two options:
1. Copy and paste the entire function into an interpreter like iPython
2. Import it into your interpreter directly
<br />
Then call the function with the arguments. Example:
<br /><br />
convert_image('/home/user/test/chad.webp', '.jpg')
<br />
You should see chad.wbp.jpg in the directory now.
<br />
When I was testing this program, I made sure it actually changed formats, it works.
<br /> <br />
Will try to convert this code into something more modular later so it can be easily copied and pasted when making modules, classes, functions, etc.
<br /><br />
For now, enjoy and hope you find this useful for either converting images or learning Python!
