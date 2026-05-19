#  print the multiplication table for a given number up to 10, but skip the 5th

number = 11;

multiplier = 10
for multiply in range(1, multiplier+1):
  if multiply==5: 
    continue
  else:
    print(f"{number} x {multiply} = {number * multiply}")


