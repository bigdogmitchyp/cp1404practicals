"""
CP1404 Practical
"""
numbers = []
for i in range(5):
    numbers.append(float(input("Number: ")))
print(f"The first number is {numbers[0]:.0f}")
print(f"The last number is {numbers[4]:.0f}")
print(f"The smallest number is {min(numbers):.0f} ")
print(f"The largest number is {max(numbers):.0f}")
print(f"The average of the numbers is {sum(numbers)/5:.1f}")

usernames = ['jimbo,' 'giltson98', 'derekf', 'WhatSup', 'NicholEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
