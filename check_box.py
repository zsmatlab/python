import xml.etree.ElementTree as ET
import os
def cover(xmlpath, thresh = 20):
    error = []
    error_type = []
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
                    error_num = []
                    for i in range(len(Center) - 1):
                        c1 = Center[i]
                        for j in range(i + 1, len(Center)):
                            c2 = Center[j]
                            d = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
                            if d < thresh:
                               error.append(oldname)
                               error_num.append(j)
                    error_type.append(str(len(error_num)))
    error = list(set(error))
    error.sort()
    error_type = [x for x in error_type if x != '0']
    for i in range(len(error)):
        keys = error[i]
        print('containing cover boxes : ', keys, error_type[i],'个')

def minibox(xmlpath, thresh = 20):
    error = []
    errors_nums = []

    for path, d, filelist in os.walk(xmlpath):
        for xmlname in filelist:
            if xmlname.endswith('xml'):
                oldname = os.path.join(path, xmlname)
                tree = ET.parse(oldname)
                objs = tree.findall('object')
                n = 0
                m = []
                for ix, obj in enumerate(objs):
                    box = obj.find('bndbox')
                    if box is None:
                        continue
                    else:
                        xmin = float(box.find('xmin').text.strip())
                        ymin = float(box.find('ymin').text.strip())
                        xmax = float(box.find('xmax').text.strip())
                        ymax = float(box.find('ymax').text.strip())

                        width = xmax - xmin
                        hight = ymax - ymin
                        n+=1

                        if width < thresh or hight < thresh:
                            error.append(oldname)
                            m.append(n)
                errors_nums.append(str(len(m)))

    errors = list(set(error))
    errors.sort()
    error_num = [x for x in errors_nums if x != '0']
    for i in range(len(errors)):
        keys = errors[i]
        nums = error_num[i]
        print('containing small boxes : ', keys, nums, '个')


def point(xmlpath):
    errors =[]
    errors_nums=[]
    for path, d, filelist in os.walk(xmlpath):
        for xmlname in filelist:
            if xmlname.endswith('xml'):
                oldname = os.path.join(path, xmlname)
                tree = ET.parse(oldname)
                objs = tree.findall('object')
                n = 0
                for ix, obj in enumerate(objs):
                        x = obj.find('point')
                        if x is None :
                            continue
                        else:
                            errors.append(oldname)
                            n+=1

                errors_nums.append(str(n))

    errors = list(set(errors))
    errors.sort()
    errors_nums = [x for x in errors_nums if x != '0']
    for i in range(len(errors)):
        keys = errors[i]
        nums = errors_nums[i]
        print('containing point boxes : ', keys, nums, '个')



if __name__ == '__main__':
    print("~~~~~~~~~~~~~~~~~~~check cover  boxes~~~~~~~~~~~~~~~~~")
    cover(xmlpath=r'E:\data\new_icebox\new_data\Annotations\files/',
            thresh=20
            )

    print("~~~~~~~~~~~~~~~~~~~check mini boxes~~~~~~~~~~~~~~~~~~~")
    minibox(xmlpath=r'E:\data\new_icebox\new_data\Annotations\files/',
          thresh=15
          )

    print("~~~~~~~~~~~~~~~~~~~check point boxes~~~~~~~~~~~~~~~~~~~")
    point(xmlpath=r'E:\data\new_icebox\new_data\Annotations\files/'
          )
