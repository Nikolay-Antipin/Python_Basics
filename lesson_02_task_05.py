"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

rating_list = [8, 6, 4, 4, 3]
print(f"Первоначальный рейтинг: {rating_list}")
new_rating_el = input("Введите значение рейтинга или напишите q для выхода:")

while new_rating_el != "q":
    new_rating_el = int(new_rating_el)
    for el in range(len(rating_list)):
        if rating_list[el] == new_rating_el:
            rating_list.insert(el + 1, new_rating_el)
            break
        elif rating_list[0] < new_rating_el:
            rating_list.insert(0, new_rating_el)
        elif rating_list[-1] > new_rating_el:
            rating_list.append(new_rating_el)
        elif rating_list[el] > new_rating_el > rating_list[el + 1]:
            rating_list.insert(el + 1, new_rating_el)

    print(f"Текущий рейтинг: {rating_list}")
    new_rating_el = int(input("Введите число: "))

print("Вы нажали q и вышли из программы!")
