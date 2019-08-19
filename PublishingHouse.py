class PublishingHouse:
    __name = ""
    __address = ""
    __turnaround = 0

    def __init__(self, name, address, turnaround):
        self.__name = name
        self.__address = address
        self.__turnaround = turnaround

    def get_publ_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_turnaround(self):
        return self.__turnaround
