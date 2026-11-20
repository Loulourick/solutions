
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
                f"Количество прочитанных страниц должно быть от 0 до {self._pages}"
            )

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


if __name__ == "__main__":
    b = Book("1984", "Оруэлл", "123", 1949, 328)

    print(b.is_available)       # True
    print(b.last_read_pages)    # 0

    b.borrow()
    print(b.is_available)       # False

    try:
        b.borrow()
    except ValueError as e:
        print(f"ValueError: {e}")

    try:
        b.is_available = True
    except AttributeError as e:
        print(f"AttributeError: {e}")

    try:
        b.give_back(400)
    except ValueError as e:
        print(f"ValueError: {e}")

    print(b.is_available)       # False

    b.give_back(120)
    print(b.last_read_pages)    # 120

    print(b == Book("1984", "Оруэлл", "123", 1949, 328))  # True

    old = Book("Мы", "Замятин", "456", 1924, 224)
    print(sorted([b, old]))
