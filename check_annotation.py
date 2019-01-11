#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 17:02
# @Author  : Gao Ke
# @Site    :
# @File    : check_annotation.py
# @Software: PyCharm Community Edition

from xml.etree import ElementTree as ET

def cover(srcfile, listfile, thresh = 20):
    """
    check and rewrite the xml file

    :param xmlfile: a format string leads to the big image detection result path
    :return:
    """
    with open(listfile, 'r') as f:
        lines = f.readlines()

    for line in lines:
        xml_file = srcfile.format(line.strip() + '.xml')

        tree = ET.parse(xml_file)
        objs = tree.findall('object')

        BB = {}
        Center = {}
        for ix, obj in enumerate(objs):
            box = obj.find('bndbox')
            xmin = float(box.find('xmin').text.strip())
            ymin = float(box.find('ymin').text.strip())
            xmax = float(box.find('xmax').text.strip())
            ymax = float(box.find('ymax').text.strip())

            b = [xmin,ymin,xmax,ymax]
            BB[ix] = b
            Center[ix] = ((xmax+xmin)/2.0,(ymax+ymin)/2.0)

        if len(Center)>0:
            for i in range(len(Center)-1):
                c1 = Center[i]
                for j in range(i+1, len(Center)):
                    c2 = Center[j]

                    d = abs(c1[0]-c2[0])+abs(c1[1]-c2[1])
                    if d < thresh:
                        print(line.strip())
                pass

def minibox(srcfile, listfile, thresh = 20):
    """
    check and rewrite the xml file

    :param xmlfile: a format string leads to the big image detection result path
    :return:
    """
    with open(listfile,'r') as f:
        lines = f.readlines()

    for line in lines:
        xml_file = srcfile.format(line.strip() + '.xml')

        tree = ET.parse(xml_file)
        objs = tree.findall('object')

        BB = {}
        Center = {}
        for ix, obj in enumerate(objs):
            box = obj.find('bndbox')
            xmin = float(box.find('xmin').text.strip())
            ymin = float(box.find('ymin').text.strip())
            xmax = float(box.find('xmax').text.strip())
            ymax = float(box.find('ymax').text.strip())

            width = xmax - xmin
            hight = ymax - ymin

            if width < thresh or hight < thresh:
                print(line.strip())


                pass

if __name__ == '__main__':
    print("check cover boxes")
    cover(srcfile=r'/media/jianchao/datas/data/new_icebox/11/{}',
            listfile='/media/jianchao/datas/data/new_icebox/11/list.txt',
            thresh=20
            )

    print("check mini boxes")
    minibox(srcfile=r'/media/jianchao/datas/data/new_icebox/11/{}',
          listfile='/media/jianchao/datas/data/new_icebox/11/list.txt',
          thresh=20
          )


