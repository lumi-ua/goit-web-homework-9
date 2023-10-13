import json
from models import Authors, Quotes


authors_json_file = "authors.json"  
quotes_json_file = "quotes.json" 


# Завантаження даних з JSON-файлів
def load_json_data(file):
    with open(file, 'r', encoding='utf-8') as file:
        return json.load(file)


# Завантаження та збереження даних авторів
authors_data = load_json_data(authors_json_file)
for author_info in authors_data:
    author = Authors(**author_info)
    author.save()

# Завантаження та збереження даних цитат
quotes_data = load_json_data(quotes_json_file)
for quote_info in quotes_data:
    author_name = quote_info['author']
    author = Authors.objects(fullname=author_name).first()
    if author:
        quote_info['author'] = author
        quote = Quotes(**quote_info)
        quote.save()


if __name__ == '__main__':
    load_json_data(authors_json_file)
    load_json_data(quotes_json_file)
    print("Дані успішно завантажені.")
