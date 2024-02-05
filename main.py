from parser import BaseParser
from time import time


class CreditasiaParser(BaseParser):
    def __init__(self):
        super(CreditasiaParser, self).__init__()

    def categories_page(self):
        soup = self.get_soup(self.get_html())
        category_all = soup.find('div', class_='form-filter')
        categories = category_all.find_all('li')
        for category in categories[15:16:]:
            category_title = category.get_text(strip=True)
            print(category_title)

            category_link = self.HOST + category.find('a')['href']
            print(category_link)

            self.products_page(category_title, category_link)

    def products_page(self, category_title, category_link):
        page_number = 1
        while True:
            if page_number == 1:
                page_link = category_link
            else:
                page_link = f'{category_link}?PAGEN_2={page_number}'

            soup = self.get_soup(self.get_html(page_link))
            products_catalog = soup.find('div', class_='flex-catalog')
            products_all = products_catalog.find_all('div', class_='product_slider-card')
            for product in products_all:
                product_title = product.find('a', class_='product_slider-name').get_text()
                print(product_title)

                product_link = self.HOST + product.find('a')['href']
                print(product_link)

                product_img = self.HOST + product.find('img')['data-lazy']
                print(product_img)

                product_price = product.find('div', class_='price').get_text()
                print(product_price)

            next_page = soup.find('a', class_='blog-page-next')
            if not next_page:
                break
            page_number += 1


def start_parsing():
    start = time()
    parser = CreditasiaParser()
    parser.categories_page()
    finish = time()
    print(finish - start)


start_parsing()
