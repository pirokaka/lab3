from Person import Person
from Author import Author
from PublishingHouse import PublishingHouse
from PrintEdition import PrintEdition

class Magazine(PrintEdition):
    __theme = ""
    __chiefeditor = ""

    def __init__(self, theme, chiefeditor, name, volume, author, publishinghouse):
        self.__theme = theme
        self.__chiefeditor = chiefeditor
        PrintEdition.__init__(self, name, volume, author, publishinghouse)

    def get_theme(self):
        return self.__theme

    def get_chiefeditor(self):
        return self.__chiefeditor

    def print_magazine_inform(self):
        print("Журнал ", PrintEdition.get_name(), "\n")
