#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find the image's name if the image has xml
# @File    : find_xml_imgs.py
import os
import cv2


def find_file(newpath , xmlpath, imgpath, listfile ):
    n=0
    with open(listfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # xml_file =
            jpg = imgpath.format(line.strip()) + '.jpg'
            xml_jpg = xmlpath.format(line.strip()) + '.xml'
            a = os.path.exists(xml_jpg)
            if a == True:
                print(jpg,n)
                img = cv2.imread(jpg)
                n+=1
                cv2.imwrite(newpath + line.strip() + '.jpg', img)




if __name__ == '__main__':
    newpath = r'E:/data/new_icebox/12/drinkj/JPEGImages/'
    listfile = 'E:/data/new_icebox/12/drinkj/Annotations/list.txt'
    imgpath = 'E:/lianshu79/lianshu79/{}'
    xmlpath = 'E:/data/new_icebox/12/drinkj/Annotations/{}'
    find_file(newpath, xmlpath, imgpath, listfile)