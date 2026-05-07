# Keep asking the user for input until they enter a number between 1 and 10 and not a alphabet.

while True:
  user_input = input("Please enter a number between 1 and 10: ")
  if user_input.isdigit():
    number = int(user_input)
    if 1 <= number <= 10:
      print("Thank you for entering a valid number: ", number)
      break
    else:
      print("Invalid input. Please enter a number between 1 and 10.")
  else:
    print("Invalid input. Please enter a valid number.")