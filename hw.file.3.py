from pprint import pprint

import os
lagest = 0

def sorted_file_list(file_list, text):
  file_list = os.scandir('D://HW')

  with open (file_list, text) as file:
    number = 0
    dict = {}
    for file in file_list:
      content = file.read()
      number = len(content)
      or file in file_list:
      content = file.read()
      number = len(content)
      dict.append(
        {file : number }
      )  
      lagest = max(dict.values())
      final_dict = {file:number for file, number in dict.items() if number == lagest}       
      if number
    sorted(dict.number(), reverse = True)
  
  for file in file_list:
    for file, number in dict.items():
      res = print(f'{file}\n {number} \n {text} \n')

pprint(sorted_file_list(res))
