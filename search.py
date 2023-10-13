from models import Authors, Quotes

if __name__ == "__main__":


    while True:
        command = input(">>>: ")

        if command.lower() == 'exit':
            break

        parts = command.split(':')
        if len(parts) != 2:
            print("Некоректний формат команди. Потрібно - name: <Призвіще автора>, або tag: <назва тега>")
            continue

        keyword, value = parts[0].strip(), parts[1].strip()

        if keyword == 'name':
            author = Authors.objects(fullname=value).first()
            if author:
                quotes = Quotes.objects(author=author)
                for quote in quotes:
                    print(quote.quote)

        elif keyword == 'tag':
            quotes = Quotes.objects(tags=value)
            for quote in quotes:
                print(quote.quote)

        elif keyword == 'tags':
            tags = value.split(',')
            quotes = Quotes.objects(tags__in=tags)
            for quote in quotes:
                print(quote.quote)

        else:
            print("Некоректний ключ команди.")