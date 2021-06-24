# OOP Tasks
Here are some of the tasks for object oriented programming:

## `control_flow.py`
This task will combine our knowledge of OOP and control flow!

First we define the parameters we want the user to have:
```python
class User:
    def __init__(self, age, driver_license):
        self.age = age
        self.driver_license = driver_license
        self.age_limit_voting = 16
        self.age_limit_driving = 17
        self.age_limit_drink = 18
        self.age_limit_student = 18
```
Note that we also took this time to define the limits too to make them easier to adjust later on!

Then we start defining the individual checks so we can call them one at a time at a later date
```python
    def vote_check(self):
        if self.age >= self.age_limit_voting:
            return f"You are {age} which is older than {self.age_limit_voting}, so go register vote"
        else:
            return f"Sorry! You need to be {self.age_limit_voting}, only {self.age_limit_voting - self.age} years to go until you can vote!"
```
So we've added a little bit of personalisation so the user is able to see how close to the limits they are
```python
    def drive_check(self):
        if self.driver_license and self.age >= self.age_limit_driving:
            return f"{self.age} is more than the required {self.age_limit_driving}. Stay safe out there!"
        else:
            return f"Sorry! You need to be {self.age_limit_driving}, only {self.age_limit_driving - self.age} years to go until you can drive"

    def drink_check(self):
        if self.age < self.age_limit_drink:
            return f"Sorry! You need to be {self.age_limit_drink}, only {self.age_limit_drink - self.age} years to go until you can drink"
        else:
            return f"{self.age} is more than {self.age_limit_drink}, so enjoy yourself!"

    def student_check(self):
        if self.age < self.age_limit_student:
            return f"Sorry to say but at the age of {self.age} is less than {self.age_limit_student}, so you've got {self.age_limit_student - self.age} years left at school!"
        else:
            return f"{self.age} is older than {self.age_limit_student} so you must be out of school! Enjoy!"
```
Next up we're actually going to be running what the user will see first, we're going to ask them for their age which will be useful for the above calculations...
```python
while True:
    age = input('What\'s your age? ')
    while not age.isdigit():
        print('Invalid Input. Try again.')
        age = input('What\'s your age? ')
    break
```
Then we'll ask them if they have a driver's license:
```python
while True:
    response = input("Do you have a driver's license?\nEnter yes or no: ")
    if response.strip().lower() == "yes":
        driver_license = True
        break
    elif response.strip().lower() == "no":
        driver_license = False
        break
    elif response.strip().lower() == "exit":
        exit()
    else:
        print("Invalid Input. Try again")
```
Then we assign the class and functions that we want to use to a variable to make it easier to call:
```python
person = User(int(age), driver_license)
```
Finally we simply print out to screen!
```python
print(person.vote_check())
print(person.drive_check())
print(person.drink_check())
print(person.student_check())
```

## `calculator.py`
We were tasked to create a calculator with the basic functions, add, subtract, multiply and divide:
```python
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2
```
So first the different operations were defined.

Then we assign the class and functions that we want to use to a variable to make it easier to call:
```python
calculation = Calculator()
```
Then we asked the user what they wanted to do and with what numbers
```python
operation = input("What operation would you like to do?\nAdd, Subtract, Multiply, Divide? ")
num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))
```
Finally, we carried out the operations for them:
```python
if operation.strip().lower() == "add":
    print(calculation.add(num1, num2))
elif operation.strip().lower() == "subtract":
    print(calculation.subtract(num1, num2))
elif operation.strip().lower() == "multiply":
    print(calculation.multiply(num1, num2))
elif operation.strip().lower() == "divide":
    print(calculation.divide(num1, num2))
```

## `functional_calculator.py`
Next we had to create a new file that inherited the classes and functions of `calculator.py` and added a few new functions

First the imports:
```python
from calculator import Calculator
import math
```
We import our `Calculator` class from the previous task as well as `math` to help with some of the operations we're going to be doing later on:
```python
class FunctionalCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def circle_area(self, num1):
        return math.pi * (num1 ** 2) # We needed pi from math to calculate this

    def square_area(self, num1, num2):
        return self.multiply(num1, num2)

    def triangle_area(self, num1, num2):
        return .5 * self.multiply(num1, num2)
```
Here we define our different operations which are just some simple area calculations

We assign the class and functions that we want to use to a variable again to make it easier to call:
```python
calc = FunctionalCalculator()
```
Then we asked the user what they wanted to do and with what numbers. Since `circle_area` only needs one number, we'll only ask for one now, ask for the other later 
```python
operation = input("What operation would you like to do?\nCircle, Square, Triangle? ")
num1 = int(input("What is your first number? "))
```
Finally, we carried out the operations for them:
```python
if operation.strip().lower() == "circle":
    print(calc.circle_area(num1))
elif operation.strip().lower() == "square":
    num2 = input("What is your second number? ")
    print(calc.square_area(num1, num2))
elif operation.strip().lower() == "triangle":
    num2 = input("What is your second number? ")
    print(calc.triangle_area(2, 4))
```