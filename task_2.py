class Book:

    type_of = "Book"

    def __init__(self, name, release, edition,genre,author,price):
        self.__name = name
        self.__release= release
        self.__edition = edition
        self.__genre = genre
        self.__author = author
        self.__price = price


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_release(self):
        return self.__release

    def set_release(self, release):
        self.__release = release

    def set_release(self, release):
        self.__release = release

    def get_edition(self):
        return self.__edition

    def set_edition(self, edition):
        self.__edition = edition

    def set_edition(self, edition):
        self.__edition = edition

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def set_author(self, author):
        self.__author = author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def set_price(self, price):
        self.__price = price

if __name__ == '__main__':
    print(Book.type_of)
    Book = Book(
        "Harry Potter", "1997", "Brit' Book", "Fantasy","J.K Rowling","3000"
    )

    print(Book.get_name())
    Book.set_name("War and Peace")
    print(Book.get_name())

    print(Book.get_release())
    Book.set_release("1867")
    print(Book.get_release())

    print(Book.get_edition())
    Book.set_edition("Russian Classic")
    print(Book.get_edition())

    print(Book.get_genre())
    Book.set_genre("novel")
    print(Book.get_genre())
    
    print(Book.get_author())
    Book.set_author("L.N Tostoy")
    print(Book.get_author())

    print(Book.get_price())
    Book.set_price("5000")
    print(Book.get_price())
