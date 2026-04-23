import pytest
from samples.book_app_buggy.books_buggy import BookCollection
import datetime

def test_add_book_valid():
    bc = BookCollection()
    book = bc.add_book("Test Title", "Test Author", 2020)
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.year == 2020

def test_add_book_negative_year():
    bc = BookCollection()
    book = bc.add_book("Negative Year", "Author", -100)
    assert book.year == -100  # バリデーションが無いのでそのまま登録される

def test_add_book_future_year():
    bc = BookCollection()
    future_year = datetime.datetime.now().year + 10
    book = bc.add_book("Future Book", "Author", future_year)
    assert book.year == future_year  # バリデーションが無いのでそのまま登録される
