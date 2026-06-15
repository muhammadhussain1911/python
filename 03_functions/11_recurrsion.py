def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    print(f"Calculating factorial({n})")
    return n * factorial(n - 1)
  
print(factorial(5)) # 120
# print(factorial(0)) # 1