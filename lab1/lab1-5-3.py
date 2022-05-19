#-*- coding: utf-8 -*-
try:
    from urllib.request import urlopen #python 3
    from tkinter import *

except ImportError:
    from urllib2 import urlopen #python 2
    from Tkinter import *

from bs4 import BeautifulSoup
from tkinter import *


def get_covid(covid):
    page = urlopen("https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%98%84%ED%99%A9")
    
    text = page.read().decode("utf-8")
    soup = BeautifulSoup(text, "html.parser")

    table = soup.select("div.status_info > ul > li")

    for item in table:
        title = item.select("strong.info_title")
        value = item.select("p.info_num")

        if title[0].string == covid:
            tempV.set(u'Value: ' + value[0].string)
            print(value[0].string, title[0].string)
            break


def refresh(*args):
    get_covid(covid19.get())

app = Tk()
app.title("COVID-19")
app.geometry("400x200+800+400")
Label(app, text="Select: ").pack(side="left")

covid_list = ["일일 확진", "재원 위중증", "신규 입원", "일일 사망"]
covid19 = StringVar()
covid19.set(covid_list[0])
covid19.trace("w", refresh)

OptionMenu(app, covid19, *covid_list).pack(side="right")
tempV = StringVar()
tempV.set("Value: ")

Label(app, textvariable=tempV).pack(pady=40,side="top")
Button(app, text="Refresh", command=refresh).pack(pady=40, side="bottom")

app.mainloop()