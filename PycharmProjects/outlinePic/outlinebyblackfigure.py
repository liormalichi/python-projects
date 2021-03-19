import numpy as np
import matplotlib.pyplot as plt

def change_image(im):
    print(im)
    count = 0
    for i in range(1,np.shape(im)[0]-1):
        for j in range(1,np.shape(im)[1]-1):
            if im[i, j][0] > 0.6:
                im[i, j][0] = 1
                im[i, j][1] = 1
                im[i, j][2] = 1
                #count = CHEAKNEAR(im,i,j ,count)

            else:
                im[i, j][0] = 0
                im[i, j][1] = 0
                im[i, j][2] = 0
    print(3)
    plt.imshow(im ,cmap="gray")
    plt.show()
    plt.imsave(r"C:\Users\malic\OneDrive\שולחן העבודה\spray painting\שבלונות\fatherson1.png", im)

    #plt.imsave(r"C:\Users\malic\OneDrive\שולחן העבודה\תמונות לאתרים\png\Newsea.png", im)



def CHEAKNEAR(im, i, j, count):
    print(count)
    flag = False
    if im[i, j-1][0] > 0.3:
        im[i, j-1][0] = 1
        flag = True

    if im[i+1, j+1][0] > 0.3:
        flag = True
        im[i+1, j+1][0] = 1
    if im[i, j+1][0] > 0.3:
        flag = True
        im[i, j+1][0] = 1
    if im[i+1, j-1][0] > 0.3:
        flag = True
        im[i+1, j-1][0] = 1
    if im[i+1, j][0] > 0.3:
        flag = True
        im[i+1, j][0] = 1
    if im[i-1, j-1][0] > 0.3:
        flag = True
        im[i-1, j-1][0] = 1
    if im[i-1, j][0] > 0.3:
        flag = True
        im[i-1, j][0] = 1
    if im[i-1, j+1][0] > 0.3:
        flag = True
        im[i-1, j+1][0] = 1
    count = count +1
    return count

input_file = r"C:\Users\malic\OneDrive\שולחן העבודה\spray painting\שבלונות\fatherson.png"
plt.figure()
im = plt.imread(input_file)
#plt.imshow(im, cmap="gray")
#plt.show()
change_image(im)
