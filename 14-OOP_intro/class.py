class Person:
    firstname = ""
    lastname = ""

    def sayHi(self):
        return "Say Hi"

Person.firstname = "Alfiyanto"
Person.lastname = "Kondolele"

print(Person.firstname + " " + Person.lastname)