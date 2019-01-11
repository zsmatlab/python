import os
xml_path = "C:/Users/seeta/Desktop/test/xml/"
img_path = "C:/Users/seeta/Desktop/test/jpg/"
f = os.listdir(img_path)
f.sort()
n=20
for i in f :
       num = str(n)
       oldname = i.split('.')[0]
       img_oldname = img_path + oldname + '.jpg'
       xml_oldname = xml_path + oldname + '.xml'
       img_newname = img_path + num.zfill(4) + '.jpg'
       xml_newname = xml_path + num.zfill(4) + '.xml'
       os.rename(img_oldname, img_newname)
       print(img_oldname,'--->',img_newname)
       os.rename(xml_oldname, xml_newname)
       print(xml_oldname, '--->', xml_newname)
       n+=1



