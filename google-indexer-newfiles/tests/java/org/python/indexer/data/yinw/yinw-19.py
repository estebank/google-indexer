def f():
  try:
    p = f(1)
  except error, v:
    raise error, v # invalid expression

# try:
#      this_fails()
# except ZeroDivisionError as detail:
#      print 'Handling run-time error:', detail
