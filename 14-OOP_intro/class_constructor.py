class Calculator:
    """"Contoh class dengan menggunakan constructor"""

    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value

    def add(self):
        return self.first_value + self.second_value

    def add_with_operator(self):
        return self.first_value + self.second_value

    @classmethod
    def multiply(cls, first_value, second_value):
        return first_value * second_value

    @staticmethod
    def divide(first_value, second_value):
        return first_value / second_value


result = Calculator(2, 5)
print(result.first_value)
print(result.second_value)
print(result.add())
print(result.multiply(2, 4))

print(Calculator.multiply(2, 9))
print(Calculator.divide(2, 5))

print(Calculator.add_with_operator(result))
