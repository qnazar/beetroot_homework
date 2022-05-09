# The greeting program
from datetime import date

day = date.today()  # сьогоднішня дата

name = 'Nazar'  # ініціюю змінну для імені

# f-рядок
print(f"Good day {name}! {day.strftime('%A')} is a perfect day to learn some Python.")

# метод .format()
print("Good day {}! {} is a perfect day to learn some Python.".format(name, day.strftime('%A')))

# %
print("Good day %s! %s is a perfect day to learn some Python." % (name, day.strftime('%A')))
