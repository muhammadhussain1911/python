# 1. Floor Division (How many full times it fits)
print(12.0 // 5.4)  # Output: 2.0

# 2. Modulus (The leftover remainder)
print(12.0 % 5.4)   # Output: 1.2 (approx due to float precision)
# If you ever want both floor division and the remainder at the same time, you can use Python's built-in divmod() function
print(divmod(12.0, 5.4))  # Output: (2.0, 1.1999999999999993)   