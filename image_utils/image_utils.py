#!/usr/bin/python
from PIL import Image

# helpers for image manipulation

def convert_image(orig_image, new_image, image_type):
    print ("convert_image...")
    image = Image.open(orig_image)
    if image.mode != 'RGB':
        print ("rgb... stuff")
        image = image.convert('RGB')

    image.save(new_image, image_type)

def compress_image(image, new_image, quality):
    image = Image.open(image)
    image.save(new_image,optimize=True,quality=quality)
