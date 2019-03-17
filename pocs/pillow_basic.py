from __future__ import print_function
from datetime import datetime
from PIL import Image

#These will be part of the script configuration.
SOURCE_PATH = "samples/Toledo/sources"
SAMPLE_IMAGE_PATH = SOURCE_PATH + "/0001-enf.jpg"
SAMPLE2_IMAGE_PATH = SOURCE_PATH + "/0384-enf.jpg"
OUTPUT_PATH = "samples/Toledo/output"

base_image = Image.open(SAMPLE_IMAGE_PATH)
print(base_image.format, base_image.size, base_image.size[0], base_image.size[1], base_image.mode)

#base_image.show()
output_file_name = OUTPUT_PATH + "/" + datetime.today().strftime('%Y%m%d-%H%M%S') + ".tiff"
outputImage = base_image.save(output_file_name)

savedImage = Image.open(output_file_name)
print(savedImage.format, base_image.format)
