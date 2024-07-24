from homework_1.models import Author, Quote

def search_by_author(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [quote.quote for quote in quotes]
    return []

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [quote.quote for quote in quotes]

def main():
    while True:
        command = input("Введите команду: ")
        if command.startswith("name:"):
            name = command[len("name:"):].strip()
            results = search_by_author(name)
            for result in results:
                print(result)
        elif command.startswith("tag:"):
            tag = command[len("tag:"):].strip()
            results = search_by_tag(tag)
            for result in results:
                print(result)
        elif command.startswith("tags:"):
            tags = command[len("tags:"):].strip()
            results = search_by_tags(tags)
            for result in results:
                print(result)
        elif command == "exit":
            break
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()
