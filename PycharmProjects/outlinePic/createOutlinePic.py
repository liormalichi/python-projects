import numpy as np
import matplotlib.pyplot as plt

def change_image(im):


    #skipping iteritions to run faster code
    for i in range(1,np.shape(im)[0]-1):
        for j in range(1,np.shape(im)[1]-1):
            im[i, j] = is_outline(im, i, j)

    plt.imshow(im ,cmap="gray")
    plt.show()

    #plt.imsave(r"C:\Users\malic\OneDrive\שולחן העבודה\תמונות לאתרים\png\Newsea.png", im)

def is_outline(im, i, j):
    the_pixsle = im[i,j]
    c_0 = im[i-1, j-1]
    c_1 = im[i-1, j]
    c_2 = im[i-1, j+1]
    c_3 = im[i, j-1]
    c_5 = im[i, j+1]
    c_6 = im[i+1, j-1]
    c_7 = im[i+1, j]
    c_8 = im[i+1, j]
    c_9 = im[i+1, j+1]
    if (c_0 > 1.5*the_pixsle or c_1 > 1.5*the_pixsle or c_2 > 1.5*the_pixsle or
        c_3 > 1.5 * the_pixsle or c_5 > 1.5 * the_pixsle or c_6 > 1.5*the_pixsle or c_7 > 1.5*the_pixsle or
        c_8 > 1.5 * the_pixsle or c_9 > 1.5*the_pixsle or
        c_0 < (2/3) * the_pixsle or c_1 < (2/3) * the_pixsle or c_2 < (2/3) * the_pixsle or
        c_3 < (2 / 3) * the_pixsle or c_5 < (2/3) * the_pixsle or c_6 < (2/3) * the_pixsle or
        c_7 < (2 / 3) * the_pixsle or c_8 < (2/3) * the_pixsle or c_9 < (2/3) * the_pixsle):
        return 0
    return 1


input_file = r"C:\Users\malic\OneDrive\שולחן העבודה\me.png"
plt.figure()
im = plt.imread(input_file)
plt.imshow(im, cmap="gray")
plt.show()
change_image(im)
