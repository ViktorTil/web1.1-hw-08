from datetime import datetime
from mongoengine import *
from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField, ReferenceField



class Contacts(Document):
    fullname = StringField(max_length=30)
    phone_number = StringField(max_length = 25)
    email = StringField(max_length=40)
    send_message = BooleanField(default=False)
    
    
    
    
    
    
