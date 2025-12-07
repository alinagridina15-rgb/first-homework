# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
number_a=1
number_b=2
def calculate_sum(number_a, number_b):
    return number_a+number_b
print(calculate_sum(number_a, number_b))
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers=[2,4,6,11,15]
def average(numbers):
    return sum(numbers)/len(numbers)
print(average(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    reversed_text = ""
    for letter in text:
        reversed_text = letter + reversed_text
    return reversed_text


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
words = ["dove", "me", "district", "matter"]
def longest_word(words):
    return max(words, key=len)
print(longest_word(words))






# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    for i in range(len(str1) - len(str2) + 1):
        if str1[i:i+len(str2)] == str2:
            return i
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 07
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
def fix_newlines(text):
    return text.replace("\n", " ")


# task 08
""" Замініть .... на пробіл """
def replace_dots(text):
    return text.replace("....", " ")


# task 09
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами. """
def normalize_spaces(text):
    return " ".join(text.split())


# task 10
""" Поверніть, скільки разів у тексті зустрічається літера "h" """
def count_h(text):
    return text.count("h")
