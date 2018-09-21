import lxml.html
import urllib3
import certifi
import requests
import re
from bs4 import BeautifulSoup

http = urllib3.PoolManager(
       cert_reqs='CERT_REQUIRED',
       ca_certs=certifi.where())

url = http.request('GET', 'https://www.topsport.lt/lazybos-siandien/futbolas')
soup = BeautifulSoup(url.data, 'lxml')

topas = soup.findAll('div', attrs={'class': 'prelive-list'})
topas_text = topas.text
topas_strip = re.sub('[\n]+', '---', topas_text)
topas_clean = topas_strip.split('---')
