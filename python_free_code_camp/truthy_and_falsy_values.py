print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False
print(bool(None)) # False
print(bool(0.0)) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

# The and operator takes two operands and returns the first operand if it is falsy, otherwise, it returns the second operand. Both operands must be truthy for an expression to result in a truthy value.

is_citizen = True
age = 25

print(is_citizen and age) # 25

is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')


# Now let's take a look at the or operator. This operator returns the first operand if it is truthy, otherwise, it returns the second operand. An or expression results in a truthy value if at least one operand is truthy. The or operator is also known as a short-circuit operator
age = 19
is_employed = False

print(age or is_employed) # 19

age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

#  the not operator which takes a single operand and inverts its boolean value. It converts truthy values to False and falsy values to True. Unlike the previous operators we looked at, not always returns True or False.

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy