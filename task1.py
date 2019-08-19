class Abiturient:
    __name = ""
    __surname = ""
    __secondname = ""
    __phone = ""
    __marks = []

    def __init__(self):
        self.__name = ""
        self.__surname = ""
        self.__secondname = ""
        self.__phone = ""
        self.__marks = []

    def __init__(self, name, surname, secondname, phone, marks):
        self.__name = name
        self.__surname = surname
        self.__secondname = secondname
        self.__phone = phone
        self.__marks = marks
        print("Создан абитуриент ", str(self.__surname), str(self.__name), str(self.__secondname), "\n")

    def set_name(self, name):
        if name is str:
            self.__name = name
        else:
            print("Имя некорректно.\n")

    def set_surname(self, surname):
        if surname is str:
            self.__surname = surname
        else:
            print("Фамилия некорректна.\n")

    def set_secondname(self, secondname):
        if secondname is str:
            self.__secondname = secondname
        else:
            print("Отчество некорректно.\n")

    def set_phone(self, phone):
        if phone is str:
            self.__phone = phone
        else:
            print("телефон некорректен. Введите телефон в формате +XXX-XX-XXX-XX-XX\n")

    def set_marks(self, marks):
        if marks is list:
            for i in range(len(marks)):
                if marks[i] is int:
                    continue
                else:
                    print("Оценки могут быть только целочисленными.")
                    return
            self.__marks = marks

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_secondname(self):
        return self.__secondname

    def get_phone(self):
        return self.__phone

    def get_marks(self):
        return self.__marks

#    def __setattr__(self, key, value):
#        if key == "name":
#            self.set_name(value)
#        elif key == "surname":
#            self.set_surname(value)
#        elif key == "secondname":
#            self.set_secondname(value)
#        elif key == "phone":
#            self.set_phone(value)
#        elif key == "marks":
#            self.set_marks(value)
#        else:
#            print("Поле ", str(key), " не найдено в классе.\n")
#            return


    def has_poor_grades(self):
        flag = False
        for i in range(len(self.__marks)):
            if self.__marks[i] < 4:
                flag = True
        return flag

    def grades_above_value(self, value):
        flag = False
        sum_grade = 0
        for i in range(len(self.__marks)):
            sum_grade += self.__marks[i]
        if sum_grade > value:
            flag = True
        return flag


Abiturients = [Abiturient("Имя1", "Фамимлия1", "Отчество1", "+357-29-111-11-11", [5,6,7,4,6,7,9,6]),
               Abiturient("Имя2", "Фамимлия2", "Отчество2", "+357-29-222-22-22", [2,7,8,9,10,1,9,6]),
               Abiturient("Имя3", "Фамимлия3", "Отчество3", "+357-29-333-33-33", [9,10,8,9,9,9,9,10]),
               Abiturient("Имя4", "Фамимлия4", "Отчество4", "+357-29-444-44-44", [5,6,7,2,6,1,1,6]),
               Abiturient("Имя5", "Фамимлия5", "Отчество5", "+357-29-555-55-55", [5,6,7,4,3,2,9,6])]

for i in range(len(Abiturients)):
    if Abiturients[i].has_poor_grades() == True:
        print(Abiturients[i].get_surname(), Abiturients[i].get_name(), " имеет неудовлетворительные оценки.")

print("------------------------------------------\n")

border = int(input("Введите пограничную сумму баллов:\n"))

for i in range(len(Abiturients)):
    if Abiturients[i].grades_above_value(border) == True:
        print(Abiturients[i].get_surname(), Abiturients[i].get_name(), " имеет сумму баллов выше заданной.")

print("------------------------------------------\n")



