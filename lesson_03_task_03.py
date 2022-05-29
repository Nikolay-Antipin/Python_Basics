"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def max_numbers(number_1, number_2, number_3):
    second_max_number = 0
    first_max_number = max(number_1, number_2, number_3)

    if first_max_number == number_1:
        second_max_number = max(number_2, number_3)
    elif first_max_number == number_2:
        second_max_number = max(number_1, number_3)
    elif first_max_number == number_3:
        second_max_number = max(number_1, number_2)

    sum_max_numbers = first_max_number + second_max_number
    print(f"Сумма наибольших аргументов {first_max_number} и {second_max_number} равна: {sum_max_numbers}")


user_number1 = int(input(f"Введите первое число: "))
user_number2 = int(input(f"Введите второе число: "))
user_number3 = int(input(f"Введите третье число: "))

max_numbers(user_number1, user_number2, user_number3)
