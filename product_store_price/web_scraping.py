import requests
from glob import glob
from bs4 import BeautifulSoup

HEADERS_PICHAU = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'pt-BR, en;q=0.5'})

HEADERS_KABUM = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'pt-BR, en;q=0.5'})

HEADERS_AMERICANAS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'authority': 'www.americanas.com.br',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1'})

HEADERS_AMAZON = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'authority': 'www.amazon.com.br',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1'})

class WebScraping():
    
    def get_price_kabum(url):
        page = requests.get(url, headers=HEADERS_KABUM)
        soup = BeautifulSoup(page.content, features="lxml")
        
        try:
            price = float(soup.find_all("div",class_='preco_normal')[0].get_text().replace('.', '').replace('R$ ', '').replace(',', '.').strip())
        except:
            price = None

        try:
            price_discount = float(soup.find_all("span",class_='preco_desconto')[0].find_all("strong")[0].get_text().replace('.', '').replace('R$ ', '').replace(',', '.').strip())
        except:
            price_discount = None

        return ({'price': price, 'price_discount': price_discount})

    def get_price_pichau(url):
        page = requests.get(url, headers=HEADERS_PICHAU)
        soup = BeautifulSoup(page.content, features="lxml")

        try:
            price = float(soup.find_all("span",class_='price')[0].get_text().replace('.', '').replace('R$', '').replace(',', '.').strip())
        except:
            price = None

        try:
            price_discount = float(soup.find_all("span",class_='price-boleto')[0].find_all("span")[0].get_text().replace('.', '').replace('à vista R$', '').replace(',', '.').strip())
        except:
            price_discount = None

        return ({'price': price, 'price_discount': price_discount})

    def get_price_americanas(url):
        page = requests.get(url, headers=HEADERS_AMERICANAS)
        soup = BeautifulSoup(page.content, features="lxml")

        try:
            price = float(soup.find_all("div",class_='src__BestPrice-sc-1jvw02c-5 cBWOIB priceSales')[0].get_text().replace('.', '').replace('R$', '').replace(',', '.').strip())
        except:
            price = None

        return ({'price': price, 'price_discount': None})

    def get_price_amazon(url):
        page = requests.get(url, headers=HEADERS_AMAZON)
        soup = BeautifulSoup(page.content, features="lxml")

        try:
            price = float(soup.find(id='priceblock_ourprice').get_text().replace('.', '').replace('R$', '').replace(',', '.').strip())
        except:
            price = None

        return ({'price': price, 'price_discount': None})