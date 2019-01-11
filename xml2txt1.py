# -*- coding: utf-8 -*-
"""
Created on 12.11 2018

@author: linkdZS
"""
import xml.dom.minidom as xmldom
import os


def xml2txt(p, filename):
    domobj = xmldom.parse(p)
    elementobj = domobj.documentElement

    name = elementobj.getElementsByTagName("text")
    x = elementobj.getElementsByTagName("x")
    y = elementobj.getElementsByTagName("y")

    f = open(txt_path + filename, 'a')
    for i in range(len(name)):
        f.write(name[i].childNodes[0].data + ';')
        f.write(x[4*(i+1)-4].childNodes[0].data + ';')
        f.write(y[4*(i+1)-4].childNodes[0].data + ';')
        f.write(x[4*(i+1)-3].childNodes[0].data + ';')
        f.write(y[4*(i+1)-2].childNodes[0].data + '\n')
    f.close()




if __name__ == '__main__':

    xml_path = '/media/jianchao/datas/data/text_label/test/test/'
    txt_path = '/media/jianchao/datas/data/text_label/test/result/'

    list = os.listdir(xml_path)
    # list = list[:660]

    for p in list:
        filename = p[:-3] + 'txt'
        xml2txt(xml_path + p, filename)
