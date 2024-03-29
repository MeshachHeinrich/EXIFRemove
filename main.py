import sys
import os
import imghdr
import PIL.Image
from PIL.ExifTags import TAGS

# Define colour printing functions
def printGreen(text): print("\033[92m{}\033[00m".format(text), end='')
def printYellow(text): print("\033[93m{}\033[00m".format(text), end='')
def printBlue(text): print("\033[96m{}\033[00m".format(text), end='')

# -------------------------------------------------------------------

# Ensure all arguments were provided
if (len(sys.argv) == 1):
     print("Usage: python3 main.py PATH_TO_IMAGE")
     exit()

# Ensure provided file actually exists
if not (os.path.exists(sys.argv[1])):
    print("File does not exist")
    exit()

# Finally, check file is a valid image format
if not (imghdr.what(sys.argv[1])):
    print("File is not an image format")
    exit()

# Run the program
printYellow("""\
    
    _______  __ ______________                               
   / ____/ |/ //  _/ ____/ __ \___  ____ ___  ____ _   _____ 
  / __/  |   / / // /_  / /_/ / _ \/ __ `__ \/ __ \ | / / _ \\
 / /___ /   |_/ // __/ / _, _/  __/ / / / / / /_/ / |/ /  __/
/_____//_/|_/___/_/   /_/ |_|\___/_/ /_/ /_/\____/|___/\___/ 
\n""")

printBlue("By Meshach Heinrich\n\n")
     
# Retrieve EXIF data from image
image = PIL.Image.open(sys.argv[1])
exif = image._getexif()

gpsCoords = [0,0]

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
            
        # Store GPS coordinates
        if f'{TAGS[key]}' == 'GPSInfo':
                  
            # Convert to decimal from its original degrees/minutes/seconds format via division by 60
            gpsCoords = [f'{int(val[2][0]) + int(val[2][1])/60 + int(val[2][2])/3600},', f'{int(val[4][0]) + int(val[4][1])/60 + int(val[4][2])/3600}']
            
            # Flip latitude if it's oriented South
            if f'{val[1][0]}' == 'S':
                gpsCoords[0] = '-' + gpsCoords[0]
            # Flip longitude if it's oriented West
            if f'{val[3][0]}' == 'W':
                gpsCoords[1] = '-' + gpsCoords[1]
            
    
    
# Display Google Maps link to the photo's origin location
printYellow("\nLocation of origin: https://www.google.com/maps/search/" + gpsCoords[0] + gpsCoords[1] + "\n")
print("\n---------------------------------------\n")

# Remove EXIF data and output as file
output = PIL.Image.new(image.mode, image.size)
output.putdata(list(image.getdata()))
fileName = os.path.basename(sys.argv[1]).split(".")
outputName = fileName[0] + "_Stripped." + fileName[1]
output.save(outputName)
output.close()

printGreen("EXIF data removed, output file = " + outputName + "\n\n\n")