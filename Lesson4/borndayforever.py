"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def get_day_or_year(isday=False):
    words=["год", "day"]
    val = int(input(f'Ввведите { words[int(isday)]} рождения А.С.Пушкина:'))
    return val

while True:
    year = get_day_or_year()
    if(1799 == year): break
    print("Не верно")
   
while True:
    day= get_day_or_year(True)
    if(6 == day): break
    print("Не верно")

print('Верно')
