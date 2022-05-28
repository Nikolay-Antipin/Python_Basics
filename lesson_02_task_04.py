"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""

user_string = input("Введите строку из нескольких слов через пробел: ")
user_words = []
number = 1

for el in range(user_string.count(" ") + 1):
    user_words = user_string.split()
    if len(str(user_words)) <= 10:
        print(f"{number}. {user_words[el]}")
        number = number + 1
    else:
        print(f"{number}. {user_words[el][0:10]}")
        number = number + 1
