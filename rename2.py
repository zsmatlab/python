import os
path = "/media/jianchao/datas/data/text_test/JPEGImages/"
f = os.listdir(path)
f.sort()
n = 1425
for i in f :
       oldname= path + i
       num =str(n)
       newname = path + num.zfill(6) + '.jpg'
       os.rename(oldname, newname)
       print(oldname,'--->',newname)
       n+=1
