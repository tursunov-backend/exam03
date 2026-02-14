from book import Book

book1 = Book(
    id=1,
    title="Clean Code",
    author="Robert Martin",
    pages=464,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)

book2 = Book(
    id=2,
    title="The Pragmatic Programmer",
    author="Andrew Hunt",
    pages=352,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)

book3 = Book(
    id=3,
    title="Design Patterns",
    author="Erich Gamma",
    pages=395,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)

book4 = Book(
    id=4,
    title="Refactoring",
    author="Martin Fowler",
    pages=448,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)

book5 = Book(
    id=5,
    title="Python Crash Course",
    author="Eric Matthes",
    pages=544,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)

book6 = Book(
    id=6,
    title="Fluent Python",
    author="Luciano Ramalho",
    pages=792,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)

book7 = Book(
    id=7,
    title="Effective Python",
    author="Brett Slatkin",
    pages=480,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)

book8 = Book(
    id=8,
    title="Introduction to Algorithms",
    author="Thomas H. Cormen",
    pages=1312,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)

book9 = Book(
    id=9,
    title="You Don't Know JS",
    author="Kyle Simpson",
    pages=278,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)

book10 = Book(
    id=10,
    title="Linux Command Line",
    author="William Shotts",
    pages=392,
    is_borrowed=False,
    borrower=None,
    borrow_history=[],
    archived=False,
)


books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]

print(book9)
print(repr(book8))
print(book1 == book10)
print(len(book1))

book4.borrow("Ali")
print(book4.info())

book4.return_book()
book3.archive()

print(bool(book4))
