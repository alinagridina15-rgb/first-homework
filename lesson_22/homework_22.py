# Імпорти
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

# Підключення до БД
engine = create_engine("sqlite:///students.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Моделі
class Enrollment(Base):
    __tablename__ = "enrollments"
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship(
        "Course",
        secondary="enrollments",
        back_populates="students"
    )

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String)

    students = relationship(
        "Student",
        secondary="enrollments",
        back_populates="courses"
    )

# Створення таблиць
Base.metadata.create_all(engine)

# Додавання даних
def seed_data():
    courses = [
        Course(title="Math"),
        Course(title="Physics"),
        Course(title="IT"),
        Course(title="History"),
        Course(title="English"),
    ]

    session.add_all(courses)
    session.commit()

    students = [Student(name=f"Student {i}") for i in range(1, 21)]
    session.add_all(students)
    session.commit()

    for student in students:
        student.courses = random.sample(courses, random.randint(1, 3))

    session.commit()

# CRUD-операції
def add_student(name, course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    student = Student(name=name)
    student.courses.append(course)
    session.add(student)
    session.commit()

def students_by_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    return [s.name for s in course.students]

def courses_by_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    return [c.title for c in student.courses]

# спроба запуску
if __name__ == "__main__":
    seed_data()
    add_student("New Student", "Math")

    print("Students in Math:", students_by_course("Math"))
    print("Courses of Student 5:", courses_by_student("Student 5"))
