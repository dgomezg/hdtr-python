from pathlib import Path

#These will be part of the script configuration.
SOURCE_PATH = "samples/Toledo/sources"

pathlist = Path(SOURCE_PATH).glob('**/*.jpg')
files = 0
for path in pathlist:
    print(str(path))
    files += 1

print('there are', files, 'images to process in', SOURCE_PATH)