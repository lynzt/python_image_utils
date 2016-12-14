#!/usr/bin/python
from PIL import Image

# helpers for image manipulation

def convert_image(orig_image, new_image, image_type):
    image = Image.open(orig_image)
    image.save(new_image, image_type)

def compress_image(image, new_image, quality):
    image = Image.open(image)
    image.save(new_image,optimize=True,quality=quality)
