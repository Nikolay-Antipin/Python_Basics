"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def user_database(name, surname, year, city, email, telephone_number):
    return ", ".join([name, surname, year, city, email, telephone_number])


print(user_database(surname="Antipin", name="Nikolay", year="1994", city="Samara", email="qwerty@gmail.com",
                    telephone_number="8-123-456-78-91"))
