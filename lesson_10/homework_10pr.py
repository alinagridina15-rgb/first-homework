# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language="JS"):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size, programming_language="JS"):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


teamlead = TeamLead("Nick", 1000, "IT", 50)  # programming_language буде "Python" за замовчуванням

print(teamlead.name)
print(teamlead.salary)
print(teamlead.department)
print(teamlead.team_size)
print(teamlead.programming_language)



# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def squre(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.__side = side

    def squre(self):
        return self.__side ** 2

    def perimetr(self):
        return 4 * self.__side


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def squre(self):
        return pi * (self.__radius ** 2)

    def perimetr(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def squre(self):
        return self.__width * self.__height

    def perimetr(self):
        return 2 * (self.__width + self.__height)


# Перевірка
shapes = [Square(5), Circle(2), Rectangle(3, 4)]
for s in shapes:
    print(s.__class__.__name__, "square:", s.squre(), "perimeter:", s.perimetr())
