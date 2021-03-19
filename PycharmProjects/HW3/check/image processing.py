import matplotlib.pyplot as plt
import numpy as np

im = plt.imread(r"C:\Users\malic\Downloads\puppy1.png")
print((im))
im2 = plt.imread(r"C:\Users\malic\OneDrive\תמונות\cercleSqure.png")
new_im = im
new_im[im < 0.3] = 0.3
im3 = np.copy(im2)
print(im2[1,2])
where =np.zeros(im2.shape)
for i in range(1, im2.shape[0]-1):
    for j in range(1, im2.shape[1]-1):
        nbors = np.array(np.array((im2[i,j+1][0] ==1 ),im2[i-1,j][0] ==1 ) ,(im2[i,j-1][0] ==1 ), (im2[i+1,j][0] ==1))):)
            for t in range(0, 20):
                im3[i+t,j+t][0] = 1
                im3[i+t,j+t][1] = 1
                im3[i+t,j+t][2] = 1


plt.figure()
plt.imshow(im3, cmap=plt.cm.gray)
plt.show()

""""
mat = np.array([[3,2,4],[5,4,1],[458,6,4]])

m = mat
m[mat > 10] = 3
print(m)
"""