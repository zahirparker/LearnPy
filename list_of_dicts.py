from pprint import pprint
def list_of_dict_ex1():
  # Make a list of dictionary
  dict_list = []

  # 
  dict_list.append({'name': 'Tom', 'age': 10})
  dict_list.append({'name': 'Tim', 'age': 11})
  dict_list.append({'name': 'Tor', 'age': 12})
  
  print dict_list

def list_of_dict_ex2():
  people = [
              {'name': 'Tom', 'age': 10},
              {'name': 'Tim', 'age': 11},
              {'name': 'Tor', 'age': 12}
            ]
  # Print the list of dictionary
  print people
  print 
  
  # Filter the list of dictionary and find the dictionary that has name='Tom'
  filter_list = filter(lambda person: person['name'] == 'Tom', people)

  # Print list using map
  # map(lambda x: print(x), filter_list)
  # Will not work because print is not a function in Python 2.x, print is a
  # statement in Python 2.x

  # Solution 1:
  # Make a wrapper function and pass it to map
  # def p(x):
  #   print x
  # map(p, lst)

  # Solution 2
  # from __future__ import print_function
  # map(print, lst)
  # This changes the behaviour of print completely
  # This makes print into a function just as it is in Python 3.x, so it works with map().

  # Solution 3
  # from pprint import pprint
  # map(pprint, lst)


  # Print the filtered list
  if filter_list:
    map(pprint, filter_list)



list_of_dict_ex1()
list_of_dict_ex2()
