import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import books
from books import BookCollection
import book_app


@pytest.fixture(autouse=True)
def use_temp_collection(tmp_path, monkeypatch):
    """Use a temporary collection file and reset the CLI collection per test."""
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]")
    monkeypatch.setattr(books, "DATA_FILE", str(temp_file))
    book_app.collection = BookCollection()
    return book_app.collection


class TestHandleMarkAsRead:
    """Tests for handle_mark_as_read."""

    def test_marks_existing_book(self, monkeypatch, capsys, use_temp_collection):
        use_temp_collection.add_book("Dune", "Frank Herbert", 1965)
        monkeypatch.setattr("builtins.input", lambda _: "Dune")

        book_app.handle_mark_as_read()

        output = capsys.readouterr().out
        assert "Book marked as read." in output
        assert use_temp_collection.find_book_by_title("Dune").read is True

    def test_reports_missing_book(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "Missing Book")

        book_app.handle_mark_as_read()

        output = capsys.readouterr().out
        assert "Book not found." in output


class TestHandleSearch:
    """Tests for handle_search."""

    def test_search_finds_books_by_title(self, monkeypatch, capsys, use_temp_collection):
        use_temp_collection.add_book("Dune", "Frank Herbert", 1965)
        use_temp_collection.add_book("Foundation", "Isaac Asimov", 1951)
        inputs = iter(["dune", "", "", ""])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_search()

        output = capsys.readouterr().out
        assert "[ ] Dune by Frank Herbert (1965)" in output
        assert "Foundation" not in output

    def test_search_finds_books_by_author(self, monkeypatch, capsys, use_temp_collection):
        use_temp_collection.add_book("Dune", "Frank Herbert", 1965)
        use_temp_collection.add_book("Foundation", "Isaac Asimov", 1951)
        inputs = iter(["", "asim", "", ""])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_search()

        output = capsys.readouterr().out
        assert "[ ] Foundation by Isaac Asimov (1951)" in output
        assert "Dune by Frank Herbert" not in output

    def test_search_shows_no_books_for_blank_inputs(self, monkeypatch, capsys, use_temp_collection):
        use_temp_collection.add_book("Dune", "Frank Herbert", 1965)
        inputs = iter(["   ", "   ", "", ""])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_search()

        output = capsys.readouterr().out
        assert "No books found." in output

    def test_search_finds_books_by_year_range(self, monkeypatch, capsys, use_temp_collection):
        use_temp_collection.add_book("Foundation", "Isaac Asimov", 1951)
        use_temp_collection.add_book("Dune", "Frank Herbert", 1965)
        use_temp_collection.add_book("Neuromancer", "William Gibson", 1984)
        inputs = iter(["", "", "1951", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_search()

        output = capsys.readouterr().out
        assert "[ ] Foundation by Isaac Asimov (1951)" in output
        assert "[ ] Dune by Frank Herbert (1965)" in output
        assert "Neuromancer" not in output

    def test_search_retries_when_year_range_is_invalid(self, monkeypatch, capsys, use_temp_collection):
        use_temp_collection.add_book("Foundation", "Isaac Asimov", 1951)
        use_temp_collection.add_book("Dune", "Frank Herbert", 1965)
        inputs = iter(["", "", "2000", "1990", "1950", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_search()

        output = capsys.readouterr().out
        assert "Start year cannot be greater than end year." in output
        assert "[ ] Foundation by Isaac Asimov (1951)" in output
        assert "[ ] Dune by Frank Herbert (1965)" in output


class TestHandleAdd:
    """Tests for handle_add."""

    def test_adds_book_with_valid_input(self, monkeypatch, capsys, use_temp_collection):
        inputs = iter(["Dune", "Frank Herbert", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_add()

        output = capsys.readouterr().out
        assert "Book added successfully." in output
        added_book = use_temp_collection.find_book_by_title("Dune")
        assert added_book is not None
        assert added_book.author == "Frank Herbert"
        assert added_book.year == 1965

    def test_retries_when_year_is_empty(self, monkeypatch, capsys, use_temp_collection):
        inputs = iter(["Dune", "Frank Herbert", "   ", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_add()

        output = capsys.readouterr().out
        assert "Publication year cannot be empty. Enter numbers only." in output
        assert use_temp_collection.find_book_by_title("Dune").year == 1965

    def test_retries_when_year_is_not_numeric(self, monkeypatch, capsys, use_temp_collection):
        inputs = iter(["Dune", "Frank Herbert", "nineteen sixty-five", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_add()

        output = capsys.readouterr().out
        assert "Invalid year. Enter a positive number only." in output
        assert use_temp_collection.find_book_by_title("Dune").year == 1965

    def test_retries_when_title_is_empty(self, monkeypatch, capsys, use_temp_collection):
        inputs = iter(["   ", "Dune", "Frank Herbert", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_add()

        output = capsys.readouterr().out
        assert "Book title cannot be empty." in output
        assert use_temp_collection.find_book_by_title("Dune").year == 1965

    def test_retries_when_author_is_empty(self, monkeypatch, capsys, use_temp_collection):
        inputs = iter(["Dune", "   ", "Frank Herbert", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.handle_add()

        output = capsys.readouterr().out
        assert "Author cannot be empty." in output
        assert use_temp_collection.find_book_by_title("Dune").author == "Frank Herbert"


class TestHandleRemove:
    """Tests for handle_remove."""

    def test_removes_book_with_empty_title(self, monkeypatch, capsys, use_temp_collection):
        use_temp_collection.add_book("", "Unknown", 2000)
        monkeypatch.setattr("builtins.input", lambda _: "")

        book_app.handle_remove()

        output = capsys.readouterr().out
        assert "Book with an empty title removed." in output
        assert use_temp_collection.find_book_by_title("") is None

    def test_does_not_treat_whitespace_only_input_as_empty_title(
        self, monkeypatch, capsys, use_temp_collection
    ):
        use_temp_collection.add_book("", "Unknown", 2000)
        monkeypatch.setattr("builtins.input", lambda _: "   ")

        book_app.handle_remove()

        output = capsys.readouterr().out
        assert "Enter a title, or press Enter to remove a book with an empty title." in output
        assert use_temp_collection.find_book_by_title("") is not None


class TestMain:
    """Tests for main command dispatch."""

    def test_help_includes_mark_command(self, capsys):
        book_app.show_help()

        output = capsys.readouterr().out
        assert "search   - Search books by title, author, and/or year range" in output
        assert "mark     - Mark a book as read by title" in output
        assert "既読にする" not in output

    def test_mark_command_works(self, monkeypatch, capsys):
        inputs = iter(["Dune"])
        monkeypatch.setattr(sys, "argv", ["book_app.py", "mark"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.collection.add_book("Dune", "Frank Herbert", 1965)

        book_app.main()
        book_app.handle_list()

        output = capsys.readouterr().out
        assert "Book marked as read." in output
        assert "[✓] Dune by Frank Herbert (1965)" in output

    def test_japanese_mark_command_fails(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, "argv", ["book_app.py", "既読にする"])

        book_app.main()

        output = capsys.readouterr().out
        assert "Unknown command." in output

    def test_search_command_flow_displays_matches(self, monkeypatch, capsys):
        inputs = iter(["", "asim", "", ""])
        monkeypatch.setattr(sys, "argv", ["book_app.py", "search"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        book_app.collection.add_book("Dune", "Frank Herbert", 1965)
        book_app.collection.add_book("Foundation", "Isaac Asimov", 1951)

        book_app.main()

        output = capsys.readouterr().out
        assert "[ ] Foundation by Isaac Asimov (1951)" in output
        assert "Dune by Frank Herbert" not in output
