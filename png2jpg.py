import os
import cv2
import sys
import numpy as np
path = "/media/jianchao/datas/data/linkdata/phoneBbox_data/JPEGImages/"
newpath = "/media/jianchao/datas/data/linkdata/phoneBbox_data/JPEGImages1/"
print(path)

for filename in os.listdir(path):
    if os.path.splitext(filename)[1] == '.png':
        # print(filename)
        img = cv2.imread(path + filename)
        print(filename.replace(".png", ".jpg"))
        newfilename = filename.replace(".png", ".jpg")
        # cv2.imshow("Image",img) #
        # cv2.waitKey(0)
        cv2.imwrite(newpath + newfilename, img)

