import unittest
from image_processing import processor

class TestStringMethods(unittest.TestCase):

    def test_should_read_image_from_source(self):
        img = processor.create_image_from("../samples/Toledo/sources/0001-enf.jpg")
        self.assertIsNotNone(img, "Image not loaded!")

if __name__ == '__main__':
    unittest.main()
