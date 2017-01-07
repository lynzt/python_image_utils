#!/usr/bin/python
from PIL import Image

# helpers for image manipulation

def convert_image(orig_image, new_image, image_type):
    image = Image.open(orig_image)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    image.save(new_image, image_type)

def resize_image_scale(orig_image, new_image, scale):
    width, height = get_image_size(orig_image)
    new_width = int(round(width/scale))
    new_height = int(round(height/scale))
    image = Image.open(orig_image)
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    image.save(new_image)

def compress_image(image, new_image, quality):
    image = Image.open(image)
    image.save(new_image,optimize=True,quality=quality)

def get_image_size(image):
    image = Image.open(image)
    return image.size
