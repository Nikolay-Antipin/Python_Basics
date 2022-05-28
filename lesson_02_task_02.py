"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
"""

test_list = []
number_of_list_items = int(input("Введите кол-во элементов списка: "))
counter = 1
index_first = 0
index_second = 1

while counter <= number_of_list_items:
    test_list.append(input(f"Введите {counter} элемент из {number_of_list_items}: "))
    counter = counter + 1

print(f"Первоначальный список: {test_list}")

counter = 0

if len(test_list) % 2 == 0:
    while counter < number_of_list_items / 2:
        test_list[index_second], test_list[index_first] = test_list[index_first], test_list[index_second]
        index_first = index_first + 2
        index_second = index_second + 2
        counter = counter + 1
else:
    counter = counter + 1
    while counter < number_of_list_items / 2:
        test_list[index_second], test_list[index_first] = test_list[index_first], test_list[index_second]
        index_first = index_first + 2
        index_second = index_second + 2
        counter = counter + 1

print(f"Итоговый список после замены: {test_list}")
