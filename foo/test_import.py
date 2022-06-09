import numpy as np
import os
import nibabel as nib

nii_img = nib.load('./Data/stitched_placenta_image_data/stitched_volumetric_image_dp.nii')

nii_data = nii_img.get_fdata()

print(nii_data.shape)

slice = nii_data[:,300,:]

# Plot
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 1)
axes.imshow(slice.T, cmap="gray", origin="lower")
plt.show()
