from Person import Person

class Author(Person):

    def __init__(self, person, pref_genre):
        self.__person = person
        self.__preffered_genre = pref_genre

    def get_preffered_genre(self):
        return self.__preffered_genre

