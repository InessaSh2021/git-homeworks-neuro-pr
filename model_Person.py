import requests

url = 'https://vk.com/id281950100?z=photo281950100_384882748%2Fphotos281950100'

class Person:
  '''������ ��������� �����'''
  
  def __init__(self, name, surname, gender, email):
    self.name = name
    self.surname = surname
    self.gender = gender    
    self.email = email
   

  def set_value(self):
    print('���: {}. �������: {}. ���: {}. email:{}'.format(self.name, self.surname, self.gender, self.email))  

person1 = Person(input('������� ��� ���������: ').capitalize(), input('������� ������� ���������: ').capitalize(), input('������� ��� ���������: ').capitalize(), input('������� email ���������: '))


print()

person1.set_value()


response = requests.get(url)
if response.status_code == 200:
  print('Success!')
elif response.status_code == 404:
  print('Not Found.')

with open("foto.png", "wb") as file:
  file.write(response.content)  
  print('������ ��������')
  file.write(response.content) 
  print('Status_code', response.status_code)
  print('Encoding', response.encoding)  
