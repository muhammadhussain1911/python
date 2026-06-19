my_int_1 = 56
my_int_2 = -4

print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints)

diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints)

product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints)

div_ints = my_int_1 / my_int_2
print('Division:', div_ints)

my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>

my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition)

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction)

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication)

float_division = my_float_2 / my_float_1
print('Float Division:', float_division)

my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints)
print('Float Modulo:', mod_floats)

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints)
print('Float Floor Division:', floor_div_floats)

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints)
print('Float Exponentiation:',  exp_floats)

my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))
print(converted_float, type(converted_float))

num = -15

absolute_value = abs(num)
print(absolute_value)

result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3