from abc import ABC, abstractmethod


class AddBookInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int) -> None:
        pass


class RemoveBookInterface(ABC):
    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass


class ShowBooksInterface(ABC):
    @abstractmethod
    def show_books(self) -> None:
        pass


class LibraryStorageInterface(
    AddBookInterface, RemoveBookInterface, ShowBooksInterface
):
    pass


class Book:
    def __init__(self, title, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class Library:

    def __init__(self):
        self.books = []


class LibraryManager(LibraryStorageInterface):

    def __init__(self, library: Library):
        self.library = library

    def add_book(self, title, author: str, year: int) -> None:
        self.library.books.append(Book(title, author, year))

    def remove_book(self, title) -> None:
        for book in self.library.books:
            if book.title == title:
                self.library.books.remove(book)
                break

    def show_books(self) -> None:
        for book in self.library.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            manager.add_book(title, author, int(year))
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
