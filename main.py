import requests
from bs4 import BeautifulSoup
import json

# Функція для отримання даних про цитати та авторів зі сторінки
def scrape_quotes_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = []
    authors = []

    for quote_div in soup.find_all('div', class_='quote'):
        text = quote_div.find('span', class_='text').get_text()
        author_name = quote_div.find('small', class_='author').get_text()
        author_link = quote_div.find('a')['href']
        tags = [tag.get_text() for tag in quote_div.find_all('a', class_='tag')]

        author_url = f"http://quotes.toscrape.com{author_link}"
        author_response = requests.get(author_url)
        author_soup = BeautifulSoup(author_response.text, 'html.parser')

        born_date_text = author_soup.find('span', class_='author-born-date').get_text()
        born_location_text = author_soup.find('span', class_='author-born-location').get_text()
        description_text = author_soup.find('div', class_='author-description').get_text(strip=True)

        quotes.append({
            'quote': text,
            'author': author_name,
            'tags': tags
        })

        authors.append({
            'fullname': author_name,
            'born_date': born_date_text,
            'born_location': born_location_text,
            'description': description_text
        })

    return quotes, authors, soup

# Функція для збереження даних у JSON файл
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

# Основна функція
def main():
    base_url = "http://quotes.toscrape.com"
    quotes_url = base_url

    all_quotes = []
    all_authors = []

    while True:
        quotes, authors, soup = scrape_quotes_page(quotes_url)
        all_quotes.extend(quotes)
        all_authors.extend(authors)

        next_page_url = soup.find('li', class_='next')
        if next_page_url:
            quotes_url = base_url + next_page_url.find('a')['href']
        else:
            quotes_url = None
            break
    
    save_to_json(all_quotes, 'quotes.json')
    save_to_json(all_authors, 'authors.json')
    
if __name__ == "__main__":
    main()
    print('json файли завантажені успішно')
    

