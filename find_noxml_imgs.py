#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find the image's name if the image hasn't xml
# @File    : find_xml_imgs.py
import os
import cv2


def find_file(newpath , xmlpath, imgpath, listfile ):
    with open(listfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            jpg = imgpath.format(line.strip()) + '.jpg'
            xml_jpg = xmlpath.format(line.strip()) + '.xml'
            a = os.path.exists(xml_jpg)
            if a == False:
                print(jpg)
                img = cv2.imread(jpg)
                cv2.imwrite(newpath + line.strip() + '.jpg', img)




if __name__ == '__main__':
    newpath = r'/media/jianchao/datas/data/new_icebox/12/drinkj/11/'
    listfile = '/media/jianchao/datas/data/drinkj/jian24xml/list.txt'
    imgpath = '/media/jianchao/datas/lianshu79/lianshu79/{}'
    xmlpath = '/media/jianchao/datas/data/drinkj/jian24xml/{}'
    find_file(newpath, xmlpath, imgpath, listfile)