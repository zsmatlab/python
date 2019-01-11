import xml.etree.ElementTree as ET
import os
cwd = '/media/jianchao/datas/data/jian/static/Annotations/'
# newcwd = 'newAnnotations/'
newcwd = '/media/jianchao/datas/python_script/test/2/'
a = 0
for path,d,filelist in os.walk(cwd):
    for xmlname in filelist:
        if xmlname.endswith('xml'):
            oldname = os.path.join(path, xmlname)
            # tree = ET.parse('/home/jianchao/Downloads/rBgODFuQ1s-ARPEFAVZHYGZrMS0490/Annotations/'+str(aaa)+'.xml')
            tree = ET.parse(oldname)
            root = tree.getroot()

            for name in root.iter('name'):
                if name.text == 'xiangchneg':
                    print(oldname)
                   # a+=1

            # for xmax in root.iter('xmax'):
            #     xmax.text = str(int(xmax.text)-470)
            #     b=xmax.text
            #     print(b)
            # tree.write(newcwd + xmlname, encoding="utf-8", xml_declaration=True)


