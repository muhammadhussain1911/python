numbers = [1, -2, 3, 7, -8, -4, 5, -9, 0, 5, 8, -6];

count = 0;

for number in numbers:
  if number >= 0:
    count += 1
  else:
    continue
print(count);

