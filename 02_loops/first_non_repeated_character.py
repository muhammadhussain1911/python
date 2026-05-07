#  Given a string. Find the first non repeated character.
input_string = "PakpatanSharif"
string_name = input_string.lower()
for char in string_name:
  if string_name.count(char) == 1:
    print("First non repeated character is: ", char)
    break
