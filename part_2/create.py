from faker import Faker

from models import Contacts
import connect

NUMBER_CONTACTS = 10

fake = Faker("uk-UA")

def create_data_contacts(number):
    for _ in range(number):
        Contacts(fullname = fake.name(), phone_number = fake.phone_number(), email = fake.email()).save()

def run():
    create_data_contacts(NUMBER_CONTACTS)
 
    
if __name__=="__main__":
    run()