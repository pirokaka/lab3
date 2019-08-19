from Person import Person
from Author import Author
from PublishingHouse import PublishingHouse
from PrintEdition import PrintEdition
from Magazine import Magazine
from Book import Book
from Textbook import Textbook

person1 = Person(40, "male", "имя1", "фамилия1")
author1 = Author(person1, "фантастика")
publishinghouse1 = PublishingHouse("Рога и Копыта", "пушкина колотушкина", 50000)
printedition1 = PrintEdition("Властелин Колец", 400, author1,publishinghouse1)
book1 = Book("фантастика", "Властелин Колец", 400, author1, publishinghouse1)
book1.print_book_inform()