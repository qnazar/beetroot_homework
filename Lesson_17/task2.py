"""Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list
for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books"""


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Book:
    number_of_books = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.number_of_books += 1

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'{self.name}. {self.author}'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def new_book(self, name: str, year: int, author: Author) -> Book:
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author) -> list:
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int) -> list:
        return [book for book in self.books if book.year == year]


l = Library('central')

j_k_row = Author('J.K.Rowling', 'Great Britain', 1965)
s_king = Author("Stephen King", 'USA', 1947)

l.new_book("Harry Potter and the Philosopher's Stone", 1997, j_k_row)
l.new_book("Harry Potter and Chamber of Secrets", 1998, j_k_row)
l.new_book("The Dark Tower IV: Wizard and Glass", 1997, s_king)

print(l.group_by_year(1997))
print(l.group_by_author(j_k_row))
