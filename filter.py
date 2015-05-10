import re



def filter_ex_1():
  # -----------------------------------------
  # Print lines that have the word lamb in it
  # -----------------------------------------

  poem = '''Mary had a little lamb,\n
  Little lamb, little lamb,\n
  Mary had a little lamb,\n
  Its fleece was white as snow\n

  And everywhere that Mary went,\n
  Mary went, Mary went,\n
  Everywhere that Mary went\n
  The lamb was sure to go\n

  It followed her to school one day\n
  School one day, school one day\n
  It followed her to school one day\n
  Which was against the rules.\n

  It made the children laugh and play,\n
  Laugh and play, laugh and play,\n
  It made the children laugh and play\n
  To see a lamb at school\n

  And so the teacher turned it out,\n
  Turned it out, turned it out,\n
  And so the teacher turned it out,\n
  But still it lingered near\n

  And waited patiently about,\n
  Patiently about, patiently about,\n
  And waited patiently about\n
  Till Mary did appear\n

  "Why does the lamb love Mary so?"\n
  Love Mary so? Love Mary so?\n
  "Why does the lamb love Mary so?"\n
  The eager children cry\n

  "Why, Mary loves the lamb, you know."\n
  Loves the lamb, you know, loves the lamb, you know\n
  "Why, Mary loves the lamb, you know."\n
  The teacher did reply'''


  def f(x): 
    """ This function returns a 1 if input matches the word 'lamb' """
    return re.search('lamb', x)

  # Filter function takes 2 arguments filter(function, list)
  # function returns a boolean argument True or False
  # function is applied to every element in the list.
  # Only if function returns True the element is included in the final list
  fil_lines_list = filter (f, poem.split('\n'))

  # Print the filtered list
  for line in fil_lines_list:
    print line



def filter_ex_2():
  # -----------------------------------------
  # Print even numbers from the list
  # -----------------------------------------
  fib = [0,1,1,2,3,5,8,13,21,34,55]

  result = filter(lambda x: x % 2 == 0, fib)

  print result
  
  # Odd numbers
  #result = filter(lambda x: x % 2, fib)

  #print result


def filter_ex_3():
  # -----------------------------------------
  # Print -ve numbers
  # -----------------------------------------
  neg_num = filter( lambda x: x < 0, range(-5,5))
  print neg_num

filter_ex_1()
filter_ex_2()
filter_ex_3()






