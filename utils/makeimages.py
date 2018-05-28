import os
import numpy as np
import matplotlib.pyplot as plt


def makeimages():
    cur_path = os.getcwd()
    data_filepath = os.path.join(cur_path, os.path.dirname("dataset/"), "semeion.data")
    print("data_filepath: " + data_filepath)
    im_path = os.path.join(cur_path, os.path.dirname('dataset/'), os.path.dirname("ims/"))

    # Container for the images
    img = np.empty([32,32])

    if os.path.exists(data_filepath):
        if not os.path.exists(im_path):
            os.makedirs(im_path)

        with open(data_filepath) as f:
            for i, line in enumerate(f):
                print(f"line: {i}")
                # strip the new line and space at the end of the read line
                l = line.strip(" \n").split(" ")
                # Put the relevent part into the img
                img = np.array(l[:-10], dtype=np.float).reshape((16,16))
                # Get the category
                category = l[-10:]

                # since we know that there is only one '1' in the array,
                # the index of the '1' in the array is our written digit
                prefix = category.index('1')
                plt.imsave(os.path.join(im_path, f"{prefix}_{i}.png"), img, cmap='binary')

    else:
        print("ERROR: unable to find semeion.data at path " + data_filepath)
        print("Please ensure it exists before continuing.")
        raise FileNotFoundError("semion.data not found")

if __name__ == "__main__":
    makeimages()