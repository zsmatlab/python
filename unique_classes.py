# encoding: utf-8
'''
@author: Gao Ke
@license: (C) Copyright 2018-present, SeetaTech, Co.,Ltd.
@contact: ke.gao@seetatech.com
@file: unique_classes.py
@time: 18-10-15 下午1:38
@desc:
'''


from xml.etree import ElementTree as ET

def unique_classes(srcfile, listfile):
    """
        check the classes in the xml file

        :param srcfile: a format string leads to the image path
        :param listfile: a format string leads to the image list path
    """
    cls_list = []
    with open(listfile, 'r') as f:
        lines = f.readlines()

    for line in lines:
        xml_file = srcfile.format(line.strip())

        tree = ET.parse(xml_file)
        objs = tree.findall('object')

        for ix, obj in enumerate(objs):
            cls = obj.find('name').text
            if cls in cls_list:
                pass
            else:
                cls_list.append(cls)
                print(cls)

def count_class(srcfile, listfile):
    """
        check the classes and the number of the classes in the xml file

        :param srcfile: a format string leads to the image path
        :param listfile: a format string leads to the image list path
        :return:
    """
    cls_list = []

    # open the list file
    with open(listfile, 'r') as f:
        lines = f.readlines()

    # check each file in the list
    for line in lines:
        xml_file = srcfile.format(line.strip())

        tree = ET.parse(xml_file)

        # objs is all the objects in the xml
        objs = tree.findall('object')

        # find the class name in the object, and add it to the cls list
        for ix, obj in enumerate(objs):
            cls = str(obj.find('name').text)
            cls_list.append(cls)

    # find the keys and sort, count the number of boxes of the keys
    if len(cls_list) > 0:
        cls_list.sort()
        import numpy as np
        cls_arr = np.array(cls_list)
        cls1 = list(set(cls_list))
        print('unsort classes is:', cls1)
        cls1.sort()
        print('sorted classes is:', cls1)
        classes = np.unique(cls_arr)
        print('the class number is:', classes.shape[0])
        print('----------------------------')
        print('the number of each class:')
        for i in range(0, classes.shape[0]):
            # print(classes[i], cls_list.count(classes[i]))
            print(classes[i], ':', np.where(cls_arr==classes[i])[0].shape[0])
        print('----------------------------')

    print('the number of all the boxes is:', len(cls_list))
    return cls_list

if __name__ == '__main__':
    srcfile = r'/media/jianchao/datas/data/jian/static/Annotations/{}.xml'
    listfile = '/media/jianchao/datas/data/jian/static/ImageSets/Main/train.txt'

    # just print all the classes
    #unique_classes(srcfile, listfile)

    # print the sorted classes list, print the number of each class
    cls_list = count_class(srcfile, listfile)