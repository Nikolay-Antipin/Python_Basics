"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк
"""

user_seconds = int(input("Введите кол-во секунд: "))
minutes = int(user_seconds / 60)  # Вычисляем кол-во целых минут
seconds = user_seconds - minutes * 60  # Вычисляем кол-во оставшихся секунд

if minutes >= 60:
    hours = int(minutes / 60)  # Вычисляем кол-во целых часов
    minutes = minutes - hours * 60  # Вычисляем кол-во оставшихся минут
else:
    hours = 0

print(f'{user_seconds} секунд в формате чч:мм:сс: {hours:02}:{minutes:02}:{seconds:02}')
