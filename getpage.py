import urllib.request  
import re  
url = 'http://699pic.com/zhuanti/hangpai.html'    
headers = {  
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'  
    }  
url1 = urllib.request.Request(url, headers=headers) # Request函数将url添加头部，模拟浏览器访问  
page = urllib.request.urlopen(url1).read()  # 将url页面的源代码保存成字符串  
page = page.decode('UTF-8')  # 字符串转码  
print('complate!')


reg=r'data-original="(http.*?.quality/90)"'
imgre=re.compile(reg)
imgList = re.findall(imgre,page)  
print(imgList)


x = 0  
for imgUrl in imgList:  # 列表循环  
    print('正在下载：%s'%imgUrl)  
        # urlretrieve(url,local)方法根据图片的url将图片保存到本机  
    urllib.request.urlretrieve(imgUrl,'D:/pyimgs/%d.jpg'%x)  
    x+=1
 
 
