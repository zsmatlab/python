# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:20:24 2018

@author: linkd
"""
import xml.dom.minidom as xmldom
import os


def xml2txt(p,filename):    
    domobj = xmldom.parse(p)
    print("xmldom.parse:", type(domobj))
    # 得到元素对象
    elementobj = domobj.documentElement
    print ("domobj.documentElement:", type(elementobj))
    
    #获得子标签
    name = elementobj.getElementsByTagName("name")
    xmin = elementobj.getElementsByTagName("xmin")
    xmax = elementobj.getElementsByTagName("xmax")
    ymin = elementobj.getElementsByTagName("ymin")
    ymax = elementobj.getElementsByTagName("ymax")
    
    #os.mkdir('test.txt')
    f = open(opend + filename, 'a')
    for i in range(len(name)):
        f.write(name[i].childNodes[0].data+' ')
        f.write(xmin[i].childNodes[0].data+' ')
        f.write(xmax[i].childNodes[0].data+' ')
        f.write(ymin[i].childNodes[0].data+' ')
        f.write(ymax[i].childNodes[0].data+'\n')
    f.close()
    
    
opend = '/media/jianchao/datas/data/text_label/test/test/'

list = os.listdir(opend)
list = list[:10]

for p in list:
    filename = p[:-3]+'txt'
    xml2txt(opend + p, filename)