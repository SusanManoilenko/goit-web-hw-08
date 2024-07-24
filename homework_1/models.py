import mongoengine as me

# Подключение к MongoDB Atlas
me.connect(host="mongodb+srv://manoilenkosuzik:www4556www@cluster2.dy3zna5.mongodb.net/Cluster2?retryWrites=true&w=majority&appName=Cluster2")

class Author(me.Document):
    fullname = me.StringField(required=True)
    born_date = me.StringField()
    born_location = me.StringField()
    description = me.StringField()

    def __str__(self):
        return self.fullname

class Quote(me.Document):
    tags = me.ListField(me.StringField())
    author = me.ReferenceField(Author, reverse_delete_rule=me.CASCADE)
    quote = me.StringField(required=True)

    def __str__(self):
        return self.quote
