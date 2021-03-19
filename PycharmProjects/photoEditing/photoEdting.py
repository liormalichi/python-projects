import matplotlib.pyplot as plt
import matplotlib.image as mp
import numpy as np

image_path = r"C:/Users/malic/PycharmProjects/photoEditing/lena_nse.jpg"
im = mp.imread(image_path)
plt.imshow(im, camp = plt.cm.gray)