class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Jobless(Person):
    def __init__(self, name, age, jobless_id):
        super().__init__(name, age)
        self.jobless_id = jobless_id


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


jobless = Jobless("Patrick", 15, "Lazy, stupid")
employee = Employee("Spanch Bob", 13, "Funny, (a little bit) stupid")

print(f"Jobless: {jobless.name}, {jobless.age} years old, Jobless ID: {jobless.jobless_id}")
print(f"Employee: {employee.name}, {employee.age} years old, Employee ID: {employee.employee_id}")