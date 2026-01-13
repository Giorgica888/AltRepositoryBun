from person import Person
import numbers
class Employee(Person):
    def __init__(self, name, email, salary, adress):
        super().__init__(name, email, adress)
        self._salary = salary
        self.__warn()

    @property
    def get_salary(self):
        return self._salary

    @get_salary.setter
    def set_salary(self, salary):
        if isinstance(salary, float) and salary >= 0:
            self._salary = salary
        else:
            print(f"Unapropriate salary")

    def incease_salary(self, percentage):
        if isinstance(percentage, float) and percentage > 0:
            self._salary += self._salary*(percentage / 100)
        else:
            print(f"unapropriate percentage")

    def display_info(self):
        print(f"Name : {self.name} | Email : {self.get_email}")
        print(f"Salary : {self.get_salary} | Adress {self.get_adress}")

    def __warn(self):
        if not(
            isinstance(self.name, str)\
            and isinstance(self.get_salary, numbers.Real)\
            and isinstance(self.get_email, str)\
            and isinstance(self.get_adress, str))\
            or self.get_salary < 0:
            print(f"Este o eroare la introducerea obiectului {self.name} \n \
            Locatia : {hex(id(self))}")

