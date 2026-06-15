def add_all(*args):
  return sum(args) # sum is default method of python

print(add_all(1, 2, 4, 5))

def mul_all(*args):
  mul = 1
  for i in args:
    mul *=i
  return mul # sum is default method of python

print(mul_all(1, 2, 4, 5))