import jsons

from flask import Blueprint, jsonify, request, make_response


class Book(object):

    def __init__(self, _id=0, name=""):
        self.id = _id
        self.name = name


bp = Blueprint('book', __name__, url_prefix='/books')
books = list()
books.append(Book(1, "The Dark Tower I - The Gunslinger"))
books.append(Book(2, "The Dark Tower II - The Drawing of the three"))


@bp.route("", methods=['GET'])
def list_books():
    """Show all books from database"""
    return jsonify([b.__dict__ for b in books])


@bp.route("", methods=['POST'])
def save_book():
    print(request.json)
    new_book = jsons.load(request.json, Book)
    print(new_book)
    books.append(new_book)
    return jsonify({'book': new_book.__dict__}), 201

