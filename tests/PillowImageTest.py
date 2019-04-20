import unittest
import numpy as np
from PIL import Image

# This Unit test is used to check how the Pillow Image library features that
# are used by the hdtr Image processor is used.
# The purpose of this tests is to experient, play around and dcoument how the
# different Image functions provided by PIL work.
class PillowImageTest(unittest.TestCase):

    def test_composite_images(self):
        image1 = Image.open('./samples/Toledo/sources/0001-enf.jpg')
        image2 = Image.open('./samples/Toledo/sources/0384-enf.jpg')
        mask = Image.open('./samples/Toledo/test-check/gradient_mask.tiff')
        composite = Image.composite(image1, image2, mask)
        
        expected_composite = Image.open('./samples/Toledo/test-check/composite-001-0384-w-mask.tiff')

        np.testing.assert_array_equal(np.array(composite), 
                                      np.array(expected_composite), 
                                      "Image arrays are not equal")
        
        

if __name__ == '__main__':
    unittest.main()