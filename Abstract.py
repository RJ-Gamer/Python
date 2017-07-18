from abc import ABCMeta, abstractmethod

class Employee(ABCMeta):

    @abstractmethod

    def calculate_salary(self, salary):
        pass

class Developer(Employee):
    def calculate_salary(self, salary):
        totalSalary = salary * 1.10
        return totalSalary

Rajat = Developer()

print(Rajat.calculate_salary(10000))
