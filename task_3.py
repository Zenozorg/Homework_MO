class Stadium:

    type_of = "Stadium"

    def __init__(self, name, release, country,city,capacity):
        self.__name = name
        self.__release= release
        self.__country = country
        self.__city = city
        self.__capacity = capacity


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

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def set_country(self, country):
        self.__country = country

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def set_city(self, city):
        self.__city = city

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

if __name__ == '__main__':
    print(Stadium.type_of)
    Stadium = Stadium(
        "Grand Stadium", "1965", "USA","New York","90000"
    )

    print(Stadium.get_name())
    Stadium.set_name("Central Stadium")
    print(Stadium.get_name())

    print(Stadium.get_release())
    Stadium.set_release("1986")
    print(Stadium.get_release())

    print(Stadium.get_country())
    Stadium.set_country("Kazakhstan")
    print(Stadium.get_country())
    
    print(Stadium.get_city())
    Stadium.set_city("Almaty")
    print(Stadium.get_city())

    print(Stadium.get_capacity())
    Stadium.set_capacity("40000")
    print(Stadium.get_capacity())
