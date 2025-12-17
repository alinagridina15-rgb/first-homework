#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал"
# Створіть об('єкт цього класу, представляючи студента. '
# 'Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента. '
# 'Виведіть інформацію про студента та змініть його середній бал.)

class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade


student = Student('Alina','Hridina', 23,90)


print("Ім'я:", student.name)
print("Прізвище:", student.surname)
print("Вік:", student.age)
print("Середній бал:", student.average_grade)


student.change_average_grade(95)

print("Після зміни середнього балу:")
print("Середній бал:", student.average_grade)


