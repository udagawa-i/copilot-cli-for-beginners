import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import books
from books import BookCollection


@pytest.fixture(autouse=True)
def use_temp_data_file(tmp_path, monkeypatch):
    """Use a temporary data file for each test."""
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]")
    monkeypatch.setattr(books, "DATA_FILE", str(temp_file))


def test_add_book():
    collection = BookCollection()
    initial_count = len(collection.books)
    collection.add_book("1984", "George Orwell", 1949)
    assert len(collection.books) == initial_count + 1
    book = collection.find_book_by_title("1984")
    assert book is not None
    assert book.author == "George Orwell"
    assert book.year == 1949
    assert book.read is False

def test_mark_book_as_read():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    result = collection.mark_as_read("Dune")
    assert result is True
    book = collection.find_book_by_title("Dune")
    assert book.read is True

def test_mark_book_as_read_invalid():
    collection = BookCollection()
    result = collection.mark_as_read("Nonexistent Book")
    assert result is False

def test_remove_book():
    collection = BookCollection()
    collection.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    result = collection.remove_book("The Hobbit")
    assert result is True
    book = collection.find_book_by_title("The Hobbit")
    assert book is None

def test_remove_book_invalid():
    collection = BookCollection()
    result = collection.remove_book("Nonexistent Book")
    assert result is False

def test_get_unread_books_empty_collection():
    """Empty collection returns empty list of unread books."""
    collection = BookCollection()
    unread = collection.get_unread_books()
    assert unread == []

def test_get_unread_books_all_unread():
    """All unread books are returned when all books are unread."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Dune", "Frank Herbert", 1965)
    collection.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    
    unread = collection.get_unread_books()
    assert len(unread) == 3
    assert all(not book.read for book in unread)

def test_get_unread_books_mixed_status():
    """Only unread books are returned when collection has mixed read status."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Dune", "Frank Herbert", 1965)
    collection.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    
    collection.mark_as_read("1984")
    collection.mark_as_read("The Hobbit")
    
    unread = collection.get_unread_books()
    assert len(unread) == 1
    assert unread[0].title == "Dune"
    assert all(not book.read for book in unread)

def test_get_unread_books_all_read():
    """Empty list is returned when all books are marked as read."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Dune", "Frank Herbert", 1965)
    
    collection.mark_as_read("1984")
    collection.mark_as_read("Dune")
    
    unread = collection.get_unread_books()
    assert unread == []

def test_get_unread_books_returns_independent_list():
    """get_unread_books returns independent list, not reference to internal list."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    
    unread = collection.get_unread_books()
    unread.clear()
    
    assert len(collection.books) == 1


def test_find_by_author_exact_match():
    """Exact match for author name returns correct books."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Animal Farm", "George Orwell", 1945)
    collection.add_book("Dune", "Frank Herbert", 1965)
    
    result = collection.find_by_author("George Orwell")
    assert len(result) == 2
    assert result[0].title == "1984"
    assert result[1].title == "Animal Farm"


def test_find_by_author_partial_match_first_name():
    """Partial match with first name returns correct books."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Animal Farm", "George Orwell", 1945)
    collection.add_book("Dune", "Frank Herbert", 1965)
    
    result = collection.find_by_author("George")
    assert len(result) == 2


def test_find_by_author_partial_match_last_name():
    """Partial match with last name returns correct books."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Animal Farm", "George Orwell", 1945)
    collection.add_book("Dune", "Frank Herbert", 1965)
    
    result = collection.find_by_author("Orwell")
    assert len(result) == 2


def test_find_by_author_case_insensitive():
    """Author search is case insensitive."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    
    result = collection.find_by_author("GEORGE ORWELL")
    assert len(result) == 1
    assert result[0].title == "1984"
    
    result = collection.find_by_author("george orwell")
    assert len(result) == 1


def test_find_by_author_empty_string():
    """Empty author string returns empty list."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    
    result = collection.find_by_author("")
    assert result == []


def test_find_by_author_whitespace_only():
    """Whitespace-only author string returns empty list."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    
    result = collection.find_by_author("   ")
    assert result == []


def test_find_by_author_no_match():
    """Non-existent author returns empty list."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    
    result = collection.find_by_author("Unknown Author")
    assert result == []


def test_search_books_author_partial_match():
    """search_books with partial author match returns correct books."""
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Animal Farm", "George Orwell", 1945)
    collection.add_book("Dune", "Frank Herbert", 1965)
    
    result = collection.search_books(author="George")
    assert len(result) == 2
    
    result = collection.search_books(author="Herbert")
    assert len(result) == 1

