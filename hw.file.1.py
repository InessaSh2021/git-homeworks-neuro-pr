from pprint import pprint

 
    with open('cook_book_file.txt') as file:
        cook_book = dict()
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
       
pprint(cook_book)
