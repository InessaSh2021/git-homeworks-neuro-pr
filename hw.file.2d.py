from pprint import pprint

def get_shop_list_by_dishes(dishes_list, person_count):
  cook_book = dict()
  for dish in dishes_list:
    if dish not in cook_book:
      print('Такого блюда нет')
    else:
      for ingr in cook_book[dish]:
        cook_book[ingr['ingr_name']]['quantity'] += int(ingr['quantity']) * person_count
  return cook_book
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
