from pathlib import Path
from PIL import Image
from datetime import datetime
import numpy as np


#These will be part of the script configuration.
SAMPLE_SET = "Alhambra-Granada"
#SAMPLE_SET = "Toledo"
SOURCE_PATH = "samples/" + SAMPLE_SET + "/sources"
OUTPUT_PATH = "samples/" + SAMPLE_SET + "/output"
gradient_in_columns = 15

def save_as_tiff(image):
    output_file_name = OUTPUT_PATH + "/" + datetime.today().strftime('%Y%m%d-%H%M%S%f') + ".tiff"
    outputImage = image.save(output_file_name)
    return Image.open(output_file_name)

def extract_dimensions(image):
    return image.size

def extract_image_size(filepath):
    return Image.open(str(filepath)).size

def generate_mask(size, start, finish):
    mask_value = []
    width = size[0]
    height = size [1]
    gradient_length = finish - start
    for i in range(height):
        mask_value.append([])
    for j in range(width):
        if (j < start):
            value = 255
        elif start <= j  < finish:
            value = 255-(255*(j-start)/gradient_length)
        else:
            value = 0
        for i in range(height):
            mask_value[i].append(value)
    return Image.fromarray(np.uint8(np.array(mask_value)), "L")


#Create Image
files = [f for f in Path(SOURCE_PATH).glob("*.jpg")]
files.sort()

size = extract_image_size(files[0])
print("Creating an image of size", size)

final_image = Image.new('RGB', size) 
column_width = int(round(size[0] / len(files)))
height = size[1]

column = 0
gradient_in_pixels = (gradient_in_columns/2) * column_width
for file in files:
    current_image = Image.open(file)
    x0=(column_width*column) - (gradient_in_pixels)
    x1=(column_width*column) + (gradient_in_pixels)
    print("Adding image ", column, " from ", file, " with gradient mask: (", x0, ", 0,", x1, ",", height, ")")    
    layer_mask = generate_mask(current_image.size, x0, x1)
    final_image = Image.composite(final_image, current_image, layer_mask)
    column += 1

final_image.show()
save_as_tiff(final_image)


