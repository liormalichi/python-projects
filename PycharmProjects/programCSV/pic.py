import numpy as np
import matplotlib.pyplot as plt

def change_image(im):
    """changing some of the pixcels for each photo in arrays of photo's
    links, just a little to maintain the same pic"""

    change_factor = [-5,-10,10,5]
    #skipping iteritions to run faster code
    for i in range(0, np.shape(im)[0], 13):
        factor = (1 + (change_factor[i%4] / 100))
        for j in range(0, np.shape(im)[1], 14):
            #making sure not to exceed 0 to 1 range
            if not ((im[i,j]*factor)[0] > 1 or (im[i,j]*factor)[1] > 1 or
            (im[i,j]*factor)[2] > 1 or (im[i,j]*factor)[0] < 0 or
            (im[i,j]*factor)[1] < 0 or (im[i,j]*factor)[2] < 0):
                value = im[i, j] * factor
                im[i,j] =value
    print(im[:,:,0])

    plt.imshow(im)
    plt.show()

    plt.imsave(r"C:\Users\malic\OneDrive\שולחן העבודה\תמונות לאתרים\png\Newsea.png", im)


input_file = r"C:\Users\malic\OneDrive\שולחן העבודה\תמונות לאתרים\png\sea.png"
plt.figure()
im = plt.imread(input_file)
#plt.imshow(im, cmap=plt.cm.gray)
#plt.show()

change_image(im)
newIm = np.array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])