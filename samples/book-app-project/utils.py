def get_user_choice() -> str:
    """Get user choice with validation."""
    while True:
        choice = input("Choose an option (1-5): ").strip()
        if not choice:
            print("Input cannot be empty.")
            continue
        if not choice.isdigit():
            print("Invalid input. Enter numbers only.")
            continue
        choice_num = int(choice)
        if choice_num < 1 or choice_num > 5:
            print("Invalid choice. Enter a number between 1 and 5.")
            continue
        return choice


def get_book_details():
    """Get book details from user input with validation."""
    while True:
        title = input("Enter book title: ").strip()
        if not title:
            print("Book title cannot be empty.")
            continue
        break

    while True:
        author = input("Enter author: ").strip()
        if not author:
            print("Author cannot be empty.")
            continue
        break

    while True:
        year_input = input("Enter publication year: ").strip()
        if not year_input:
            print("Publication year cannot be empty. Enter numbers only.")
            continue
        if not year_input.isdigit():
            print("Invalid year. Enter a positive number only.")
            continue
        year = int(year_input)
        if year <= 0:
            print("Invalid year. Enter a positive number only.")
            continue
        break

    return title, author, year


def get_search_year_range():
    """Get year range for search with validation."""
    while True:
        start_year_input = input("Start year (or press Enter for none): ").strip()
        end_year_input = input("End year (or press Enter for none): ").strip()

        if not start_year_input and not end_year_input:
            return None, None

        start_year = None
        end_year = None

        if start_year_input:
            if not start_year_input.isdigit():
                print("Invalid start year. Enter numbers only or leave blank.")
                continue
            start_year = int(start_year_input)

        if end_year_input:
            if not end_year_input.isdigit():
                print("Invalid end year. Enter numbers only or leave blank.")
                continue
            end_year = int(end_year_input)

        if start_year is not None and end_year is not None:
            if start_year > end_year:
                print("Start year cannot be greater than end year.")
                continue

        return start_year, end_year


def sum_one_to_ten():
    """Sum numbers from 1 to 10."""
    return sum(range(1, 11))


def cal10():
    """Calculate sum from 1 to 10."""
    return sum(range(1, 11))
