Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт

from pprint import pprint

def get_dicht('cook_book_file.txt'):  
    with open('cook_book_file.txt') as file:
        cook_book = dicht()
        for line in file:
            dishes = line.strip()
            counter = int(file.readline())
            temp_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline()
                temp_list.append(
                    {ingredient_name: ingredient_name,
                     quantity : quantity,
                     measure : measure}
                    )
            cook_book[dishes] = temp_list
            file.readline()
        return cook_book
pprint(get_data('cook_book_file.txt'))