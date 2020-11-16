import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'наука']

URL = 'https://habr.com/ru/all/'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')


for article in soup.find_all('article', class_ = 'post post_preview'):
    hubs = article.find_all('div', class_ = 'post__text post__text-html post__text_v1')
    hubs_text = list(map(lambda x: x.text.lower(), hubs))
    full_text = ' '.join(hubs_text)


    for dh in KEYWORDS:
        if dh in full_text:
            date_element = article.find('span', class_ = 'post__time')
            date = date_element.text
            title_element = article.find('a', class_ = 'post__title_link')
            title = title_element.text
            link = title_element.attrs.get('href')
            print(f'{date} - {title} - {link}')
            break

