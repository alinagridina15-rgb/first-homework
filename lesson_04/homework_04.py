adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

text = adventures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
text = text.replace("....", " ")
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
text = " ".join(text.split())

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("task 04:", text.count("h"))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = text.split()
capital_words = [w for w in words if w[0].isupper()]
print("Слів з великої літери:", len(capital_words))

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first = text.find("Tom")
second = text.find("Tom", first + 1)
print("task 06:", second)

# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = text.split(". ")
# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("task 08:", adventures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
starts = False
for s in adventures_of_tom_sawer_sentences:
    if s.startswith("By the time"):
        starts = True

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawer_sentences.
"""
last = adventures_of_tom_sawer_sentences[-1]
print("task 10:", len(last.split()))