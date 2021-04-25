import os
import requests
from bs4 import BeautifulSoup

study_link = []
URL = 'https://exploreidea.net/category/xplore-answers/xplore-answers-python/'
page = 'page/'
url_list = [URL,URL+page+'1/',URL+page+'2/',URL+page+'3/',URL+page+'4/']
for url in url_list:
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    articles = soup.find_all('article',class_='post')
    for article in articles:
        x = article.find('div',class_='post-image')
        link = x.a.get('href')
        study_link.append(link)
# delete file if exists
if os.path.exists("study.txt"):
    os.remove("study.txt")
# writing the latest data into the file
fileappend = open("study.txt","a+")
for data in study_link:
    fileappend.write(data)
    fileappend.write("\n")
fileappend.close()

    