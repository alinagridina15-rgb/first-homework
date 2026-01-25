#Генератори:
#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


for num in even_numbers(10):
    print(num)

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci(50):
    print(num)

# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


lst = [1, 2, 3, 4]
for item in ReverseIterator(lst):
    print(item)


class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            value = self.current
            self.current += 1
            if value % 2 == 0:
                return value
        raise StopIteration

for num in EvenIterator(10):
    print(num)

# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик {func.__name__} з аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка у функції {func.__name__}: {e}")
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

divide(10, 0)
