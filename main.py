from traceback import print_stack

import requests
from bs4 import (BeautifulSoup)


base_url = "https://migardener.com/en-ca/collections/all-seeds?page={}"
total_pages = 20
counter = 1
total_plants = []
total_prices = []
# plant_names = [plant.find('p', class_='product-card-title').text for plant in plants]
def DisplayAll():
    for plant in total_plants:
        print(plant)
def Search(search):
    for plant,price in zip(total_plants,total_prices):
        if(search == plant):
            print(plant + " was found and it costs " + price)
            return
    print("Plant not found")

for page_number in range(1, total_pages + 1):
    url = base_url.format(page_number)
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
    plants = soup.find_all('div', attrs={"class": "grid-product__title"})
    prices = soup.find_all('span', attrs = {"class":"visually-hidden" })
    for plant,price in zip(plants,prices):
        total_plants.append(plant.text)
        total_prices.append(price.text)

print("Welcome to Jacobs plants search program")

print("\t1,) Do you want to search a plant up by name ")
print("\t2,) Do you want to list of all the plants available")
print()
userinput = input("What do you want to do ")
if(userinput == "1"):
    userPlant = input("What is the name of the plant you are looking for ")
    Search(userPlant)
elif(userinput == "2"):
    DisplayAll()
else:
    print("Invalid Input")

