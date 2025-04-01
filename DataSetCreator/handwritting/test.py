from __future__ import print_function

import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt




# set display defaults
plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


path = 'curated.tar.gz.01/'
[2]
#Read characters only a-z and A-Z characters
#PENDING: special characters and digits

from os import listdir
from os.path import isfile, join

character_curated = [ord(c) for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
print([chr(i) for i in character_curated])

X = []
y = []
for i in character_curated:
    path_img = path + str(i) + '/'
    for file_name in [f for f in listdir(path_img) if isfile(join(path_img, f))]:
        img = cv2.imread(path_img + file_name, 0)
        #img = cv2.resize(img,(32, 32), interpolation = cv2.INTER_AREA)
        X += [img]
        y += [i]

X = np.array(X, dtype=np.uint8)
y = np.array(y, dtype=np.uint8)
print(X.shape)
print(y.shape)