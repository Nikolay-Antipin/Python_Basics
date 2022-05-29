"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""


def sum_numbers_func():
    sum_numbers = 0
    exit_func = False
    while not exit_func:
        user_numbers = input("Вводите числа через пробел или нажмите Q для выхода: ").split()

        tmp_sum_numbers = 0
        for el in range(len(user_numbers)):
            if user_numbers[el] == "q" or user_numbers[el] == "Q" or user_numbers[el] == "й" or user_numbers[el] == "Й":
                exit_func = True
                break
            else:
                tmp_sum_numbers = tmp_sum_numbers + int(user_numbers[el])
        sum_numbers = sum_numbers + tmp_sum_numbers
        print(f"Текущая сумма чисел: {sum_numbers}")

    print(f"Вы нажали Q и вышли из программы. Итоговая сумма чисел: {sum_numbers}")


sum_numbers_func()
