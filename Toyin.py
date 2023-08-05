class Book:
    def __init__(self, title, author, publication_year, isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn

class BookCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, publication_year, isbn):
        book = Book(title, author, publication_year, isbn)
        self.books.append(book)
        print("Book added successfully.")

    def search_by_title(self, title):
        results = []
        for book in self.books:
            if title.lower() in book.title.lower():
                results.append(book)
        return results

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("{:<30} {:<20} {:<10} {:<15}".format("Title", "Author", "Year", "ISBN"))
            print("=" * 75)
            for book in self.books:
                print("{:<30} {:<20} {:<10} {:<15}".format(book.title, book.author, book.publication_year, book.isbn))

class User:
    def __init__(self, name):
        self.name = name
        self.reserved_books = []

    def reserve_book(self, book):
        self.reserved_books.append(book)
        print("Book reserved successfully.")

def display_search_results(results):
    if not results:
        print("No books found.")
    else:
        print("Search Results:")
        for idx, book in enumerate(results, start=1):
            print(f"{idx}. {book.title} by {book.author}")

def main():
    catalog = BookCatalog()
    user = User("John")  # Example user

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search by Title")
        print("3. Display All Books")
        print("4. Reserve a Book")
        print("5. View Your Reserved Books")
        print("6. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            publication_year = input("Enter the publication year: ")
            isbn = input("Enter the ISBN: ")
            catalog.add_book(title, author, publication_year, isbn)
            print("Book added successfully.")
        elif choice == "2":
            title = input("Enter the title to search for: ")
            results = catalog.search_by_title(title)
            display_search_results(results)
        elif choice == "3":
            catalog.display_all_books()
        elif choice == "4":
            if not catalog.books:
                print("No books available to reserve.")
            else:
                display_search_results(catalog.books)
                book_idx = int(input("Enter the number of the book to reserve (or 0 to cancel): "))
                if 1 <= book_idx <= len(catalog.books):
                    selected_book = catalog.books[book_idx - 1]
                    user.reserve_book(selected_book)
                elif book_idx == 0:
                    print("Reservation canceled.")
                else:
                    print("Invalid book number.")
        elif choice == "5":
            if not user.reserved_books:
                print("You haven't reserved any books yet.")
            else:
                print("Your Reserved Books:")
                for idx, book in enumerate(user.reserved_books, start=1):
                    print(f"{idx}. {book.title} by {book.author}")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main(
