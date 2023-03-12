import requests
from bs4 import BeautifulSoup

url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
res = requests.get(url)
print(res.status_code)
soup = BeautifulSoup(res.text, "html.parser")
#print(soup)
#soup是BeautifulSoup的ResultSet对象，属性有find, find_all
print(soup.find_all("div"))
print(type(soup.find_all("div")))
#find_all(标签，属性)
#find(标签，属性)

#tag对象，
#tag.find_all, tag.find
#tag.text
#tag['属性名']
