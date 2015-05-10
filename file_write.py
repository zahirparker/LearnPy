def file_write_ex1():
  # --------------------------------------------------------------------------
  # This example shows how to open a file for Writing
  # Formatted Write to a file using print statement
  # + print statements can be easily converted to write from console to file
  #   no change is needed in the print formatting only add '>> fobj' 
  # print x               .. write to console
  # print >> fobj, x      .. write to a file
  # --------------------------------------------------------------------------

  # Open the file for writing
  try:
    fobj = open("poem1.txt", 'w')
  except IOError:
    print 'ERROR Failed to open file poem1.txt for writing'

  poem = '''Mary had a little lamb,
  Little lamb, little lamb,
  Mary had a little lamb,
  Its fleece was white as snow

  And everywhere that Mary went,
  Mary went, Mary went,
  Everywhere that Mary went
  The lamb was sure to go

  It followed her to school one day
  School one day, school one day
  It followed her to school one day
  Which was against the rules.

  It made the children laugh and play,
  Laugh and play, laugh and play,
  It made the children laugh and play
  To see a lamb at school

  And so the teacher turned it out,
  Turned it out, turned it out,
  And so the teacher turned it out,
  But still it lingered near

  And waited patiently about,
  Patiently about, patiently about,
  And waited patiently about
  Till Mary did appear

  "Why does the lamb love Mary so?"
  Love Mary so? Love Mary so?
  "Why does the lamb love Mary so?"
  The eager children cry

  "Why, Mary loves the lamb, you know."
  Loves the lamb, you know, loves the lamb, you know
  "Why, Mary loves the lamb, you know."
  The teacher did reply'''

  # Write to file
  print >> fobj, poem

  # Formatted write to a file
  print >> fobj
  print >> fobj, 'Number of lines in the poem :', len(list(poem.split('\n')))
  print >> fobj, '%d characters in the poem' % len(poem)

  # Close the file object
  fobj.close()

def file_write_ex2():
  # TODO
  # --------------------------------------------------------------------------
  # This example shows how to open a file for Writing
  # Formatted Write to a file using f.write()
  #  print statements can be easily converted to f.write 
  #   as long as print follows 'format specifier' % (variable) format
  #  print 'xyz', var   when written as f.write('xyz', var) will not work as
  #  f.write takes only one string argument
  #  - \n has to be explicity added to the f.write('xyz\n')
  # --------------------------------------------------------------------------

  # Open the file for writing
  try:
    fobj = open("poem2.txt", 'w')
  except IOError:
    print 'ERROR Failed to open file poem2.txt for writing'

  poem = '''Mary had a little lamb,
  Little lamb, little lamb,
  Mary had a little lamb,
  Its fleece was white as snow

  And everywhere that Mary went,
  Mary went, Mary went,
  Everywhere that Mary went
  The lamb was sure to go

  It followed her to school one day
  School one day, school one day
  It followed her to school one day
  Which was against the rules.

  It made the children laugh and play,
  Laugh and play, laugh and play,
  It made the children laugh and play
  To see a lamb at school

  And so the teacher turned it out,
  Turned it out, turned it out,
  And so the teacher turned it out,
  But still it lingered near

  And waited patiently about,
  Patiently about, patiently about,
  And waited patiently about
  Till Mary did appear

  "Why does the lamb love Mary so?"
  Love Mary so? Love Mary so?
  "Why does the lamb love Mary so?"
  The eager children cry

  "Why, Mary loves the lamb, you know."
  Loves the lamb, you know, loves the lamb, you know
  "Why, Mary loves the lamb, you know."
  The teacher did reply'''

  # Write to file
  fobj.write(poem)

  # Formatted write to a file
  fobj.write('\n')
  fobj.write('Number of lines in the poem : %d\n' % len(list(poem.split('\n'))))
  fobj.write('%d characters in the poem' % len(poem))

  # Close the file object
  fobj.close()


file_write_ex1()
file_write_ex2()
