import xml.etree.ElementTree as ET
import os
cwd = 'ice_box_0910/Annotations/'
# newcwd = 'newAnnotations/'
newcwd = 'ice_box_0910/newAnnotations/'
for path,d,filelist in os.walk(cwd):
    for xmlname in filelist:
        if xmlname.endswith('xml'):
            oldname = os.path.join(path,xmlname)
            # tree = ET.parse('/home/jianchao/Downloads/rBgODFuQ1s-ARPEFAVZHYGZrMS0490/Annotations/'+str(aaa)+'.xml')
            tree = ET.parse(oldname)
            root = tree.getroot()

            for xmin in root.iter('xmin'):
                xmin.text = str(int(xmin.text)-470)
                a=xmin.text
                print(a)
            for xmax in root.iter('xmax'):
                xmax.text = str(int(xmax.text)-470)
                b=xmax.text
                print(b)
        tree.write(newcwd + xmlname, encoding="utf-8", xml_declaration=True)


