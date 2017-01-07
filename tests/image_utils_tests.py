import unittest
from file_utils import file_utils
from image_utils import image_utils

class UtilsTests(unittest.TestCase):
    def test_convert_image(self):
        orig_image = 'tests/images/cabelas-inc.png'
        new_image = 'tests/images/cabelas-inc.jpeg'
        image_utils.convert_image(orig_image, new_image, 'JPEG')
        self.assertTrue(file_utils.check_file_exists(new_image))
        file_utils.remove_file(new_image)

        orig_image = 'tests/images/penntex-midstream-partners.jpg'
        new_image = 'tests/images/penntex-midstream-partners.jpeg'
        image_utils.convert_image(orig_image, new_image, 'JPEG')
        self.assertTrue(file_utils.check_file_exists(new_image))
        file_utils.remove_file(new_image)

        orig_image = 'tests/images/jerry-e-sheridan.gif'
        new_image = 'tests/images/jerry-e-sheridan.jpeg'
        image_utils.convert_image(orig_image, new_image, 'JPEG')
        self.assertTrue(file_utils.check_file_exists(new_image))
        file_utils.remove_file(new_image)

    def test_compress_image(self):
        image = 'tests/images/cabelas-inc.png'
        new_image = 'tests/images/cabelas-inc-compressed.png'
        image_utils.compress_image(image, new_image, 40)
        image_file_size = file_utils.get_file_size(image)
        self.assertLess(file_utils.get_file_size(new_image), image_file_size)
        file_utils.remove_file(new_image)

        image = 'tests/images/cabelas-inc.png'
        new_image = 'tests/images/cabelas-inc-copy.png'
        file_utils.copy_file(image, new_image)
        image_file_size = file_utils.get_file_size(new_image)
        image_utils.compress_image(new_image, new_image, 40)
        self.assertLess(file_utils.get_file_size(new_image), image_file_size)
        file_utils.remove_file(new_image)

    def test_get_image_size(self):
        image = 'tests/images/cabelas-inc.png'
        width, height = image_utils.get_image_size(image)
        self.assertEqual(width, 250)
        self.assertEqual(height, 150)

    def test_resize_image_scale(self):
        filename = 'tests/images/cabelas-inc.png'
        new_filename = 'tests/images/cabelas-inc-resize.png'
        scale = 16
        image_utils.resize_image_scale(filename, new_filename, scale)
        width, height = image_utils.get_image_size(filename)
        self.assertEqual(width, 250)
        self.assertEqual(height, 150)
        width, height = image_utils.get_image_size(new_filename)
        self.assertEqual(width, 16)
        self.assertEqual(height, 9)
        file_utils.remove_file(new_filename)



# IMAGE_PATH=/Library/WebServer/Documents/python_image_utils/tests/images/ python -m unittest discover -s tests -p "*_tests.py"
