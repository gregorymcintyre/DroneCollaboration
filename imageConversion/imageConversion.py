from PIL import Image
import PIL.ImageOps  
import numpy as np  

image = Image.open('crop.png')
print("Processing image...")
inverted_image = PIL.ImageOps.invert(image)
print("Image inverted")
gray_file= inverted_image.convert('LA') # convert grey
print("Image converted to greyscale")
resize_image = gray_file.resize((600, 600))
print("Image resized to 600px x 600px")
#resize_image.save('resize_image.png')
background = Image.open("background.pgm")
background.convert('LA')
background.paste(resize_image, (0, 0), background)
print("Image merged with background.pgm")
background.save('output.png')
print("Image Processing complete: image output output.pgm")
