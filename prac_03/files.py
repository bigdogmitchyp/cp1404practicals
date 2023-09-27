"""
CP1404 Practical
Reading and writing files
"""

user_name = input("Name please: ")
out_file = open("name.txt", 'w')
print(user_name, file=out_file)
out_file.close()

in_file = open("name.txt", 'r')
name_string = in_file.readline()
print(f"Your name is {name_string.capitalize()}")
in_file.close()

in_file = open("numbers.txt", 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
print(first_number + second_number)
in_file.close()

in_file = open("numbers.txt", 'r')
sum_of_numbers = 0
for line in in_file:
    number = int(line)
    sum += number
print(sum)
in_file.close()
