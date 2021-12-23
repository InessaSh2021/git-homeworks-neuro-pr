from pprint import pprint
import os

def sorted_file_list(file_list):
  file_list = os.scandir('D://HW')
  
  with open (file_list, text) as file:
    number = 0
    dict = {}
    for file in file_list:
      content = file.readline()
      number = len(content)
      dict.append(
        {file : number }
      )
      sorted_tuple = sorted(dict.items(), file=lambda x: x[1]) 
      sorted_tuple      
      dict(sorted_tuple)

      for file, number in dict.items():
        file[i] = number[i]
        print(file, number)

        with open('1.txt', 'a', '1.txt') as file:
          file.write('1.txt')

        with open('1.txt', 'a', file.number[1]) as file:
          file.write(f'{file.number[1]} \n')

        with open('2.txt', 'a', '2.txt') as file:
          file.write('2.txt')

        with open('2.txt', 'a', file.number[2]) as file:
          file.write(f'{file.number[2]} \n')

        with open('3.txt', 'a', '3.txt') as file:
          file.write('3.txt')

        with open('3.txt', 'a', file.number[3]) as file:
          file.write(f'{file.number[3]} \n')

          
        with open('1.txt') as first, open('2.txt', 'w') as second:
          data = first.read()
          second.write(data)

        with open('1.txt') as first, open('3.txt', 'w') as second:
          data = first.read()
          second.write(data)

pprint(sorted_file_list('1.txt, 2.txt, 3.txt'))
