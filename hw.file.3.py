from pprint import pprint

import os

def sorted_file_list():
  file_list = os.scandir('https://github.com/netology-code/py-homework-basic-files/tree/master/2.4.files/sorted')

  with open (file_list, text) as file_name:
    number = 0
    dicht = {}
    for file_name in file_list:
      content = file_name.read()
      number = len(content)
      dicht.append(
        {file_name : number }
      )
    sorted(dicht.number(), reverse = True)
  
  for file_name in file_list:
    for file_name, number in dicht.items():
      res = print(f'{file_name}\n {number} \n {text} \n')

pprint(sorted_file_list(res))