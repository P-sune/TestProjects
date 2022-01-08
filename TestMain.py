import requests
from bs4 import BeautifulSoup




def parse():
    URL = 'https://auto.ru/sankt-peterburg/cars/used/do-150000/?sort=cr_date-desc&price_from=100000'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'

    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='ListingItem')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('a', class_='Link ListingItemTitle__link').get_text(strip=True),
            'price': item.find('div', class_='ListingItemPrice__content').get_text(strip=True),
            'gorod': item.find('div', class_='ListingItem__additionalInfo').get_text(strip=True),
            'god': item.find('div', class_='ListingItem__column ListingItem__column_middle').get_text(strip=True),
            'link': item.find('a', class_='Link ListingItemTitle__link').get('href')


        })

    for comp in comps:
        print(f'{comp["title"]} -> Price: {comp["price"]} -> Gorod: {comp["gorod"]} -> God: {comp["god"]} -> Link: {comp["link"]}')


parse()
