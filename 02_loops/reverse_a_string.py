#  Reverse a string using a loop;

full_str = "abcdefghijklmnopqrstuvwxyz"
reversed_full_str = ""
for str in full_str:
  reversed_full_str = str + reversed_full_str

print(reversed_full_str)