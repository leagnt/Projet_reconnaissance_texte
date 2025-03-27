import numpy as np
import pandas as pd
import cv2
class normaliser:
    def __init__(self, image_lettre, dim=(28, 28)):
        image_normal = image_lettre.np.reshape(dim)

        return image_normal