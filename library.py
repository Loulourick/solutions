class Book:
    def __init__(self, title, author, isbn, year, pages):
        if pages <= 0: raise ValueError
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages1 = pages
        self.is_available = True
        self.last_read_pages = 0

    @property
    def pages(self): return self.pages1

    @property
    def is_available(self): return self.is_available

    @property
    def last_read_pages(self): return self.last_read_pages

    def borrow(self):
        if not self.is_available: raise ValueError
        self.is_available = False

    def give_back(self, pages_read):
        if self.is_available and (not(0 <= pages_read <= self.pages1)): raise ValueError
        self.is_available = True
        self.last_read_pages = pages_read

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __lt__(self, other):
        return self.year < other.year
    def __repr__(self): return f"Book('{self.title}', '{self.author}', {self.isbn}, '{self.year}', '{self.pages}')"

    class Reader:
        def __init__(self, name):
            self.name = name
            self.books = []
            self.pages_read = 0
        def __repr__(self): return f"Reader('{self.name}')"

    class Library:
        def __init__(self):
            self._books = []

        def add_book(self, book):
            self.books1.append(book)

        def find_by_isbn(self, isbn):
            for book in self.books1:
                if book.isbn == isbn: return book

        def find_by_author(self,author):
            return [book for book in self.books if book.author == author]

        def lend(self, isbn, reader):
            book = self.find_by_isbn(isbn)
            if book is None:
                raise KeyError
            book.borrow()
            reader.books.append(book)

        def take_back(isbn, reader, pages_read):
            if book is None or book not in reader.books: raise ValueError
            book.give_back(pages_read)
            reader.books.remove(book)
            reader.pages_read += pages_read
        def available(self):
            return [book for book in self.books if book.is_available]
        def unfinished(self):
            res = []
            for book in self.books:
                if 0 < book.last_read_pages < book.pages:
                    res.append(book)
            return res
        def __len__(self):
            return len(self._books)

lib = Library()
lib.add_book(Book("1984", "Оруэлл", "123", 1949, 328))
lib.add_book(Book("Скотный двор", "Оруэлл", "124", 1945, 112))
alice = Reader("Алиса")

lib.lend("123", alice)
alice.books                              # [Book('1984', 'Оруэлл', '123', 1949, 328)]
lib.find_by_isbn("123").is_available     # False
len(lib.available())                     # 1
lib.lend("123", Reader("Боб"))           # ValueError
lib.take_back("123", alice, 500)         # ValueError: столько страниц в книге нет
alice.books                              # [Book('1984', 'Оруэлл', '123', 1949, 328)]
lib.take_back("123", alice, 100)
alice.books                              # []
alice.pages_read                         # 100
lib.unfinished()                         # [Book('1984', 'Оруэлл', '123', 1949, 328)]

lib.lend("124", alice)
lib.take_back("124", alice, 112)         # дочитала до конца
alice.pages_read                         # 212
len(lib.unfinished())                    # 1

