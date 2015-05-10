def file_copy_ex1():
  # --------------------------------------------------------------------------
  # This example shows how to copy a file in python
  # Opens a file in 'r' mode, Reads it in a string using f.read()
  # Opens a file in 'w' mode, Writes the string in it
  # NOTE: Make sure file_write.py is executed so that it generates the poem1.txt 
  # file required in this example
  # --------------------------------------------------------------------------

  # Open the file for reading
  try:
    fobj_rd = open("poem1.txt", 'r')
  except IOError:
    print 'ERROR Failed to open file poem1.txt for reading'

  # Read the file in a string object
  file_str = fobj_rd.read()
  
  # Open the file for writing
  try:
    fobj_wr = open("poem_cp.txt", 'w')
  except IOError:
    print 'ERROR Failed to open file poem_cp.txt for writing'

  # Copy the file on console
  print >> fobj_wr, file_str

  # Print Copy complete message
  print 'Copied poem1.txt to poem_cp.txt'

  # Close the file object
  fobj_rd.close()
  fobj_wr.close()

file_copy_ex1()
