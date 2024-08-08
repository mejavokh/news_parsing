from bs4 import BeautifulSoup
import requests
import json
import os


def get_info():
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }

    url = 'https://kun.uz/ru'
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')

    categories_block = soup.find('ul', class_='header-bottom__list')
    categories = categories_block.find_all('a', class_='header-bottom__link')

    all_categories_dict = []

    for category in categories:
        cat_title = category.get_text(strip=True)
        cat_link = 'https://kun.uz' + category.get('href')

        all_categories_dict.append({
            'title': cat_title,
            'link': cat_link
        })

    if not os.path.exists('date'):
        os.makedirs('date')

    with open('date/all_category_dict.json', 'w', encoding='utf-8') as file:
        json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

    with open('date/all_category_dict.json', encoding='utf-8') as file:
        all_categories = json.load(file)

    article_block = soup.find('ul', class_='main-news__right-list')
    articles = article_block.find_all('li', class_='main-news__right-item')

    all_articles_dict = []

    for article in articles:
        title = article.find('a', class_='main-news__right-link').text
        desc = article.find('p', class_='main-news__right-text').text

        all_articles_dict.append({
            'title': title,
            'description': desc
        })

    with open(f'date/all_articles_dict.json', 'w', encoding='utf-8') as file:
        json.dump(all_articles_dict, file, indent=4, ensure_ascii=False)

    with open(f'date/all_articles_dict.json', encoding='utf-8') as file:
        all_articles = json.load(file)


def main():
    print(get_info())


if __name__ == '__main__':
    main()
