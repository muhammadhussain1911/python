#  check if the number is prime or not

user_input = input("Enter a number: ");
is_prime = True
if user_input.isdigit():
  number = int(user_input)
  if number > 1:
    for i in range(2, number):
      if (number % i) == 0:
        is_prime = False
        break

if(is_prime==True):
  print(number, "is prime")
else:
  print(number, "is composite")

