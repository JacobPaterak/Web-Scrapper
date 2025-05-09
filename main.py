from traceback import print_stack

import requests
from bs4 import (BeautifulSoup)


base_url = "https://migardener.com/en-ca/collections/all-seeds?page={}"
total_pages = 20
counter = 1
total_plants = []
total_prices = []
# plant_names = [plant.find('p', class_='product-card-title').text for plant in plants]

def Search():
    for plant,price in zip(total_plants,total_prices):
        print(plant)
        print(price)

for page_number in range(1, total_pages + 1):
    url = base_url.format(page_number)
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
    plants = soup.find_all('div', attrs={"class": "grid-product__title"})
    prices = soup.find_all('span', attrs = {"class":"visually-hidden" })
    for plant,price in zip(plants,prices):
        total_plants.append(plant.text)
        total_prices.append(price.text)





Search()

