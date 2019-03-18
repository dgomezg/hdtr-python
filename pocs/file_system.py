from pathlib import Path

#These will be part of the script configuration.
SOURCE_PATH = "samples/Toledo/sources"

pathlist = Path(SOURCE_PATH).glob('**/*.jpg')
for path in pathlist:
    print(str(path))

#Get the number of files in pahtlist
totalFiles = len([f for f in pathlist])

print('there are', totalFiles, 'images to process in', SOURCE_PATH)