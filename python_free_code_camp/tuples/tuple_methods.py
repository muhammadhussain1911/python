developer = ('Muhammad Hussain', 34, 'Rust Developer')

programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript' # TypeError: 'tuple' object does not support item assignment

developer = ('Muhammad Hussain', 34, 'Rust Developer')
developer[1] # 34

numbers = (1, 2, 3, 4, 5)
numbers[-2] # 4

numbers_1 = (1, 2, 3, 4, 5)
numbers_1[7] # IndexError: list index out of range

developer_1 = 'Muhammad Hussain'
tuple(developer_1) # ('M', 'u', 'h', 'a', 'm', 'm', 'a', 'd', ' ', 'H', 'u', 's', 's', 'a', 'i', 'n')

programming_languages_1 = ('Python', 'Java', 'C++', 'Rust')
'Rust' in programming_languages_1 # True
'JavaScript' in programming_languages_1 # False

developer_2 = ('Muhammad Hussain', 34, 'Rust Developer')
name, age, job = developer_2
print(name) # 'Muhammad Hussain'
print(age) # 34
print(job) # 'Rust Developer'

developer_3 = ('Muhammad Hussain', 34, 'Rust Developer')
name, *rest = developer_3
print(name) # 'Muhammad Hussain'
print(rest) # [34, 'Rust Developer']

desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3] # ('pie', 'cookies')

developer_4 = ('Muhammad Hussain', 23, 'Python Developer')
del developer_4[1] # TypeError: "tuple" object doesn't support item deletion