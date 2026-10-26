class Book:
    def __init__(self, title, author, isbn, year, pages):
        if pages <= 0: raise ValueError
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self._pages = pages
        self._is_available = True
        self._last_read_pages = 0

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
        if self._is_available or not (0 <= pages_read <= self.pages):
            raise ValueError("Некорректный возврат книги")

        self._is_available = True
        self._last_read_pages = pages_read

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __lt__(self, other):
        return self.year < other.year
    def __repr__(self): return f"Book('{self.title}', '{self.author}', {self.isbn}, '{self.year}', '{self.pages}')"


b = Book("1984", "Оруэлл", "123", 1949, 328)
b.is_available  # True
b.last_read_pages  # 0
b.borrow()
b.is_available  # False
b.borrow()  # ValueError: книга уже выдана
b.is_available = True  # AttributeError
b.give_back(400)  # ValueError: в книге всего 328 страниц
b.is_available  # False - книга так и осталась у читателя
b.give_back(120)
b.last_read_pages  # 120
b == Book("1984", "Оруэлл", "123", 1949, 328)  # True

old = Book("Мы", "Замятин", "456", 1924, 224)
sorted([b, old])  # [Book('Мы', 'Замятин', '456', 1924, 224), Book('1984', 'Оруэлл', '123', 1949, 328)]


