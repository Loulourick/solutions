class Book:
    def __init__(self, title, author, isbn, year, pages):
        if pages <= 0: raise ValueError("Количество страниц должно быть положительным")
        self._title = title
        self._author = author
        self._isbn = isbn
        self._year = year
        self._pages = pages
        self._is_available = True
        self._last_read_pages = 0

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def year(self):
        return self._year

    @property
    def pages(self):
        return self._pages

    @property
    def is_available(self):
        return self._is_available

    @property
    def last_read_pages(self):
        return self._last_read_pages

    def borrow(self):
        if not self._is_available:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def give_back(self, pages_read):
        if self._is_available:
            raise ValueError("Книга уже на полке")

        if not (0 <= pages_read <= self._pages):
            raise ValueError(
                f"Количество прочитанных страниц должно быть от 0 до {self._pages}")

        self._last_read_pages = pages_read
        self._is_available = True

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._isbn == other._isbn

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._year < other._year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.year}, {self.pages})"


class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.pages_read = 0


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def find_by_isbn(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def find_by_author(self, author):
        return [book for book in self._books if book.author == author]

    def lend(self, isbn, reader):
        book = self.find_by_isbn(isbn)
        if book is None:
            raise KeyError(f"Книги с ISBN {isbn} нет в фонде")
        book.borrow()
        reader.books.append(book)

    def take_back(self, isbn, reader, pages_read):
        target_book = None
        for book in reader.books:
            if book.isbn == isbn:
                target_book = book
                break

        if target_book is None:
            raise ValueError("У читателя нет этой книги")
        target_book.give_back(pages_read)
        reader.books.remove(target_book)
        reader.pages_read += pages_read

    def available(self):
        return [book for book in self._books if book.is_available]

    def unfinished(self):
        return [book for book in self._books if 0 < book.last_read_pages < book.pages]

    def __len__(self):
        return len(self._books)

if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("1984", "Оруэлл", "123", 1949, 328))
    lib.add_book(Book("Скотный двор", "Оруэлл", "124", 1945, 112))
    alice = Reader("Алиса")

    lib.lend("123", alice)
    print(alice.books)  # [Book('1984', 'Оруэлл', '123', 1949, 328)]
    print(lib.find_by_isbn("123").is_available)  # False
    print(len(lib.available()))  # 1

    try:
        lib.lend("123", Reader("Боб"))  # ValueError
    except ValueError as e:
        print(f"ValueError: {e}")

    try:
        lib.take_back("123", alice, 500)  # ValueError: столько страниц в книге нет
    except ValueError as e:
        print(f"ValueError: {e}")

    print(alice.books)  # Книга осталась: [Book('1984', 'Оруэлл', '123', 1949, 328)]
    lib.take_back("123", alice, 100)
    print(alice.books)  # []
    print(alice.pages_read)  # 100
    print(lib.unfinished())  # [Book('1984', 'Оруэлл', '123', 1949, 328)]

    lib.lend("124", alice)
    lib.take_back("124", alice, 112)  # дочитала до конца
    print(alice.pages_read)  # 212
    print(len(lib.unfinished()))  # 1
