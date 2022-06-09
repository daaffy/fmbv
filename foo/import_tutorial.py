# https://nipy.org/nibabel/nifti_images.html
# https://carpentries-incubator.github.io/SDC-BIDS-IntroMRI/anatomy-of-nifti/index.html
# Working with some example NIfTI images.

# exec(open("./foo/test.py").read())

import numpy as np
# Print to 2 d.p. precision
np.set_printoptions(precision=2, suppress=True)

import os
import nibabel as nib
from nibabel.testing import data_path

# --- NIfTI 1 image
example_ni1 = os.path.join(data_path, 'example4d.nii.gz')
n1_img = nib.load(example_ni1)

# Header information
n1_header = n1_img.header
# print(n1_header)

# # Get and set individual fields
# print(n1_header['cal_max'])
# n1_header['cal_max'] = 1200
# print(n1_header['cal_max'])
# # what about get_/set_ methods? apparently they are safer as they apply checks


# ...

# Getting data
n1_data = n1_img.get_fdata()
print(n1_data.shape)

# print(n1_data[:,:,20,0])
slice = n1_data[60,:,:,0]

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 1)
axes.imshow(slice.T, cmap="gray", origin="lower")
plt.show()