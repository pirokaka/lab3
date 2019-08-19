class Person:
    __age = 0
    __sex = ""
    __name = ""
    __surname = ""

    def __init__(self, age, sex, name, surname):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__sex = sex

    def get_age(self):
        return self.__age

    def get_sex(self):
        return self.__sex

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname
