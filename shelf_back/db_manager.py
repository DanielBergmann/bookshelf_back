from playhouse.db_url import connect
from playhouse.postgres_ext import (
    ArrayField,
    BooleanField,
    CharField,
    DateTimeField,
    fn,
    ForeignKeyField,
    Model,
    TextField
)
psql_db = connect("postgresql://postgres:postgres@127.0.0.1/BOOK_SHELF")
