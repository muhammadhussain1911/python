def multiple_args(**kwargs):
  result = []
  for key, value in kwargs.items():
    result.append(f"{key}: {value}")
  return result # return terminates the function, so the loop never continues to subsequent iterations, so we store all values in a list.
    

# print(multiple_args(name="Muhammad Hussain"))
# print(multiple_args(name="Muhammad Hussain", age= 23))
# print(multiple_args(name="Muhammad Hussain", age= 23, role="Software Developer"))
print(multiple_args())


# def multiple_args_1(**kwargs):
#   return [f"{key}: {value}" for key, value in kwargs.items()]

# print(multiple_args_1(name="Muhammad Hussain", age= 23))