import os
import numpy as np

def getdataset():
    # Get the path do the data file
    cur_path = os.getcwd()
    data_filepath = os.path.join(cur_path, os.path.dirname("dataset/"), "semeion.data")
    print("data_filepath: " + data_filepath)

    x = np.empty((1593, 16*16), dtype=np.float)
    y = np.empty((1593, 10), dtype=np.int)

    if os.path.exists(data_filepath):
        with open(data_filepath) as f:
            for i, line in enumerate(f):    
                # strip the space and new line, then split each value
                l = line.strip(" \n").split(" ")
                # Put the relevent part into the x data
                x[i] = np.array(l[:-10], dtype=np.float)
                # Get the category
                y[i] = l[-10:]

    return x,y

if __name__ == "__main__":
    getdataset()