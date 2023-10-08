from models import Authors, Quotes
import connect
import create

command_list = ['name', 'tag', 'tags']
commands_exit = ['ex', 'exit', 'q', 'quit']

def find_name(name):
    name = name.title()
    try:
        name_obj = Authors.objects(fullname = name)[0] 
        quotes_list = Quotes.objects(author = name_obj)
        for quote in quotes_list:
            print(f"{name_obj.fullname} : {quote.quote}")
    except IndexError:
        print(f"No such name: {name} in your's database!!!")

def find_tag(tag):
    quotes = Quotes.objects(tags__name=tag)
    if quotes:
        for quote in quotes:
            print(f"{quote.author.fullname} : {quote.quote}")
    else:
        print(f"There are not quotes with tag: {tag}")


def find_tags(tags):
    tags = tags.split(',')
    quotes = Quotes.objects(tags__name__in=tags)
    if quotes:
        for quote in quotes:
            print(f"{quote.author.fullname} : {quote.quote}")
    else:
        print(f"There are not quotes with any tag from list of tags: {tags}") 

if __name__ == "__main__":
    create.run()
    message = (f"Enter the command script from list: {', '.join(i+':'+'['+i+']' for i in command_list)} "
              f"or enter any command from list: {', '.join(commands_exit)} for EXIT")
    while True:
        print(message)
        command = input(f"Enter the command script > ").lower().split(":")
        if command[0] in commands_exit:
            break 
        try:
            globals()['find_'+command[0]](command[1])
        except KeyError:
            print(f"No such command: {command[0]} in your command-list!!!")
        except IndexError:
            print(f"Enter!!! the right script")



