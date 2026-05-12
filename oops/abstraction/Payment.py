from abc import ABC, abstractmethod

class Payment(ABC):  # Inherit from ABC
    @abstractmethod
    def pay(self, amount: float): # Added a parameter for realism
        pass

class GPay(Payment):
    def pay(self, amount: float):
        print(f"Paying ${amount} via GPay")


class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self._salary = salary

    @property
    def salary(self) -> float:
        """The salary property getter."""
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if value < 0:
            # Raising an error is better than a print statement for APIs
            raise ValueError("Salary cannot be negative")
        self._salary = value

e1 = Employee("Kavin", 20000)
print(f"Employee: {e1.name}, Salary: {e1.salary}")