class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


calculation = Calculator()

operation = input("What operation would you like to do?\nAdd, Subtract, Multiply, Divide? ")
num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))

if operation.strip().lower() == "add":
    print(calculation.add(num1, num2))
elif operation.strip().lower() == "subtract":
    print(calculation.subtract(num1, num2))
elif operation.strip().lower() == "multiply":
    print(calculation.multiply(num1, num2))
elif operation.strip().lower() == "divide":
    print(calculation.divide(num1, num2))