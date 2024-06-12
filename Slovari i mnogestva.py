my_dict = {'Abdula': 1986}
print(my_dict)
print(my_dict['Abdula'])
print(my_dict.get('Madina'))
my_dict['Ahmed'] = 1990
print(my_dict)
my_dict.update({'Aliya': 2016, 'Magamed': 2010})
print(my_dict)
del my_dict['Abdula']
print(my_dict)
my_dict = {'Abdula': 1986, 'Ahmed': 1990, 'Aliya': 2016, 'Magamed': 2010}
print(my_dict)
my_dict.pop('Ahmed')
print(my_dict)

my_set = {1, 6, 8, 9, 678, 6, 8, 'banan', 'kiwi', 'grusha', 'kiwi'}
print(my_set)
print(my_set.add(4))
print(my_set)
print(my_set.discard(6))
print(my_set)