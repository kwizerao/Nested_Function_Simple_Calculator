def incriment(x):
  return x+1

def decrement(x):
  return x-1

def sum(x,y):
  for i in range(y):
   x=incriment(x)
  return x

def minus(x,y):
  for i in range(y):
   x=decrement(x)
  return x

def times(x, y):
  result = 0
  for i in range(y):
    result = sum(result, x)
  return result

def power(x, y):
  result = 1
  for i in range(y):
    result = times(result, x)
  return result

def arith(x, y):
  print(x, '+', y, '=', sum(x, y))
  print(x, '-', y, '=', minus(x, y))
  print(x, '*', y, '=', times(x, y))
  print(x, '**', y, '=', power(x, y))






