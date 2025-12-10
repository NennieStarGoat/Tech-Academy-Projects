class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title              # public
        self._author = author           # protected
        self.__pages = pages            # private
        self._current = 0               # protected

    def read(self, pages: int) -> None:
        if pages <= 0:
            raise ValueError("Pages must be positive.")
        self._current = min(self._current + pages, self.__pages)            # uses private __pages

    def progress(self) -> float:
        if self.__pages == 0:
            return 0.0
        return (self._current / self.__pages) * 100.0

    def get_pages(self) -> int:         # public getter for private data
        return self.__pages


class AnnotatedBook(Book):
    def __init__(self, title: str, author: str, pages: int):
        super().__init__(title, author, pages)
        self._notes = []                # protected

    def add_note(self, page: int, text: str) -> None:
        if not (0 <= page <= self.get_pages()):
            raise ValueError("Page out of bounds.")
        self._notes.append((page, text))

    def export_notes(self) -> str:
        lines = [f"'{self.title}' by {self._author} ({self.get_pages()} pages)", "Annotations:"]
        for p, t in self._notes:
            lines.append(f"- p.{p}: {t}")
        return "\n".join(lines)


# Using class and subclass
book = Book("Gideon the Ninth", "Tamsyn Muir", 496)
book.read(25)                           # updates protected _current, limited by private __pages
print(f"Progress: {book.progress():.1f}%")
print(book.get_pages())                 # accessed via getter

abook = AnnotatedBook("Nona the Ninth", "Tamsyn Muir", 512)
abook.read(50)
abook.add_note(10, "She appears!")
print(abook.export_notes())
