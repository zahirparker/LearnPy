def zip_ex_1():
  # ------------------------------------------------
  # Suppose we have two lists
  # we want to make them a list making pairs with 
  # ------------------------------------------------
  a = [1,2,3]
  b = [4,5,6]
  z = zip(a,b)
  print z

  # reverse the zip
  c, d = zip(*z)
  print c
  print d

zip_ex_1()

# TODO: cover more examples
'''http://www.bogotobogo.com/python/python_dictionary_comprehension_with_zip_from_list.php'''
