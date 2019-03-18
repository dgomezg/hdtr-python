from pathlib import Path

#These will be part of the script configuration.
SOURCE_PATH = "samples/Toledo/sources"

#Path().glob returns an unsorted list
pathlist = list([f for f in Path(SOURCE_PATH).glob('**/*.jpg')])
pathlist.sort()
for path in pathlist:
    print(str(path))

#Get the number of files in pahtlist
totalFiles = len(pathlist)

print('there are', totalFiles, 'images to process in', SOURCE_PATH)