import requests
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
novel=res.text
a=open('code.txt','w', encoding = 'utf-8')
a.write(novel)
a.close()