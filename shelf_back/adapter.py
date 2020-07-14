from .db_manager import(
    get_books,
    get_book,
)
from funcy import walk, walk_values, is_seqcoll, is_mapping, autocurry


def get_books_all():
    test = get_books()
    return recursive_walk(w, list(test.dicts()))


def get_book_details(book_id):
    test = get_book(book_id).dicts()[0]
    return recursive_walk(w, test)


def add_book_to_storage(book_id, payload):
    return 'add_book_to_storage'


def change_book_in_storage(book_id):
    return 'change_book_in_storage'


@autocurry
def recursive_walk(func, coll):
    if is_seqcoll(coll):
        return walk(recursive_walk(func), coll)
    if is_mapping(coll):
        return walk_values(recursive_walk(func), coll)
    return func(coll)


def w(value):
    return value
