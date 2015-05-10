def reduce_ex_1():
  # --------------------------------------
  # Print the sum of 1 - 100
  # --------------------------------------
  sum = reduce(lambda x, y: x + y, range(1,101))
  print sum
  print

def reduce_ex_2():
  # --------------------------------------
  # Find the Max number in the list
  # --------------------------------------
  max = reduce(lambda x, y: x if x > y else y, [1, 4, 31, 103, 201, 45, 6, 9])
  print max
  print

def reduce_ex_3():
  # --------------------------------------
  # Concatenate a list of strings to make a sentence
  # --------------------------------------
  L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
  print reduce( (lambda x,y:x+y), L)
  # We get the same using join
  print ''.join(L)
  print


def reduce_ex_4():
  # --------------------------------------
  # Sum of Squares of 1 - 100
  # --------------------------------------
  sum_of_squares = reduce(lambda x, y: x + y, map(lambda x: x ** 2, range(1,101)))
  print 'Sum of squares of 1-100 is ', sum_of_squares
  print

# The function reduce(func, seq) continually applies the function func() to the sequence seq.
# It returns a single value. 
# If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
# At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
# In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
# The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
# Continue like this until just one element is left and return this element as the result of reduce()

reduce_ex_1()
reduce_ex_2()
reduce_ex_3()
reduce_ex_4()

'''Reference: http://www.python-course.eu/lambda.php'''
'''http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php'''
