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