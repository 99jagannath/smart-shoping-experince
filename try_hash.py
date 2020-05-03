# example_averagehash.py

# Import dependencies
from PIL import Image
import imagehash

# Create the Hash Object of the first image
#HDBatmanHash = imagehash.average_hash(Image.open('dettol.jpg'))
HDBatmanHash = imagehash.phash(Image.open('savlon2.jpg'))
print('Batman HD Picture: ' + str(HDBatmanHash))

# Create the Hash Object of the second image
#SDBatmanHash = imagehash.average_hash(Image.open('savlon1.jpg'))
SDBatmanHash = imagehash.phash(Image.open('savlon1.jpg'))
print('Batman HD Picture: ' + str(SDBatmanHash))

# Compare hashes to determine whether the pictures are the same or not
if(HDBatmanHash == SDBatmanHash):
    print("The pictures are perceptually the same !")
else:
    print("The pictures are different, distance: " + str(HDBatmanHash - SDBatmanHash))