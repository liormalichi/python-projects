import numpy
import matp

גef squeeze_image(im,factor):
    new_n = im.shape[0]
    new_m = im.shape[1] / factor
    new_mat = np.zeros((new_n,new_m))
    for j in range(new_mat.shape[1]):
        curr_range = range(j*factor,min((j+1)*factor,im.shape[1]))
        new_mat[:,j] = im[:,curr_range].mean(axis=1)
    return new_mat