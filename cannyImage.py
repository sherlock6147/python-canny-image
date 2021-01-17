from cv2 import cv2 as cv
import numpy as np
from PIL import Image
import PIL

path = input("Enter Path relative to the current directory: ")
img=cv.imread(str(path))

cannied_img=cv.Canny(img,220,250)
output_path_name = input("Enter Output Path Name: ")
status = cv.imwrite(output_path_name, cannied_img)
 
print("Image written to file-system : ", status)

cv.waitKey(3)