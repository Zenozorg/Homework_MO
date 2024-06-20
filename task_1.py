class Car:

    type_of = "Car"

    def __init__(self, model, release, brand,engine_cap,color,price):
        self.__model = model
        self.__release= release
        self.__brand = brand
        self.__engine_cap = engine_cap
        self.__color = color
        self.__price = price


    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def set_model(self, model):
        self.__model = model

    def get_release(self):
        return self.__release

    def set_release(self, release):
        self.__release = release

    def set_release(self, release):
        self.__release = release

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_engine_cap(self):
        return self.__engine_cap

    def set_engine_cap(self, engine_cap):
        self.__engine_cap = engine_cap

    def set_engine_cap(self, engine_cap):
        self.__engine_cap = engine_cap

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def set_color(self, color):
        self.__color = color

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def set_price(self, price):
        self.__price = price

if __name__ == '__main__':
    print(Car.type_of)
    Car = Car(
        "Supra", "2021", "Toyota", "2.4L","red","40ml"
    )

    print(Car.get_model())
    Car.set_model("Land Cruiser Prado")
    print(Car.get_model())

    print(Car.get_release())
    Car.set_release("2021")
    print(Car.get_release())

    print(Car.get_brand())
    Car.set_brand("Toyota")
    print(Car.get_brand())

    print(Car.get_engine_cap())
    Car.set_engine_cap("4L")
    print(Car.get_engine_cap())
    
    print(Car.get_color())
    Car.set_color("black")
    print(Car.get_color())

    print(Car.get_price())
    Car.set_price("15ml")
    print(Car.get_price())
