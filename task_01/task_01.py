# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


a = int(input("Введите день недели "))

if a > 7 or a < 1:
    print("такого дня нет")
elif a > 1 and a < 6:
    print("Нет - это не выходной")
elif a > 5 and a < 8:
    print("Да - это выходной")
