import matplotlib.pyplot as plt
import numpy as np
import scipy.misc
import os
from skimage.transform import resize
from PIL import Image
 
file_dir = r"/mnt/data/panxue/PX/H-vmunet-main/data_train.npy"  # npy file address.
dest_dir = r"/mnt/data/panxue/PX/H-vmunet-main/npy/train" # Generate png images save address.
 
def npy_png(file_dir, dest_dir):
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
 
    #file = file_dir #+ 'name.npy'  
    con_arr = np.load(file_dir)  
    for i in range(0, 9999):  
        arr = con_arr[i, :, :]  
        disp_to_img = resize(arr, [256, 256])  
        a = format(i, '04d')
        disp_to_img = disp_to_img.astype('uint8')
        plt.imsave(os.path.join(dest_dir, a+".png"), disp_to_img, cmap='gray')  # Select 'gray' for masks. 'plasma' for images.
        print('photo a finished')
 
 
if __name__ == "__main__":
    npy_png(file_dir, dest_dir)
