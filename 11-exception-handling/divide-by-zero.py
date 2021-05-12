try:
    print(2 / 0)
except ZeroDivisionError:
    print("Cannot divide with zero")

try:
    with open("../10-erro-and-exception-handling/exception-errors.py") as file:
        print(file.read())
except (FileNotFoundError,):
    print("File not found")

d = {"mean": "10.0"}

try:
    print("Mean: ", d["rata-rata"])
except KeyError:
    print("Key not found")
except ValueError:
    print("Value not match")
