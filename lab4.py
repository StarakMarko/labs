# №23
class Park:

    def __init__(self, address="Franko street 1", length=900, price=70):
        self.__address = address
        self.__length = length
        self.__price = price

        self.area = 500
        self.name = "Stryiskyi"

    def get_address(self):
        return self.__address

    def get_length(self):
        return self.__length

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"park: name = {self.name}, adress = {self.__address}"

    def __repr__(self):
        return (
            f"park:\n"
            f"  name = {self.name}\n"
            f"  address = {self.__address}\n"
            f"  price = {self.__price}\n"
            f"  length = {self.__length}\n"
            f"  area = {self.area}"
        )

    def __del__(self):
        print("class park deleted")


def main():
    park_1 = Park()
    park_2 = Park("Bandera street 8", 100, 10)
    park_3 = Park("Shevchenko street 5", 500, 50)

    print(repr(park_1))
    print(repr(park_2))
    print(repr(park_3))


main()
