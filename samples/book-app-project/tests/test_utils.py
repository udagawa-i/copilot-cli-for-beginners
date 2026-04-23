import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils


class TestGetUserChoice:
    """Tests for get_user_choice."""

    def test_returns_choice_for_valid_numeric_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "2")

        assert utils.get_user_choice() == "2"

    def test_retries_when_input_is_empty(self, monkeypatch, capsys):
        inputs = iter(["   ", "3"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_user_choice() == "3"

        output = capsys.readouterr().out
        assert "Input cannot be empty." in output

    def test_retries_when_input_is_not_numeric(self, monkeypatch, capsys):
        inputs = iter(["abc", "4"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_user_choice() == "4"

        output = capsys.readouterr().out
        assert "Invalid input. Enter numbers only." in output

    def test_retries_when_choice_is_out_of_range(self, monkeypatch, capsys):
        inputs = iter(["9", "5"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_user_choice() == "5"

        output = capsys.readouterr().out
        assert "Invalid choice. Enter a number between 1 and 5." in output


class TestGetBookDetails:
    """Tests for get_book_details."""

    def test_returns_values_for_valid_input(self, monkeypatch):
        inputs = iter(["Dune", "Frank Herbert", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_book_details() == ("Dune", "Frank Herbert", 1965)

    def test_extremely_long_book_title(self, monkeypatch):
        long_title = "A" * 10000
        long_author = "B" * 8000
        inputs = iter([long_title, long_author, "2024"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert utils.get_book_details() == (long_title, long_author, 2024)

    def test_retries_when_title_is_empty(self, monkeypatch, capsys):
        inputs = iter(["   ", "Dune", "Frank Herbert", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_book_details() == ("Dune", "Frank Herbert", 1965)

        output = capsys.readouterr().out
        assert "Book title cannot be empty." in output

    def test_retries_when_author_is_empty(self, monkeypatch, capsys):
        inputs = iter(["Dune", "   ", "Frank Herbert", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_book_details() == ("Dune", "Frank Herbert", 1965)

        output = capsys.readouterr().out
        assert "Author cannot be empty." in output

    def test_retries_when_year_is_empty(self, monkeypatch, capsys):
        inputs = iter(["Dune", "Frank Herbert", "   ", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_book_details() == ("Dune", "Frank Herbert", 1965)

        output = capsys.readouterr().out
        assert "Publication year cannot be empty. Enter numbers only." in output

    def test_retries_when_year_is_not_numeric(self, monkeypatch, capsys):
        inputs = iter(["Dune", "Frank Herbert", "year", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_book_details() == ("Dune", "Frank Herbert", 1965)

        output = capsys.readouterr().out
        assert "Invalid year. Enter a positive number only." in output

    def test_retries_when_year_is_negative(self, monkeypatch, capsys):
        # Simulate negative and zero year input, then valid input
        inputs = iter(["Dune", "Frank Herbert", "-2020", "0", "1965"])
        def fake_input(prompt):
            value = next(inputs)
            # Simulate negative/zero year as non-numeric for .isdigit() check
            if prompt.startswith("Enter publication year") and (value.startswith("-") or value == "0"):
                return value
            return value
        monkeypatch.setattr("builtins.input", fake_input)

        assert utils.get_book_details() == ("Dune", "Frank Herbert", 1965)

        output = capsys.readouterr().out
        # Should treat negative and zero as invalid (not .isdigit()), so error message should appear
        assert "Invalid year. Enter a positive number only." in output

    def test_author_with_special_characters(self, monkeypatch):
        # Author names with special characters
        inputs = iter(["Dune", "François d'Arcy!@#", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert utils.get_book_details() == ("Dune", "François d'Arcy!@#", 1965)

    def test_retries_all_empty_fields(self, monkeypatch, capsys):
        # All fields empty first, then valid inputs
        inputs = iter(["", "Dune", "", "Frank Herbert", "", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_book_details() == ("Dune", "Frank Herbert", 1965)

        output = capsys.readouterr().out
        assert "Book title cannot be empty." in output
        assert "Author cannot be empty." in output
        assert "Publication year cannot be empty. Enter numbers only." in output


class TestGetSearchYearRange:
    """Tests for get_search_year_range."""

    def test_returns_none_for_blank_inputs(self, monkeypatch):
        inputs = iter(["", ""])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_search_year_range() == (None, None)

    def test_returns_year_range_for_valid_numeric_input(self, monkeypatch):
        inputs = iter(["1950", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_search_year_range() == (1950, 1965)

    def test_retries_when_start_year_is_not_numeric(self, monkeypatch, capsys):
        inputs = iter(["nineteen", "1965", "1950", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_search_year_range() == (1950, 1965)

        output = capsys.readouterr().out
        assert "Invalid start year. Enter numbers only or leave blank." in output

    def test_retries_when_end_year_is_not_numeric(self, monkeypatch, capsys):
        inputs = iter(["1950", "sixty-five", "1950", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_search_year_range() == (1950, 1965)

        output = capsys.readouterr().out
        assert "Invalid end year. Enter numbers only or leave blank." in output

    def test_retries_when_start_year_is_greater_than_end_year(self, monkeypatch, capsys):
        inputs = iter(["2000", "1990", "1990", "2000"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert utils.get_search_year_range() == (1990, 2000)

        output = capsys.readouterr().out
        assert "Start year cannot be greater than end year." in output


def test_sum_one_to_ten():
    assert utils.sum_one_to_ten() == 55


def test_cal10():
    assert utils.cal10() == 55
