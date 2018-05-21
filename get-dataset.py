import os
import numpy as np
from PIL import Image

cur_path = os.getcwd()
data_filepath = os.path.join(cur_path, os.path.dirname("dataset/"), "semeion.data")
print("data_filepath: " + data_filepath)

# Container for the images
img = np.empty([32,32])

if os.path.exists(data_filepath):
    with open(data_filepath) as f:
        for line in f:      
            # Read the line, then strip the new line and space at the end
            line = f.readline().strip(" \n").split(" ")
            # Put the relevent part into the img
            img = np.array(line[:-10]).reshape((16,16))
            # Get the category
            category = line[-10:]
            
            img_obj = Image.fromarray(img, mode="L")
            img_obj.show()

else:
    print("ERROR: unable to find semeion.data at path " + data_filepath)
    print("Please ensure it exists before continuing.")
    raise FileNotFoundError("semion.data not found")
