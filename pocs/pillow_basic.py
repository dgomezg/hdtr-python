from __future__ import print_function
from datetime import datetime
from PIL import Image
import numpy as np

#These will be part of the script configuration.
SOURCE_PATH = "samples/Toledo/sources"
SAMPLE_IMAGE_PATH = SOURCE_PATH + "/0001-enf.jpg"
SAMPLE2_IMAGE_PATH = SOURCE_PATH + "/0384-enf.jpg"
OUTPUT_PATH = "samples/Toledo/output"

def save_as_tiff(image):
    output_file_name = OUTPUT_PATH + "/" + datetime.today().strftime('%Y%m%d-%H%M%S%f') + ".tiff"
    outputImage = image.save(output_file_name)
    return Image.open(output_file_name)

def generate_mask(size):
    mask_value = []
    for i in range(size[1]):
        mask_value.append([])
    for j in range(size[0]):
        value = 255-(255*j/size[0])
        for i in range(size[1]):
            mask_value[i].append(value)
    return Image.fromarray(np.array(mask_value))

base_image = Image.open(SAMPLE_IMAGE_PATH)
print(base_image.format, base_image.size, base_image.size[0], base_image.size[1], base_image.mode)
savedImage = save_as_tiff(base_image)

image2 = Image.open(SAMPLE2_IMAGE_PATH)
print(image2.format, image2.size[0], image2.size[1], image2.mode)


width = base_image.size[0]
height = base_image.size[1]
layer_width_start = int(round(width/2))

layer2 = image2.crop((0 , 0, width, height))
print("layer size", layer2.size)

mask_array = np.random.rand(layer2.size[1], layer2.size[0]) > 0.7
print(mask_array)
mask = Image.fromarray(np.uint8(255*(mask_array)))

#mask = Image.fromarray(np.uint8(255*(np.random.rand(layer2.size[1], layer2.size[0]) > 0.7))) 
#print("Mask size", mask.size)
#mask = generate_mask(layer2.size)
print("mask size", mask.size)
mask.show()

print("image2 size", image2.size)
savedImage.paste(image2, (0, 0, width, height), mask)

savedImage.show()
#save_as_tiff(savedImage)

