import urllib.request
import requests
from bs4 import BeautifulSoup

url = "https://www.domecall.net/goods/goods_view.php?goodsNo="

request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
price = soup.select_one('#frmView > div > div.item > ul > li.price > div > strong')
bacode = soup.select_one('#frmView > div > div.item > ul > li:nth-child(2) > div')
productCode = soup.select_one('#frmView > div > div.item > ul > li:nth-child(3) > div')
origin = soup.select_one('#frmView > div > div.item > ul > li:nth-child(4) > div')
bigBoxCount = soup.select_one('#frmView > div > div.item > ul > li:nth-child(5) > div > span')
smallBoxCount = soup.select_one('#frmView > div > div.item > ul > li:nth-child(6) > div > span')

print(price)
print(bigBoxCount)
print(smallBoxCount)