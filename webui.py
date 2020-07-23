# import utf8reader
import json
from bottle import HTTPError, get, default_app, post, put, request, route, static_file

from shelf_back.adapter import (
    get_books_all,
    get_book_details,
    add_book_to_storage,
    change_book_in_storage,
    change_book_status,
    get_authors_all,
    get_author_details,
    delete_book,
)


@get("/")
@get("/api/books")
def books():
    return {"response": get_books_all()}


@get("/api/books/<book_id:int>")
def book(book_id):
    return {"response": get_book_details(book_id)}


@post("/api/books/add")
def book_add():
    # {'author': 'Ernest Hemingway', 'title': 'Men Without Women', 'description': '12345', 'priority': '1234'}
    request_payload = json.loads(request.body.getvalue().decode("utf-8"))
    print(request_payload['author'])
    status = add_book_to_storage(request_payload)
    #status = 1
    return (
        #"<a href='http://127.0.0.1:3000/books'><p>go back</p></a></br>"+
        "{response: "
        + json.dumps(request_payload)
        + "}"
        if status
        else {"response": "failed to add booking"}
    )


@post("/api/books/change")
def book_change():
    test = json.loads(request.body.getvalue().decode("utf-8"))
    change = change_book_in_storage(test)
    return {"response": test} if change else "something went wrong"


@post("/api/books/<id:int>/change")
def book_change(id):
    test = json.loads(request.body.getvalue().decode("utf-8"))
    change = change_book_status(test)
    return {"response": test} if change else "something went wrong"


@post("/api/books/delete")
def book_change():
    test = json.loads(request.body.getvalue().decode("utf-8"))
    change = delete_book(test)
    return {"response": test} if change else "something went wrong"


@get("/api/authors")
def authors():
    return {"response": get_authors_all()}


@get("/api/authors/<author_id:int>")
def book(author_id):
    return {"response": get_author_details(author_id)}


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
