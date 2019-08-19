from Person import Person
from Author import Author
from PublishingHouse import PublishingHouse
from PrintEdition import PrintEdition
from Book import Book


class Textbook(PrintEdition):

    def __init__(self, subject, name, volume, author, publishinghouse):
        self.__subject = subject
        PrintEdition.__init__(self, name, volume, author, publishinghouse)

    def print_textbook_inform(self):
        print("Учебник ", PrintEdition.get_name(), "\n")

    def get_subject(self):
        return self.__subject

