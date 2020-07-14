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

class Books(BaseModel):
    title=CharField()
    author=CharField()
    read_status=IntegerField(default=0)
    priority=IntegerField(default=0)
    description=TextField(default='')

    class Meta:
        indexes = (
            (('title', 'author', 'read_status', 'priority',
              'description'), True),
        )


def get_books():
    query = Books.select().order_by(Books.id.asc())
    return query


def get_book(book_id):
    query = Books.select().where(Books.id == book_id)
    return query


def add_book(book_id, payload):
    return 0


def change_book(book_id, payload):
    return 0
