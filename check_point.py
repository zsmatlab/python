import xml.etree.ElementTree as ET
import os
def cover(xmlpath, thresh = 20):
    for path, d, filelist in os.walk(xmlpath):
        for xmlname in filelist:
            if xmlname.endswith('xml'):
                oldname = os.path.join(path, xmlname)
                tree = ET.parse(oldname)
                objs = tree.findall('object')
                BB = {}
                Center = {}
                m = 0
                for ix, obj in enumerate(objs):
                        box = obj.find('bndbox')
                        x = obj.find('point')
                        while x:
                            break
                        else:
                            xmin = float(box.find('xmin').text.strip())
                            ymin = float(box.find('ymin').text.strip())
                            xmax = float(box.find('xmax').text.strip())
                            ymax = float(box.find('ymax').text.strip())
                            b = [xmin, ymin, xmax, ymax]
                            BB[m] = b
                            Center[m] = ((xmax + xmin) / 2.0, (ymax + ymin) / 2.0)
                            m+=1

                if len(Center) > 0:
                    for i in range(len(Center) - 1):
                        c1 = Center[i]
                        for j in range(i + 1, len(Center)):
                            c2 = Center[j]
                            d = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
                            if d < thresh:
                                print('containing double boxes : ', oldname)
                                pass

def minibox(xmlpath, thresh = 20):
    for path, d, filelist in os.walk(xmlpath):
        for xmlname in filelist:
            if xmlname.endswith('xml'):
                oldname = os.path.join(path, xmlname)
                tree = ET.parse(oldname)
                objs = tree.findall('object')
                n = 0
                for ix, obj in enumerate(objs):
                    box = obj.find('bndbox')
                    y = obj.find('point')
                    while y:
                        break
                    else:
                        xmin = float(box.find('xmin').text.strip())
                        ymin = float(box.find('ymin').text.strip())
                        xmax = float(box.find('xmax').text.strip())
                        ymax = float(box.find('ymax').text.strip())

                        width = xmax - xmin
                        hight = ymax - ymin
                        n+=1

                        if width < thresh or hight < thresh:
                            print('containing small boxes : ', oldname)
                            pass


def point(xmlpath):
    for path, d, filelist in os.walk(xmlpath):
        for xmlname in filelist:
            if xmlname.endswith('xml'):
                oldname = os.path.join(path, xmlname)
                tree = ET.parse(oldname)
                objs = tree.findall('object')
                for ix, obj in enumerate(objs):
                        x = obj.find('point')
                        while x :
                            print('containing point : ', oldname)
                            break








if __name__ == '__main__':
    print("~~~~~~~~~~~~~~~~~~~check cover  boxes~~~~~~~~~~~~~~~~~")
    cover(xmlpath=r'/media/jianchao/SEETADATA/icebox_new/标注/20181219',
            thresh=20
            )

    print("~~~~~~~~~~~~~~~~~~~check mini boxes~~~~~~~~~~~~~~~~~~~")
    minibox(xmlpath=r'/media/jianchao/SEETADATA/icebox_new/标注/20181219/',
          thresh=15
          )

    print("~~~~~~~~~~~~~~~~~~~check point boxes~~~~~~~~~~~~~~~~~~~")
    point(xmlpath=r'/media/jianchao/SEETADATA/icebox_new/标注/20181219/')
