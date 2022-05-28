"""
6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

products = []
item_parameter = {"Наименование": "", "Цена": "", "Кол-во": "", "Ед. измерения": ""}
product_analytics = {"Наименование": [], "Цена": [], "Кол-во": [], "Ед. измерения": []}
counter = 0
item_parameter_tmp = None

quantity_of_goods = int(input("Введите количество наименований товаров: "))

while counter < quantity_of_goods:
    for el in item_parameter.keys():
        item_parameter_tmp = input(f"{el} товара: ")
        item_parameter[el] = int(item_parameter_tmp) if (el == "Цена" or el == "Кол-во") else item_parameter_tmp
        product_analytics[el].append(item_parameter[el])
    products.append((counter, item_parameter))
    counter = counter + 1

print("Аналитика товаров:")
for key, value in product_analytics.items():
    print(f'{key[:25]}: {value}')
