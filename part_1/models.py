from datetime import datetime
from mongoengine import *
from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import DateTimeField, EmbeddedDocumentField, ListField, StringField, ReferenceField


class Tag(EmbeddedDocument):
    name = StringField(max_length=15)


class Authors(Document):
    fullname = StringField(max_length=30)
    born_date = DateTimeField()
    born_location = StringField(max_length=40)
    description = StringField()
    
class Quotes(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField(Authors, reverse_delete_rule = CASCADE)
    quote = StringField()
    
    
    
    
    
