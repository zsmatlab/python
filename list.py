import os
f=open('C:/Users/seeta/Desktop/ke/icebox_1022/ice_box/list.txt', 'r+')
n=[]
for names in f:
   na = names.split('.')[0]
   n.append(na)
   #print(na)


for name in n:
  f.write(name + '\n')

  

