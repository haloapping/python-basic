class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add_number(self, first_number, second_number):
        self.value = first_number + second_number

        if self.value > 9:
            print("Value is" + self.value)

        return self.value


class CalculatorMultiply(Calculator):
    def multiply(self, first_value, second_value):
        self.value = first_value * second_value

        return self.value


calculator_multiply = CalculatorMultiply()
print(calculator_multiply.multiply(2, 5))
print(calculator_multiply.multiply(10, 17))
