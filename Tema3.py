import requests
from bs4 import BeautifulSoup

URL = 'https://www.pcgarage.ro/notebook-laptop/asus/gaming-156-rog-strix-g15-g512lv-fhd-240hz-procesor-intel-core-i7-10870h-16m-cache-up-to-500-ghz-16gb-ddr4-1tb-ssd-geforce-rtx-2060-6gb-no-os-black/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="product_name").get_text()
price = soup.find("span", {"class": "price_num"}).get_text()

print(title.strip())
print(price)
