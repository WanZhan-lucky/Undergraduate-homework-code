import requests
from bs4 import BeautifulSoup

url = "http://www.xiachufang.com/explore/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
res = requests.get(url, headers = headers)
print(res.status_code)
soup = BeautifulSoup(res.text, "html.parser")

listfoods = soup.find_all("div", class_ = "info pure-u")
listitems = []
for lifood in listfoods:
    k = lifood.find('a')
    name = k.text.strip()
    urlk = 'http://www.xiachufang.com'+k['href']
    tagp = lifood.find('p', class_ = "ing ellipsis")
    ingredits = tagp.text.strip()
    print(name, urlk, ingredits)
    listitems.append([name, urlk, ingredits])

print(listitems)



            


