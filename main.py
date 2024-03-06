import sys
import os
import PIL.Image
from PIL.ExifTags import TAGS

# Define colour printing functions
def printGreen(text): print("\033[92m{}\033[00m".format(text), end='')
def printYellow(text): print("\033[93m{}\033[00m".format(text), end='')
def printBlue(text): print("\033[96m{}\033[00m".format(text), end='')

# Run the program
printYellow("""\
    
    _______  __ ______________                               
   / ____/ |/ //  _/ ____/ __ \___  ____ ___  ____ _   _____ 
  / __/  |   / / // /_  / /_/ / _ \/ __ `__ \/ __ \ | / / _ \\
 / /___ /   |_/ // __/ / _, _/  __/ / / / / / /_/ / |/ /  __/
/_____//_/|_/___/_/   /_/ |_|\___/_/ /_/ /_/\____/|___/\___/ 
\n""")

printBlue("By Meshach Heinrich\n\n")

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
    print("---------------------------------------\n")
    
    for key, val in exif.items():
        if key in TAGS:
            printYellow(f'{TAGS[key]}')
            print(f': {val}')
        else:
            printYellow(f'{key} : {val}') 
    
    print("\n---------------------------------------\n")

# Remove EXIF data and output as file
output = PIL.Image.new(image.mode, image.size)
output.putdata(list(image.getdata()))
fileName = os.path.basename(sys.argv[1]).split(".")
outputName = fileName[0] + "_Stripped." + fileName[1]
output.save(outputName)
output.close()

printGreen("EXIF data removed, output file = " + outputName + "\n\n\n")