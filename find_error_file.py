import xml.etree.ElementTree as ET
import os

"""
cwd : The root directory of oldXML
nwcwd: The root directory of rewrite XML
errorname : Error label name
newname : Correct label name 

"""

def find_errofile(filename):
    for path, d, filelist in os.walk(cwd):
        for xmlname in filelist:
            if xmlname.endswith('xml'):
                oldname = os.path.join(path, xmlname)
                tree = ET.parse(oldname)
                root = tree.getroot()
                for name in root.iter('name'):
                    if name.text == filename:
                        print(oldname)

def rewrite_xml(errorname, newname):
    for path, d, filelist in os.walk(cwd):
        for xmlname in filelist:
            if xmlname.endswith('xml'):
                oldname = os.path.join(path, xmlname)
                tree = ET.parse(oldname)
                root = tree.getroot()
                for name in root.iter('name'):
                    if name.text == errorname:
                        print(oldname)
                        name.text = newname
                tree.write(newcwd + xmlname, encoding="utf-8", xml_declaration=True)




if __name__ == '__main__':
    cwd = '/media/jianchao/datas/data/drink/drink_1/wt/fch/'
    newcwd = '/media/jianchao/datas/data/drink/nocalib_onlycap5/Annotations1/'
    errorname = 'STARBUCKS'
    newname = 'starbucks'
    # find_errofile(errorname)
    rewrite_xml(errorname, newname)













# cwd = '/media/jianchao/datas/data/jian/static/Annotations/'
    # errorname = 'w'
    # find_errofile(errorname)










