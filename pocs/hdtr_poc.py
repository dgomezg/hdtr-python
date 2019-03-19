from pathlib import Path
from PIL import Image
from datetime import datetime


#These will be part of the script configuration.
SOURCE_PATH = "samples/Toledo/sources"
OUTPUT_PATH = "samples/Toledo/output"

def save_as_tiff(image):
    output_file_name = OUTPUT_PATH + "/" + datetime.today().strftime('%Y%m%d-%H%M%S%f') + ".tiff"
    outputImage = image.save(output_file_name)
    return Image.open(output_file_name)

def extract_dimensions(image):
    return image.size

def extract_image_size(filepath):
    return Image.open(str(filepath)).size

#Create Image

files = [f for f in Path(SOURCE_PATH).glob("*.jpg")]
files.sort()

size = extract_image_size(files[0])
print("Creating an image of size", size)

final_image = Image.new('RGB', size) 
column_width = int(round(size[0] / len(files)))
height = size[1]

column = 0
for file in files:
    print("Processing", file)
    current_image = Image.open(file)
    x0=column_width*column
    x1=column_width*(column +1)
    print("Pasting column ", column, " from (", x0, ", 0,", x1, ",", height)    
    layer = current_image.crop((x0 , 0, x1, height))
    final_image.paste(layer, (x0 , 0, x1, height))
    column += 1

#final_image.show()
save_as_tiff(final_image)


