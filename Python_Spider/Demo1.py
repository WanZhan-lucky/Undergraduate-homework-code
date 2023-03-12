import requests

res = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md")
res.encoding = 'utf-8'
novel = res.text
print(novel)
k = open("./三国演义.txt", 'w', encoding = 'utf-8')
k.write(novel)
k.close()

#status_code
#content 二进制
#text 文本
#encoding