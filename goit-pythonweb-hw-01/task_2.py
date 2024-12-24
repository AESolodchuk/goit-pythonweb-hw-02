import logging
from abc import ABC, abstractmethod


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


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
    def __init__(self, title: str, author: str, year: int):
        self.title: str = title
        self.author: str = author
        self.year: int = year


class Library:

    def __init__(self):
        self.books: list = []


class LibraryManager(LibraryStorageInterface):

    def __init__(self, library: Library):
        self.library: Library = library

    def add_book(self, title, author, year) -> None:
        self.library.books.append(Book(title, author, year))
        logging.info(f"Title: {title}, Author: {author}, Year: {year} has been added")

    def remove_book(self, title) -> None:
        for book in self.library.books:
            if book.title == title:
                self.library.books.remove(book)
                logging.info(
                    f"Title: {book.title}, Author: {book.author}, Year: {book.year} has been removed"
                )
                break

    def show_books(self) -> None:
        for book in self.library.books:
            logging.info(
                f"Title: {book.title}, Author: {book.author}, Year: {book.year}"
            )


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
            logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
