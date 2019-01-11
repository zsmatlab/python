import os
path='/home/seeta/'
names = os.listdir(path)
print(names)
i = 1
for folder in names:
	new_path=os.path.join(path,folder)
	print(new_path,i)
	w = open(new_path,'r+')
	lines = w.readlines()
	j = 1
	for l in lines:
		print('the sixth char is :',a)
		if a != '0' and a != '11':
			print('new%s:'%(j),l)
			if j == 1:
				w.seek(0)
				w.truncate()
			else:
				w.write()
			j+=1
    i+=1
print('all complate!')