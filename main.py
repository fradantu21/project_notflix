import os
from warnings import catch_warnings
from bs4 import BeautifulSoup
import requests



try:

    movie = input("insert title : ")

    movie = movie.replace(" ", "+")

    response = requests.get(f'https://www.1337xx.to/search/{movie}/1/')

    with open("index.html" ,"w" ,encoding="utf-8") as f:
        f.write(response.text)

    with open("index.html" ,"r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")

    td = soup.find_all("td" , class_="coll-1 name")
    sizes = soup.find_all("td" , class_="coll-4 size mob-uploader")

    links = []
    i = 0

    for elem in td:
        e = elem.find_all("a")[-1]
        links.append({e.text+" ["+sizes[i].text+"]": e["href"]})
        i+=1

    i = 0
    for link in links:
        for l in link:
            print(i, l)
        i+=1


    number = int(input("insert number: "))

    for l in links[number]:
        mag_link = links[number][l]  

    mag_link="https://www.1337xx.to"+mag_link

    #print(mag_link)

    page = requests.get(mag_link)

    with open("page.html" ,"w" ,encoding="utf-8") as f:
        f.write(page.text)

    with open("page.html" ,"r", encoding="utf-8") as f:
        content_page = f.read()

    pg = BeautifulSoup(content_page, "html.parser")

    ul = pg.find_all("ul" , class_ = "dropdown-menu")

    a = ul[-1].find_all("a")

    final_link = a[-1]['href']

    os.system(f'peerflix "{final_link}" --vlc -r ')
except KeyboardInterrupt:
    quit()