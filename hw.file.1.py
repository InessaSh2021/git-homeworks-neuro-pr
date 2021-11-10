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
