from enum import Enum


class GuestGender(Enum):
    FEMALE = "Female"
    MALE = "Male"
    NON_BINARY = "Non binary"


class Guest:
    def __init__(self, id, name, age, city, phone_number, gender):
        self.id = id
        self.name = name
        self.age = age
        self.__city = city
        self.__phone_number = phone_number
        self.gender = gender

    def is_lucky_phone_number(self):
        str_phone_number = str(self.__phone_number)
        return str_phone_number.count("7") >= 3

    def get_phone_number(self):
        return self.__phone_number

    def get_city(self):
        return self.__city

    def __str__(self):
        return f"name = {self.name}, city = {self.__city}"

    def __del__(self):
        print("class Guest deleted")


class Party:
    def __init__(self, day, reason, guests):
        self.day = day
        self.reason = reason
        self.guests = guests

    def find_average_age(self, gender):
        total_age = 0
        number = 0
        for guest in self.guests:
            if guest.gender == gender:
                total_age += guest.age
                number += 1
        average_age = total_age / number
        return average_age

    def id_sort(self):
        for _ in range(len(self.guests) - 1):
            for i in range(len(self.guests) - 1):
                if self.guests[i].id > self.guests[i + 1].id:
                    self.guests[i], self.guests[i + 1] = (
                        self.guests[i + 1],
                        self.guests[i],
                    )
        guests_name = []
        for i in range(len(self.guests)):
            guests_name.append(self.guests[i].name)
        return guests_name

    def __del__(self):
        print("class Party deleted")


guest_1 = Guest(16, "Anna", 25, "Kyiv", 1237777, GuestGender.FEMALE)
guest_2 = Guest(2, "Ivan", 30, "Lviv", 1234567, GuestGender.MALE)
guest_3 = Guest(3, "Robot", 2, "Beijing", 7771237, GuestGender.NON_BINARY)
guest_4 = Guest(34, "Maria", 22, "Kharkiv", 4906765, GuestGender.FEMALE)
guest_5 = Guest(45, "Dmytro", 35, "Dnipro", 4561237, GuestGender.MALE)
guest_6 = Guest(1, "Yaryna", 27, "Zaporizhzhia", 3216549, GuestGender.FEMALE)

guests = [guest_1, guest_2, guest_3, guest_4, guest_5, guest_6]


def main():
    party = Party("Tuesday", "no reason", guests)
    print(guest_1.is_lucky_phone_number())
    print(guest_2.is_lucky_phone_number())
    print(guest_3.is_lucky_phone_number())
    print(guest_4.is_lucky_phone_number())
    print(guest_5.is_lucky_phone_number())
    print(guest_6.is_lucky_phone_number())
    print(party.id_sort())
    print(party.find_average_age(GuestGender.MALE))
    print(party.find_average_age(GuestGender.FEMALE))
    print(party.find_average_age(GuestGender.NON_BINARY))


main()
