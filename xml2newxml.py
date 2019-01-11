import xml.etree.ElementTree as ET
import os
cwd = 'E:/data/text_label/test_label/1/'
# newcwd = 'newAnnotations/'
newcwd = 'E:/data/text_label/test_label/2/'
m=open('E:/data/text_label/test_label/3/list.txt', 'r+')
e=[]
f=[]
for path,d,filelist in os.walk(cwd):
    for xmlname in filelist:
        if xmlname.endswith('xml'):
            oldname = os.path.join(path, xmlname)
            # tree = ET.parse('/home/jianchao/Downloads/rBgODFuQ1s-ARPEFAVZHYGZrMS0490/Annotations/'+str(aaa)+'.xml')
            tree = ET.parse(oldname)
            root = tree.getroot()

            for filename in root.iter('filename'):
                a=filename.text
                print(a)
            for width in root.iter('width'):
                b=width.text
                print(b)
            for height in root.iter('height'):
                c=height.text
                print(c)
            for ob in root.iter('object'):
                for name in ob.iter('text'):
                    d.append(name.text)

                for x in ob.iter('x'):
                    e.append(x.text)

                for y in ob.iter('y'):
                    f.append(y.text)
                    print(f)



    print(d[0],min(e[0:4]),max(f[0:4]),max(e[0:4]),min(f[0:4]))
    print(d[1],min(e[5:8]),max(f[5:8]),max(e[5:8]),min(f[5:8]))
    n = len(d)
    print(n)
# xmin=[]
for i in range(len(d)):
    # xmin[0] = min(e[i:i+4])
    #     # print(xmin[0])
    m.write(d[i]+' '+ min(e[(4*(i+1)-4): 4*(i+1)])+' '+max(f[4*(i+1)-4:4*(i+1)])+ ' ' + max(e[4*(i+1)-4:4*(i+1)])+ ' ' + min(f[4*(i+1)-4:4*(i+1)]) + '\n')
# for i in range(len())
# m.write()
#  tree.write(newcwd + xmlname, encoding="utf-8", xml_declaration=True)


from lxml.etree import Element, SubElement, tostring
from html.parser import HTMLParser
from xml.dom.minidom import parseString

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

# filename=open('E:/data/text_label/test_label/2/111.xml')
node_root = Element('annotation')

node_folder = SubElement(node_root, 'folder')
node_folder.text = 'JPEGImages'

node_filename = SubElement(node_root, 'filename')
node_filename.text = a

node_size = SubElement(node_root, 'size')
node_width = SubElement(node_size, 'width')
node_width.text = b

node_height = SubElement(node_size, 'height')
node_height.text = c

node_depth = SubElement(node_size, 'depth')
node_depth.text = '3'

node_object = SubElement(node_root, 'object')
node_name = SubElement(node_object, 'name')
node_name.text = d[0]
node_pose = SubElement(node_object, 'pose')
node_pose.text = 'Unspecified'
node_truncated = SubElement(node_object, 'truncated')
node_truncated.text = '0'
node_difficult = SubElement(node_object, 'difficult')
node_difficult.text = '0'
node_bndbox = SubElement(node_object, 'bndbox')
node_xmin = SubElement(node_bndbox, 'xmin')
node_xmin.text = min(e[0:4])
node_ymin = SubElement(node_bndbox, 'ymin')
node_ymin.text = max(f[0:4])
node_xmax = SubElement(node_bndbox, 'xmax')
node_xmax.text = max(e[0:4])
node_ymax = SubElement(node_bndbox, 'ymax')
node_ymax.text = min(f[0:4])
node_object = SubElement(node_root, 'object')
node_name = SubElement(node_object, 'name')
node_name.text = d[1]
node_pose = SubElement(node_object, 'pose')
node_pose.text = 'Unspecified'
node_truncated = SubElement(node_object, 'truncated')
node_truncated.text = '0'
node_difficult = SubElement(node_object, 'difficult')
node_difficult.text = '0'
node_bndbox = SubElement(node_object, 'bndbox')
node_xmin = SubElement(node_bndbox, 'xmin')
node_xmin.text = min(e[5:8])
node_ymin = SubElement(node_bndbox, 'ymin')
node_ymin.text = max(f[5:8])
node_xmax = SubElement(node_bndbox, 'xmax')
node_xmax.text = max(e[5:8])
node_ymax = SubElement(node_bndbox, 'ymax')
node_ymax.text = min(f[5:8])
# node_object = SubElement(node_root, 'object')
# node_name = SubElement(node_object, 'name')
# node_name.text = d[2]
# node_pose = SubElement(node_object, 'pose')
# node_pose.text = 'Unspecified'
# node_truncated = SubElement(node_object, 'truncated')
# node_truncated.text = '0'
# node_difficult = SubElement(node_object, 'difficult')
# node_difficult.text = '0'
# node_bndbox = SubElement(node_object, 'bndbox')
# node_xmin = SubElement(node_bndbox, 'xmin')
# node_xmin.text = min(e[9:12])
# node_ymin = SubElement(node_bndbox, 'ymin')
# node_ymin.text = max(f[9:12])
# node_xmax = SubElement(node_bndbox, 'xmax')
# node_xmax.text = max(e[9:12])
# node_ymax = SubElement(node_bndbox, 'ymax')
# node_ymax.text = min(f[9:12])
xml = tostring(node_root, pretty_print=True)  # 格式化显示，该换行的换行
dom = parseString(xml)
print(dom)
html_parser = HTMLParser()
tranform = html_parser.unescape(dom.toxml())
sname ='E:/data/text_label/test_label/2/'+ a[0:-4]+'.xml'
save_to_file(sname,tranform)