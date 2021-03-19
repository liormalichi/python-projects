import numpy as np
import random
import matplotlib.pyplot as plt


newIm = np.array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])

plt.imshow(newIm, cmap=plt.cm.gray)
plt.show()
newIm = np.array([[ [0,  1,  2]],
       [[ 155,  126.2,  207]],
       [[12, 12, 12]],
       [[12, 18, 19]]])

plt.imshow(newIm, cmap=plt.cm.gray)
plt.show()