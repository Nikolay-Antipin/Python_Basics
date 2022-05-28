"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

proceeds = int(input("Введите значение выручки Вашей фирмы: "))
costs = int(input("Введите значение издержек Вашей фирмы: "))
profitability = 0
percent_profitability = 0

if proceeds > costs:
    profitability = proceeds - costs
    ratio_profitability = profitability / proceeds
    percent_profitability = profitability * 100 / costs
    print(f"Фирма отработала с прибылью -> {profitability}")
    print(f"Прибыль составляет -> {percent_profitability}% от издержек!")
    print(f"Соотношение прибыли к выручке равно -> {ratio_profitability}")

else:
    print("Фирма отработала с убытком")

number_of_staff = int(input("Введите численность персонала Вашей фирмы: "))
profit_per_employee = profitability / number_of_staff
print(f"Прибыль на одного сотрудника составляет {profit_per_employee}")
