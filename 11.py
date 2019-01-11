import os,shutil
xml_path = '600_1/'
jpg_path = '2/'
newxml_path = '600_2/'
a = []
for path, d, filelist in os.walk(xml_path):
    for filename in filelist:
        xml_name = filename.split('.')[0]
        xmls = os.path.join(path, filename)
        jpg_name = '2/' + xml_name + '.jpg'
        a.append(jpg_name)

        print(xmls)
    print(a)

for jpg in a:
    if os.path.exists(jpg):
        shutil.copy(jpg, r'600_2/')

