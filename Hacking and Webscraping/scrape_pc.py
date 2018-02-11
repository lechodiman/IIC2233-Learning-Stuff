import requests
from bs4 import BeautifulSoup
import pandas as pd

pc_1 = {
    'g450': 'https://www.spdigital.cl/products/view/55007',
    'placa': 'https://www.spdigital.cl/products/view/54895',
    'hdd': 'https://www.spdigital.cl/products/view/32720',
    'ram': 'https://www.spdigital.cl/products/view/55697',
    'fuente': 'https://www.spdigital.cl/products/view/55870',
    'kit_gabinete': 'https://www.spdigital.cl/products/view/51538',
    'zotac_1050': 'https://www.spdigital.cl/products/view/53740'
}

pc_2 = {
    'g450': 'https://www.spdigital.cl/products/view/55007',
    'placa': 'https://www.spdigital.cl/products/view/54895',
    'hdd': 'https://www.spdigital.cl/products/view/32720',
    'ram': 'https://www.spdigital.cl/products/view/55697',
    'fuente': 'https://www.spdigital.cl/products/view/55870',
    'thermaltake': 'https://www.spdigital.cl/products/view/55946',
    'zotac_1050': 'https://www.spdigital.cl/products/view/53740'
}


def get_soup(url):
    # Make request to get content
    req = requests.get(url)

    # Make soup
    soup = BeautifulSoup(req.content, 'html.parser')

    return soup


def get_price(soup):
    # Get the price div in the soup
    price = soup.find_all('div', {'class': 'product-view-cash-price-div product-view-cash-price text-webstore'})

    return int(price[0].text.replace('$', '').strip())


def get_units(soup):
    # get the div of units
    divs = soup.find_all('div', {'class': 'product-view-stock'})

    units_left = divs[0].span.text.strip()

    return units_left.replace(' UNIDADES', '') if ' UNIDADES' in units_left else units_left


def scrape_pieces_to_df(products=pc_1):

    names = []
    prices = []
    list_units = []

    for prod, url in products.items():
        soup = get_soup(url)

        price = get_price(soup)
        units = get_units(soup)

        names.append(prod)
        prices.append(price)
        list_units.append(units)

    df = pd.DataFrame({'Name': names, 'Price': prices, 'Units': list_units})

    return df


if __name__ == '__main__':
    df_1 = scrape_pieces_to_df(pc_1)
    df_1.to_excel('PC-low-profile-1.xlsx', index=False)

    df_2 = scrape_pieces_to_df(pc_2)
    df_2.to_excel('PC-low-profile-2.xlsx', index=False)
