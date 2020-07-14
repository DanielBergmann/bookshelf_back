from bottle import (
    HTTPError,
    get,
    default_app,
    post,
    put,
    request,
    route,
    static_file
)

from shelf_back.adapter import (
    get_books_all,
    get_book_details,
)

@get('/api/books')
def books():
    return {'response': get_books_all()}

@get('/api/book/<bookId:int>')
def book(bookId):
    return {'response': get_book_details(bookId)}

application = default_app()
