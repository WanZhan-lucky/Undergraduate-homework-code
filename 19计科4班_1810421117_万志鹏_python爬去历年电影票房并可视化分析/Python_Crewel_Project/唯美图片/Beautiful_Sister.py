import requests
from bs4 import BeautifulSoup
import re
rek = re.compile(r"_(\d{1,2})")
init_url = "https://www.umei.cc/meinvtupian/meinvxiezhen/"
res = requests.get(init_url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, "html.parser")
item = soup.find("div", attrs= {"class":"TypeList"})
iks = item.find_all("li")
n = 1
for ik in iks:
    href = ik.find("a").get("href")
    next_url = "https://www.umei.cc/"+href
    res_next = requests.get(next_url)
    res_next.encoding = 'utf-8'
    soup_next = BeautifulSoup(res_next.text, "html.parser")
    soup_items = soup_next.find("div", attrs = {"class":"ImageBody"})
    imag_href = soup_items.find("img").get("src")
    download_imag = requests.get(imag_href)
    f = open("WeiMeiImage_%d.jpg" % n, "wb")#wb写入二进制
    f.write(download_imag.content)
    print("第%d张图片下载完毕!" % n)
    n = n + 1





#提取套图页数
# print(imag_href)
# last_href = soup_next.find("div", attrs = {"class":"NewPages"}).find_all("a")[-1]
# print(type(last_href))
# sk = last_href.get("href")
# t = re.findall(rek, sk)
# num = int(t[0])

'''
find("div", attrs={"class" : "fjkdsaf"})
#拿属性  k['href']/k.get('href')
find_next找下一个
strip("\"")
'''