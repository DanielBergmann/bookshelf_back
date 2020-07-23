import peewee
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
    TextField,
)


psql_db = connect("postgresql://postgres:postgres@127.0.0.1/BOOK_SHELF")


class BaseModel(Model):
    class Meta:
        database = psql_db


class Book2(BaseModel):
    title = CharField()
    authorid = IntegerField()
    read_status = IntegerField(default=0)
    priority = IntegerField(default=0)
    description = TextField(default="")

    class Meta:
        indexes = (
            (("title", "author", "read_status", "priority", "description"), True),
        )


class Author(BaseModel):
    name = CharField()
    description = CharField()

    class Meta:
        indexes = ((("name", "description"), True),)


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
    author = payload['author']
    # test = list(get_authors_by_name(author).dicts())[0]['id']
    test = get_authors_by_name(author)[0]
    Book2.get_or_create(
        title=payload['title'],
        authorid=test,
        read_status=0,
        description=payload['description'],
        priority=payload['priority'],
    )
    return test


def change_status(payload):
    query = Book2.update(read_status=payload["read_status"]).where(
        Book2.id == payload["id"]
    )
    query.execute()
    return query

def change_book(payload):
    # {'id': 1, 'title': 'meditations', 'authorid': 'Marcus Aurelius', 'read_status': '1', 'priority': 0, 'description': 'cool book, thanks'}
    author = payload["author"]
    test = get_authors_by_name(author)[0]

    query = Book2.update(read_status=payload["read_status"],
                         title=payload["title"],
                         authorid=test,
                         priority=payload["priority"],
                         description=payload["description"]).where(
        Book2.id == payload["id"]
    )
    # Book2.update(title=payload.title).where(Book2.id == payload['id'])
    query.execute()
    return query

def delete_book_by_id(book):
    query = Book2.delete().where(Book2.id == book['id'])
    query.execute()
    return query

def get_authors_by_name(name):
    query = Author.get_or_create(name=name)
    return query


# print(list(get_authors().dicts())[0])s
# print(list(get_authors_by_name().dicts()))
# payload = ['some new book', 'author_test', 'descr', '4']
# print(add_book(payload))
