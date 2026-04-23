import sys
from books import BookCollection
from utils import get_book_details, get_search_year_range


# Global collection instance
collection = BookCollection()


def show_books(books):
    """Display books in a user-friendly format."""
    if not books:
        print("No books found.")
        return

    print("\nYour Book Collection:\n")

    for index, book in enumerate(books, start=1):
        status = "✓" if book.read else " "
        print(f"{index}. [{status}] {book.title} by {book.author} ({book.year})")

    print()


def handle_list():
    books = collection.list_books()
    show_books(books)


def handle_unread():
    books = collection.get_unread_books()
    show_books(books)


def handle_add():
    print("\nAdd a New Book\n")

    title, author, year = get_book_details()

    try:
        collection.add_book(title, author, year)
        print("\nBook added successfully.\n")
    except ValueError as e:
        print(f"\nError: {e}\n")


def handle_remove():
    print("\nRemove a Book\n")

    raw_title = input(
        "Enter the title of the book to remove (press Enter for an empty title): "
    )

    if raw_title == "":
        title = ""
    elif not raw_title.strip():
        print("\nEnter a title, or press Enter to remove a book with an empty title.\n")
        return
    else:
        title = raw_title.strip()

    if collection.remove_book(title):
        if title:
            print("\nBook removed.\n")
        else:
            print("\nBook with an empty title removed.\n")
    else:
        print("\nBook not found.\n")


def handle_find():
    print("\nFind Books by Author\n")

    author = input("Author name: ").strip()
    books = collection.find_by_author(author)

    show_books(books)


def handle_search():
    print("\nSearch Books\n")

    title = input("Title contains: ").strip()
    author = input("Author contains: ").strip()
    start_year, end_year = get_search_year_range()
    books = collection.search_books(
        title=title,
        author=author,
        start_year=start_year,
        end_year=end_year,
    )

    show_books(books)


def handle_mark_as_read():
    print("\nMark a Book as Read\n")

    title = input("Enter the title of the book to mark as read: ").strip()

    if collection.mark_as_read(title):
        print("\nBook marked as read.\n")
    else:
        print("\nBook not found.\n")


def show_help():
    print("""
Book Collection Helper

Commands:
  list         - Show all books
  list-unread  - Show unread books
  add          - Add a new book
  search       - Search books by title, author, and/or year range
  mark         - Mark a book as read by title
  remove       - Remove a book by title
  find         - Find books by author
  help         - Show this help message
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "list":
        handle_list()
    elif command == "list-unread":
        handle_unread()
    elif command == "add":
        handle_add()
    elif command == "search":
        handle_search()
    elif command == "mark":
        handle_mark_as_read()
    elif command == "remove":
        handle_remove()
    elif command == "find":
        handle_find()
    elif command == "help":
        show_help()
    else:
        print("Unknown command.\n")
        show_help()


if __name__ == "__main__":
    main()
