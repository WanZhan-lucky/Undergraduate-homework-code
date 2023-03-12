import requests
from bs4 import BeautifulSoup
import xlwt
import pandas as pd

url = "http://www.boxofficecn.com/boxoffice"
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet("中国历年电影票房" )
listk = ['序列', '年份', '电影', '票房(万元)']
for i in range(len(listk)):
    worksheet.write(0, i, listk[i])

def downmovie2014(year):
    res = requests.get(url + str(year))
    print(url + str(year), end="   ->  ")
    res.encoding = 'utf-8'
    print(res.status_code)

    soup = BeautifulSoup(res.text, "html.parser")
    tbody = soup.find("tbody")
    items = tbody.find_all("tr")
    for item in items[1:]:
        movcontent = item.find_all("td")
        itemlist = []
        for mov in movcontent:
            kstr = mov.text
            itemlist.append(kstr)
        values = itemlist[-1]
        try:
            values = float(values)
            if (itemlist[1] == str(year)):
                itemlist[-1] = itemlist[-1].strip()
                if (str(year) == '2015' and (itemlist[0] == '157' or itemlist[0] == '172')):
                    continue
                for index in range(0, 4):
                       worksheet.write(n, index, itemlist[index])
                n = n + 1
        except Exception as e:
            pass
def downmovieticket(year):
    res = requests.get(url + str(year))
    print(url+str(year), end = "    -> ")
    res.encoding = 'utf-8'
    print(res.status_code)

    soup = BeautifulSoup(res.text, "html.parser")
    tbody = soup.find("tbody")
    items = tbody.find_all("tr", attrs={"align":"left"})
    n = 1
    for item in items:
        movcontent = item.find_all("td")
        itemlist = []
        for mov in movcontent:
            kstr = mov.text
            itemlist.append(kstr)
        values = itemlist[-1]
        try:
            values = float(values)
            if (itemlist[1] == str(year)):
                #itemlist[1] = int(itemlist[1])
                itemlist[-1] = itemlist[-1].strip()
                if (str(year) == '2015' and (itemlist[0] == '157' or itemlist[0] == '172')):
                    continue
                for index in range(0, 4):
                    print(n, index, itemlist[index])
                    worksheet.write(n, index, itemlist[index])
                n = n + 1
        except Exception as e:
            pass

if __name__ == "__main__":
    for year in range(2021, 2022):
        if (year == 2014):
            downmovie2014(year)
        else:
            downmovieticket(year)

workbook.save("中国2001-2021历年电影票房.xls")
