import requests
from bs4 import BeautifulSoup
import pprint

url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100168537&IsNodeId=1&page=1&bop=And&ActiveSearchResult=True&order=RATING'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
links = soup.find_all('a', attrs = {'class' : 'item-title'})
prices = soup.find_all('li', attrs = {'class' : 'price-current'})
title_list = []
href_list = []
price_strong_list = []
price_sup_list = []

for link in links:
	title_list.append(link.text)
	href_list.append(link['href'])
for price in list(prices):
	price_strong_list.append(price.strong.text)
	price_sup_list.append(price.sup.text)

zipped_list = zip(title_list[:10], href_list[:10], price_strong_list[:10], price_sup_list[:10])
num = 0

print(f'\n-Best rated cooling systems-\n----------------------------------------------------------------')
for zipped_item in zipped_list:
	num += 1
	title, url, price_strong, price_sup = zipped_item
	print(f'{num}. {title}\n${price_strong}{price_sup}\n{url}\n----------------------------------------------------------------')
