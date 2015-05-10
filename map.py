def map_ex_1():
  # --------------------------------------
  # Print the square of every item in list
  # --------------------------------------
  items = [1, 2, 3, 4, 5]
  squared = map(lambda x: x**2, items)
  print squared
  print

def map_ex_2():
  # ------------------------------------------------
  # Print the square and cube of every item in list
  # ------------------------------------------------
  items = [1, 2, 3, 4, 5]
  def square(x): return (x**2)
  def cube(x): return (x**3)
  funcs = [square, cube]
  for num in items:
    # lambda as a function, 'list of functions' as sequence
    ret_list = map(lambda x: x(num), funcs)
    print ret_list
  print

def map_ex_3():
  # ------------------------------------------------
  # map can be used in more advance way.
  # For example, given multiple sequence arguments,
  # it sends items taken form sequences in parallel as distinct arguments to the function
  # ------------------------------------------------
  print list(map(pow,[2, 3, 4], [10, 11, 12]))
  print 

def map_ex_4():
  # ------------------------------------------------
  # If function is None, the identity function is assumed
  # if there are multiple arguments, map() returns a list consisting of tuples containing the 
  # corresponding items from all iterables (a kind of transpose operation)
  # ------------------------------------------------
  m = [1,2,3]
  n = [1,4,9]
  new_tuple = map(None, m, n)
  print new_tuple
  print

def map_ex_5():
  # --------------------------------------
  # Increment every element of the list by 1
  # --------------------------------------
  items = [1, 2, 3, 4, 5]
  inc = map(lambda x: x+1, items)
  print inc
  print


# map(function, sequence)
# Map applies operation to each element in the sequence
# map is equivalent to for loops  (Example 1)
# map can work with a list of functions (Example 2)
# map has performance benifits over manually coded for loop
# map is similar to list comprehension expression. But map applies function call
# to each item instead of arbitrary expression. Because of this limitation it is
# somewhat less general.

# map can be used in more advance way.
# For example, given multiple sequence arguments,
# it sends items taken form sequences in parallel as distinct arguments to the
# function:(Example 3)

# If function is None, the identity function is assumed; if there are multiple arguments, map() 
# returns a list consisting of tuples containing the corresponding 
# items from all iterables (a kind of transpose operation)  (Example 4)
map_ex_1()
map_ex_2()
map_ex_3()
map_ex_4()
map_ex_5()



'''Reference: http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php'''
