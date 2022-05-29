"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_numbers(dividend, divisor):
    try:
        quotient = dividend / divisor
        print(f"Ответ: {dividend} / {divisor} = {quotient}")

    except ZeroDivisionError:
        print("Внимание! На ноль делить нельзя!")


user_dividend = int(input(f"Задайте делимое число (то, которое нужно разделить): "))
user_divisor = int(input(f"Задайте делитель числа (то, на которое нужно разделить): "))
division_numbers(user_dividend, user_divisor)
