from datetime import datetime
import json
from models import Authors, Quotes, Tag

import connect


authors = 'authors.json'
quotes = 'quotes.json'

def create_data_authors(file):
    with open(file, "r") as fh:
        data = json.load(fh)
        for author in data:
            Authors(fullname = author["fullname"], born_date = datetime.strptime(author["born_date"], '%B %d, %Y' ).date(),
                born_location = author["born_location"], description = author["description"]).save()


def create_data_quotes(file):
    with open(file, "r") as fh:
        quotes = json.load(fh) 
        for quote in quotes:
            author_from_authors = Authors.objects(fullname = quote["author"])[0]
            author_tags = [Tag(name=i) for i in quote["tags"]]
            quote_to_write = Quotes(tags = author_tags, author = author_from_authors, quote = quote["quote"])
            quote_to_write.save()


def run():
    create_data_authors(authors)
    create_data_quotes(quotes)
    
if __name__=="__main__":
    run()