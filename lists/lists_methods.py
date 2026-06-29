cities = ['Los Angeles', 'London', 'Tokyo']
cities[0] # 'Los Angeles'
cities[-1] # 'Tokyo'
developer = 'Hussain'
list(developer) # ['H', 'u', 's', 's', 'a', 'i', 'n']

numbers = [1, 2, 3, 4, 5]
len(numbers) # 5

programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

developer1 = ['Jane Doe', 23, 'Python Developer']
del developer1[1]
print(developer1) # ['Jane Doe', 'Python Developer']

programming_languages_1 = ['Python', 'Java', 'C++', 'Rust']
'Rust' in programming_languages_1 # True
'JavaScript' in programming_languages_1 # False

developer_2 = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer_2[2] # ['Python', 'Rust', 'C++']

developer_3 = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer_3[2][1] # 'Rust'

developer_4 = ['Alice', 34, 'Rust Developer']
name, age, job = developer_4
print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

developer_5 = ['Alice', 34, 'Rust Developer']
name, *rest = developer_5
print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']

numbers_1 = [1, 2, 3, 4, 5, 6]
numbers_1[1::2] # [2, 4, 6]

numbers_3 = [1, 2, 3, 4, 5]
numbers_3.append(6)
print(numbers_3) # [1, 2, 3, 4, 5, 6]

numbers_4 = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers_4.extend(even_numbers)
print(numbers_4) # [1, 2, 3, 4, 5, 6, 8, 10]

numbers_5 = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers_5.extend(even_numbers)
print(numbers_5) # [1, 2, 3, 4, 5, 6, 8, 10]

numbers_6 = [1, 2, 3, 4, 5]
numbers_6.insert(2, 2.5)
print(numbers_6) # [1, 2, 2.5, 3, 4, 5]

numbers_7 = [10, 20, 30, 40, 50, 50]
numbers_7.remove(50)
print(numbers_7) # [10, 20, 30, 40, 50]

numbers_8 = [1, 2, 3, 4, 5]
numbers_8.pop(1) # The number 2 is returned
print(numbers_8) # [1, 3, 4, 5]

numbers_9 = [1, 2, 3, 4, 5]
numbers_9.clear()
print(numbers_9) # []

numbers_10 = [19, 2, 35, 1, 67, 41]
numbers_10.sort()
print(numbers_10) # [1, 2, 19, 35, 41, 67]

numbers_11 = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers_11)
print(numbers_11) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

numbers_12 = [6, 5, 4, 3, 2, 1]
numbers_12.reverse()
print(numbers_12) # [1, 2, 3, 4, 5, 6]

programming_languages_2 = ['Rust', 'Java', 'Python', 'C++']
programming_languages_2.index('Java') # 1

programming_languages_3 = ['Rust', 'Java', 'Python', 'C++']
programming_languages_3.index('JavaScript')