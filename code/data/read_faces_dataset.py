import numpy as np
#import matplotlib.pyplot as plt
from skimage.transform import PiecewiseAffineTransform, warp
from skimage import data
from scipy import misc

#image = misc.imread('/home/pnallam/Desktop/Ram-Charan-Teja.jpg')

def convert_image(imageLoc, imageOutLoc, var):
    image = misc.imread(imageLoc)
    rows, cols = image.shape[0], image.shape[1]
    src_cols = np.linspace(0, cols, 20)
    src_rows = np.linspace(0, rows, 10)
    src_rows, src_cols = np.meshgrid(src_rows, src_cols)
    src = np.dstack([src_cols.flat, src_rows.flat])[0]

    # add sinusoidal oscillation to row coordinates
    #dst_rows = src[:, 1] - np.sin(np.linspace(0, 3 * np.pi, src.shape[0])) * 50
    #dst_cols = src[:, 0]
    #dst_rows *= 1.5
    #dst_rows -= 1.5 * 50
    #dst = np.vstack([dst_cols, dst_rows]).T

    mu, sigma = 0, var # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000) #src.shape[0]

    # add Gausian oscillation to row coordinates
    dst_rows = src[:, 1] - np.random.normal(mu, sigma, src.shape[0]) * 50
    dst_cols = src[:, 0]
    dst_rows *= 1.5
    dst_rows -= 1.5 * 50
    dst = np.vstack([dst_cols, dst_rows]).T


    tform = PiecewiseAffineTransform()
    tform.estimate(src, dst)


    tform = PiecewiseAffineTransform()
    tform.estimate(src, dst)

    out_rows = image.shape[0] - 1.5 * 50
    out_cols = cols
    out = warp(image, tform, output_shape=(out_rows, out_cols))   
    misc.imsave(imageOutLoc, out)

    #fig, ax = plt.subplots()
    #ax.imshow(out)
    #ax.plot(tform.inverse(src)[:, 0], tform.inverse(src)[:, 1], '.b')
    #ax.axis((0, out_cols, out_rows, 0))
    #plt.show()
    
def add_white_noise(imageLoc, imageOutLoc, var):
    image = misc.imread(imageLoc)
    out = image + var * image.std() * np.random.random(image.shape)
    misc.imsave(imageOutLoc, out)

    #fig, ax = plt.subplots()
    #ax.imshow(out)
    #ax.plot(tform.inverse(src)[:, 0], tform.inverse(src)[:, 1], '.b')
    #ax.axis((0, out_cols, out_rows, 0))
    #plt.show()    
