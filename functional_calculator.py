from calculator import Calculator
import math

class FunctionalCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def circle_area(self, num1):
        return math.pi * (num1 ** 2)

    def square_area(self, num1, num2):
        return self.multiply(num1, num2)

    def triangle_area(self, num1, num2):
        return .5 * self.multiply(num1, num2)

calc = FunctionalCalculator()

operation = input("What operation would you like to do?\nCircle, Square, Triangle? ")
num1 = int(input("What is your first number? "))

if operation.strip().lower() == "circle":
    print(calc.circle_area(num1))
elif operation.strip().lower() == "square":
    num2 = input("What is your second number? ")
    print(calc.square_area(num1, num2))
elif operation.strip().lower() == "triangle":
    num2 = input("What is your second number? ")
    print(calc.triangle_area(2, 4))