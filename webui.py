#import utf8reader
import json
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
    add_book_to_storage,
    change_book_in_storage,
    get_authors_all,
    get_author_details,
)
@get('/')
@get('/api/books')
def books():
    return {'response': get_books_all()}


@get('/api/books/<book_id:int>')
def book(book_id):
    return {'response': get_book_details(book_id)}


@post('/api/books/add')
def book_add():
    title = request.forms.get('Title')
    author = request.forms.get('Author')
    description = request.forms.get('Description')
    priority = request.forms.get('Priority')
    request_payload = [title,author,description,priority]
    #status = add_book_to_storage(request_payload)
    status = 1
    print(request_payload)
    return {'response': request_payload} if status else {'response':'failed to add booking'}


@get('/api/authors')
def authors():
    return {'response': get_authors_all()}


@get('/api/authors/<author_id:int>')
def book(author_id):
    return {'response': get_author_details(author_id)}

# @post('/follow/error/<error_id:int>')
# def follow_error(error_id):
#     request_payload = request.json
#     notification_sent = send_slack_notification(error_id, request_payload['notes'])
#     return {
#         'response': notification_sent
#     } if notification_sent else HTTPError(400, 'Bad request')


# @post('api/book/<book_id:int>')
# def add_book(book_id):
#     request_payload = request.json
#     book_added = add_book_to_storage(book_id, request_payload['new_book'])
#     return {'response': book_added} if book_added else HTTPError(400, 'Bad request')
#
#
# @put('api/book/<book_id:int>')
# def change_book(book_id):
#     request_payload = request.json
#     book_changed = change_book_in_storage(book_id, request_payload['changed_book'])
#     return {'response': book_changed} if book_changed else HTTPError(400, 'Bad request')


application = default_app()
