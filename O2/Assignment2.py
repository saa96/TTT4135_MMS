import numpy as np
import glob
from PIL import Image
#import cv2
import matplotlib.pyplot as plt
## Task 4: Prediction

img_path = glob.glob('Program_Files/*.png')
img_data = []
for path in img_path:
    img_data.append(np.array(Image.open(path)))

print(img_data[0])
plt.figure()
plt.imshow(img_data[0])
#cv2.imshow(("Window", img_data[0]))