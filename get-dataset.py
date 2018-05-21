import os
import numpy as np

cur_path = os.getcwd()
data_filepath = os.path.join(cur_path, os.path.dirname("dataset/"), "semeion.data")
print("data_filepath: " + data_filepath)

# Container for the images
img = np.empty([32,32])

if os.path.exists(data_filepath):
    with open(data_filepath) as f:
        line = f.readline()
        print(line)
else:
    print("ERROR: unable to find semeion.data at path " + data_filepath)
    print("Please ensure it exists before continuing.")
    raise FileNotFoundError("semion.data not found")
