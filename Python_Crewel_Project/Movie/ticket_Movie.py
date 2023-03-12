import requests
from bs4 import BeautifulSoup
import xlwt
import pandas as pd

fmovie = open("movie1994-2021.csv", mode='w', encoding = "utf-8")

url = "http://www.boxofficecn.com/boxoffice"

def downmovie2014(year):
    res = requests.get(url + str(year))
    print(url + str(year), end = "  -> ")
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
                for index in range(0, len(itemlist)):
                    fmovie.write(itemlist[index])
                    fmovie.write(",")
                fmovie.write("\n")
        except Exception as e:
            # print(e)
            pass

def downmovieticke(year):
    res = requests.get(url + str(year))
    print(url+str(year) ,end = "  -> ")
    res.encoding = 'utf-8'
    print(res.status_code)

    soup = BeautifulSoup(res.text, "html.parser")
    tbody = soup.find("tbody")
    items = tbody.find_all("tr", attrs={"align":"left"})
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
                #print(itemlist)
                if (str(year) == '2015' and (itemlist[0] == '157' or itemlist[0] == '172')):
                    continue
                for index in range(0, len(itemlist)):
                    fmovie.write(itemlist[index])
                    fmovie.write(",")
                fmovie.write("\n")
        except Exception as e:
            #print(e)
            pass

for year in range(1994, 2022):
    if (year == 2014):
        downmovie2014(year)
    else:
        downmovieticke(year)
