from datetime import datetime


class Book:
    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        pages: int,
        is_borrowed: bool,
        borrower: str | None,
        borrow_history: list[tuple[str, datetime]],
        archived: bool,
    ):
        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = is_borrowed
        self.borrower = borrower
        self.borrow_history = borrow_history
        self.archived = archived

    def borrow(self, user: str) -> None:
        if self.archived:
            raise RuntimeWarning("Kitob archived holatda")

        if self.is_borrowed:
            raise RuntimeError("Kitob allaqachon olingan")

        self.is_borrowed = True
        self.borrower = user
        self.borrow_history.append((user, datetime.now()))

    def return_book(self) -> None:
        if not self.is_borrowed:
            raise RuntimeError("Kitob olinmagan")

        self.borrower = None
        self.is_borrowed = False

    def archive(self) -> None:
        if self.is_borrowed:
            raise RuntimeError("Kitob hozir kimgadir olingan")

        self.archived = True

    def info(self) -> dict:
        if self.archived:
            status = "archived"
        elif self.is_borrowed:
            status = "borrowed"
        else:
            status = "available"

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "status": status,
            "borrower": self.borrower,
            "times_borrowed": len(self.borrow_history),
        }

    def __str__(self) -> str:
        return f"<Book {self.title}>"

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title='{self.title}', borrowed={self.is_borrowed})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.id == other.id

    def __len__(self) -> int:
        return self.pages

    def __bool__(self) -> bool:
        return not self.archived
