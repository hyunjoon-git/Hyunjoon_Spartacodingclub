import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client['scc-w4']


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


page_url = "https://www.genie.co.kr/chart/top200"
data = requests.get(page_url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

genie = soup.select('#body-content > div.newest-list > div.music-list-wrap > table > tbody > tr')

rank = 0

for song in genie:
    if not song.a == None:
        rank = rank + 1

        doc = {}
        doc['rank'] = rank
        doc['title'] = song.select('a.title')[0].text
        doc['artist'] = song.select('a.artist')[0].text
        db.genie.insert_one(doc)



