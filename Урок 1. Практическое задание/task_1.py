"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
x1 = 7
x2 = 8
x3 = x1 + x2
print(x3)
x3 =x1 - x2
print(x3)
x3 =x1 * x2
print(x3)
a = int(input("Введите число а:"))
b = int(input("Введите число b:"))
s = a + b
print(s)

user_name = input("Enter your user name and press Enter ")
print(f"Вы ввели {user_name}")