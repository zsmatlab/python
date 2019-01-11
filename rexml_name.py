import xml.etree.ElementTree as ET
import os
cwd = 'E:/data/test/'
# newcwd = '/media/jianchao/datas/data/new_icebox/12/jian24/'
for path,d,filelist in os.walk(cwd):
    for xmlname in filelist:
        if xmlname.endswith('xml'):
            oldname = os.path.join(path, xmlname)
            tree = ET.parse(oldname)
            root = tree.getroot()

            for name in root.iter('name'):
                if name.text == "\\":
                   print(oldname)
                   # name.text = "heweidao_haixian"
                   # a = name.text
            # tree.write(newcwd + xmlname, encoding="utf-8", xml_declaration=True)


