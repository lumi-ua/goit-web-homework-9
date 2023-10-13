from mongoengine import *

connect(host='mongodb+srv://goitlearn:77766@cluster0.gud02oa.mongodb.net/?retryWrites=true&w=majority')

class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    quote = StringField()
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=50))
    
    
