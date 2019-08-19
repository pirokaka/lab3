from Person import Person
from Author import Author
from PublishingHouse import PublishingHouse
from PrintEdition import PrintEdition

class Book(PrintEdition,PublishingHouse):

    def __init__(self, genre, name, volume, author, publishinghouse):
        self.__genre = genre
        PrintEdition.__init__(self, name, volume, author, publishinghouse)

    def print_book_inform(self):
        print("Книга ", self.get_name(), " издаётся ", self.get_publishinghouse().get_publ_name(), "\n")

    def get_genre(self):
        return self.__genre

