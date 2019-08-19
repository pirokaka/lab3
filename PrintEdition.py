from Person import Person
from Author import Author
from PublishingHouse import PublishingHouse

class PrintEdition():
    
    def __init__(self, name, volume, author, publishinghouse):
        self.__name = name
        self.__volume = volume
        self.__author = author
        self.__publishinghouse = publishinghouse

    def get_name(self):
        return self.__name

    def get_volume(self):
        return self.__volume

    def get_author(self):
        return self.__author
    
    def get_publishinghouse(self):
        return self.__publishinghouse

