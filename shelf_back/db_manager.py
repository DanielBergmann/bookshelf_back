from playhouse.db_url import connect
from playhouse.postgres_ext import (
    ArrayField,
    BooleanField,
    IntegerField,
    CharField,
    DateTimeField,
    fn,
    ForeignKeyField,
    Model,
    TextField
)



psql_db = connect("postgresql://postgres:postgres@127.0.0.1/BOOK_SHELF")


class BaseModel(Model):
    class Meta:
        database = psql_db


class Book2(BaseModel):
    title=CharField()
    authorid=IntegerField()
    read_status=IntegerField(default=0)
    priority=IntegerField(default=0)
    description=TextField(default='')

    class Meta:
        indexes = (
            (('title', 'author', 'read_status', 'priority',
              'description'), True),
        )


class Author(BaseModel):
    name = CharField()
    description = CharField()
    class Meta:
        indexes = (
            (('name','description'), True),
        )


def get_authors():
    query = Author.select()
    return query


def get_author(author_id):
    query = Author.select().where(Author.id == author_id)
    return query


def get_books():
    query = Book2.select().order_by(Book2.id.asc())
    return query


def get_book(book_id):
    query = Book2.select().where(Book2.id == book_id)
    return query


def add_book(payload):
    author = payload[1]
    #test = list(get_authors_by_name(author).dicts())[0]['id']
    test = get_authors_by_name(author)[0]
    Book2.create(title=payload[0], author=test, read_status=0,description = payload[2], priority=payload[3])
    return test


def change_book(book_id, payload):
    return 0


def get_authors_by_name(name):
    query = Author.get_or_create(name = name)
    return query

#print(list(get_authors().dicts())[0])
#print(list(get_authors_by_name().dicts()))
#payload = ['some book', 'Bergmann', 'descr', '4']
#print(add_book(payload))
