import re
import random
import time
from bs4 import BeautifulSoup
from lxml import etree
import requests


songs = []
HEADERS = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/',
        }

with open('data/songlist.txt') as f:
    lines = f.readlines() 
    for line in lines:
        songs.append(re.sub('[^A-Za-z0-9]+', '', line).lower())

with open('data/drakelyrics.txt', 'a') as f:
    for i, song in enumerate(songs):
        url = 'https://www.azlyrics.com/lyrics/drake/' + song + '.html'
        page = requests.get(url, headers=HEADERS).text
        soup = BeautifulSoup(page, 'html.parser')
        dom = etree.HTML(str(soup))
        lyrics = dom.xpath('/html/body/div[2]/div[2]/div[2]/div[5]/text()')
        time.sleep(random.randint(4, 8))
        if len(lyrics) > 0:
            print('[', i+1, ":", song, ']', lyrics[0])
            for i in range(len(lyrics)):
                lyric = dom.xpath('/html/body/div[2]/div[2]/div[2]/div[5]/text()')[i]
                f.write(lyric)
        else:
            print('[', i+1, ':', song, ':',  'SCRAPING FAILED ]')
