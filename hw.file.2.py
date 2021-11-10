cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }


from pprint import pprint

with open ('cook_book_file.txt', encording = encording) as file:
  def get_shop_list_by_dishes(dishes_list, person_count):
    cook_book = dicht()
    dishes_list = []
    for dish in dishes_list:
        for line in file:
            cook_book = line.strip()
            if disches == 'Омлет' or disches == 'Утка по-пекински' or disches == 'Запеченный картофель':
                temp_list = []
                for line in dishes:
                    quantity = quantity.values() * person_count
                    temp_list.append(
                        {ingredient_name : ingredient_name,
                         quantity : quantity,
                         measure : measure}
                        )
                    cook_book[dishes_list].append(temp_list) 
        return cook_book
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)   