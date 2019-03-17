from __future__ import print_function
from datetime import datetime
from PIL import Image

#These will be part of the script configuration.
SOURCE_PATH = "samples/Toledo/sources"
SAMPLE_IMAGE_PATH = SOURCE_PATH + "/0001-enf.jpg"
SAMPLE2_IMAGE_PATH = SOURCE_PATH + "/0384-enf.jpg"
OUTPUT_PATH = "samples/Toledo/output"

def save_as_tiff(image):
    output_file_name = OUTPUT_PATH + "/" + datetime.today().strftime('%Y%m%d-%H%M%S%f') + ".tiff"
    outputImage = image.save(output_file_name)
    return Image.open(output_file_name)

base_image = Image.open(SAMPLE_IMAGE_PATH)
print(base_image.format, base_image.size, base_image.size[0], base_image.size[1], base_image.mode)
savedImage = save_as_tiff(base_image)

image2 = Image.open(SAMPLE2_IMAGE_PATH)
print(image2.format, image2.size, image2.mode)

width = base_image.size[0]
height = base_image.size[1]
layer_width_start = int(round(width/2))

layer2 = image2.crop((layer_width_start , 0, width, height))
savedImage.paste(layer2, (layer_width_start , 0, width, height))

savedImage.show()
save_as_tiff(savedImage)

