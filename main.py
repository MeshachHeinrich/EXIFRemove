import sys
import PIL.Image
from PIL.ExifTags import TAGS

# Run the program
print("Running EXIFRemove...\n")

# Read input arguments
if (len(sys.argv) == 1):
     print("No file inputs provided")
     exit()
     
# Retrieve EXIF data from image
image = PIL.Image.open(sys.argv[1])
exif = image._getexif()

# Display EXIF data
if exif is None:
    print("File has no EXIF data")
    exit()
else:
    print("EXIF data: ------------------------------------------------------\n")
    
    for key, val in exif.items():
        if key in TAGS:
            print(f'{TAGS[key]} : {val}')
        else:
            print(f'{key} : {val}') 
    
    print("----------------------------------------------------------------\n")

