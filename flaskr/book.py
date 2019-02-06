import json

from flask import Blueprint, jsonify


class Book(object):

    def __init__(self, _id=0, name=""):
        self.id = _id
        self.name = name


bp = Blueprint('book', __name__)


@bp.route("/book/")
def index():
    """Show all books from database"""
    books = list()
    books.append(Book(1, "The Dark Tower I - The Gunslinger"))
    books.append(Book(2, "The Dark Tower II - The Drawing of the three"))
    return jsonify([b.__dict__ for b in books])
