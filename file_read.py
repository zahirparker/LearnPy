def file_read_ex1():
  # --------------------------------------------------------------------------
  # This example shows how to open a file for Reading
  # Read the entire file in one shot
  # fobj.read() returns the entire file in one string 
  # --------------------------------------------------------------------------

  # Open the file for reading
  try:
    fobj = open("poem1.txt", 'r')
  except IOError:
    print 'ERROR Failed to open file poem1.txt for reading'

  # Read the file in a string object
  file_str = fobj.read()
  
  print 'x'*40
  print 'File Read Example 1'
  print 'x'*40

  # Print the type of file_str
  print 'TYPE fobj.read(): ', type(file_str)

  # Print the file on console
  print file_str

  # Close the file object
  fobj.close()

def file_read_ex2():
  # --------------------------------------------------------------------------
  # This example shows how to open a file for Reading
  # Read the entire file line by line
  # fobj.readlines() returns all lines from file as list of strings seperated by '\n'
  # --------------------------------------------------------------------------

  # Open the file for reading
  try:
    fobj = open("poem1.txt", 'r')
  except IOError:
    print 'ERROR Failed to open file poem1.txt for reading'
  
  # Read file in a list 
  lines_list = fobj.readlines()

  print 'x'*40
  print 'File Read Example 2'
  print 'x'*40

  # Print the type of lines_list
  print 'TYPE fobj.readlines(): ', type(lines_list)

  for line in lines_list:
    # Print the file on console
    print line.rstrip()
  
  # Close the file object
  fobj.close()

def file_read_ex3():
  # --------------------------------------------------------------------------
  # This example shows how to open a file for Reading
  # Open a file object
  # Loop over file object
  # This is memory efficient, fast, and leads to simple code
  # --------------------------------------------------------------------------

  # Open the file for reading
  try:
    fobj = open("poem1.txt", 'r')
  except IOError:
    print 'ERROR Failed to open file poem1.txt for reading'
  
  print 'x'*40
  print 'File Read Example 3'
  print 'x'*40

  # Print the type of fobj
  print 'TYPE fobj: ', type(fobj)

  for line in fobj:
    # Print the file on console
    print line.rstrip()
  
  # Close the file object
  fobj.close()


file_read_ex1()
file_read_ex2()
file_read_ex3()
