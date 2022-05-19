from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://se.deu.ac.kr/se/index.do")
bsObj = BeautifulSoup(html.read(), "html.parser")
nameList = bsObj.findAll("span")

for name in nameList:
    print(name.get_text())