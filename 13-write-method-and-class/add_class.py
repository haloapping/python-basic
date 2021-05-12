def world():
    print("Hi hi :)")


firstname = "Apping"


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def walk(self):
        print(self.firstname + " " + self.lastname + " berjalan menggunakan kaki")
