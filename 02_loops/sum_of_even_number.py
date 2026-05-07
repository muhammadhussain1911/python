# calculate the sum of even numbers up to a given number n;

number = 1000

even_numbers_sum = 0

for num in range(0, number+1):
  if num % 2 == 0:
    even_numbers_sum += num
  else:
    continue

print(even_numbers_sum)

