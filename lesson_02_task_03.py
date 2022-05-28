"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# Решение через dict:

user_number = input("Введите значение месяца в виде целого числа от 1 до 12: ")

dictionary_of_months = {"12": "Зима", "1": "Зима", "2": "Зима", "3": "Весна", "4": "Весна", "5": "Весна", "6": "Лето",
                        "7": "Лето", "8": "Лето", "9": "Осень", "10": "Осень", "11": "Осень"}

print(f"Решение через dict -> {user_number} месяц это: {dictionary_of_months.setdefault(user_number)}")

# Решение через list:

user_number = int(user_number)

list_of_month = ["Зима", "Весна", "Лето", "Осень"]

if user_number == 12 or user_number == 1 or user_number == 2:
    print(f"Решение через list -> {user_number} месяц это: {list_of_month[0]}")
elif user_number == 3 or user_number == 4 or user_number == 5:
    print(f"Решение через list -> {user_number} месяц это: {list_of_month[1]}")
elif user_number == 6 or user_number == 7 or user_number == 8:
    print(f"Решение через list -> {user_number} месяц это: {list_of_month[2]}")
elif user_number == 9 or user_number == 10 or user_number == 11:
    print(f"Решение через list -> {user_number} месяц это: {list_of_month[3]}")
