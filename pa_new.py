import urllib.request
import urllib.parse
import re
import time
from selenium import webdriver
import os

def get_class(url,sort,start,end,path):
    num = start
    pic_name = []
    for i in range(end):
        new_url = url + 'sort/'+ sort +'?pageSize=28&pageNumber=' + str(num)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
        url_1 = urllib.request.Request(new_url, headers=headers)
        page1 = urllib.request.urlopen(url_1).read().decode('utf-8')
        pic_pipei = r'href+=([^\s]+search.[\u4e00-\u9fa5]*)'  # 正则表达式
        pic_name1 = re.findall(re.compile(pic_pipei), page1)  # 在页面中找到正则匹配到的所有文本，并存放为数组
        pic_name.extend(pic_name1)  # 合并数组
        num += 1
    for i in pic_name:
        cla_name = urllib.parse.quote(i[2:])  # 获取栏目名字（为中文），翻译为URL编码
        url_1 = url + cla_name  # 链接拼接
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url_1)
        time.sleep(1)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        time.sleep(1)
        html_source = driver.page_source
        driver.quit()
        file_name = urllib.parse.unquote(cla_name.split('/')[1])  # 翻译为中文文件名
        reg = r'src="([a-zA-Z]+://[^\s]+.gif_s400x0)"'  # 正则表达式
        imgre = re.compile(reg)  # 正则匹配图片路径
        imgList = re.findall(imgre, html_source)  # 在页面中找到所有图片路径,并写入数组
        print(file_name, len(imgList))  # 输出类别和类别数量
        path = (path+'%s' % file_name)  # 设置保存路径及文件夹名称
        if (os.path.exists(path)):
            continue
        else:
            os.makedirs(path)
            for imgUrl in imgList:
                t = time.time() * 1000
                # 列表循环
                print('正在下载：%s' % imgUrl)
                try:
                    urllib.request.urlretrieve(imgUrl, path + '/%s.gif' % str(int(t)))  # 保存图片
                except:
                    continue
                else:
                    print('~~~~~~~~~~~~~~~~~~~下载成功!~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if __name__ == '__main__':
    get_class(url='https://www.soogif.com/', sort='139', start=1, end=1, path='E:/2/')

