import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '-', '+']

num_alphabets = int(input("How many alphabets would you like? "))
num_numbers = int(input("How many numbers would you like? "))
num_symbols = int(input("How many symbols would you like? "))

password_list = []

for n in range(num_alphabets):
    letter = random.choice(alphabets)
    password_list.append(letter)

for n in range(num_numbers):
    number = random.choice(numbers)
    password_list.append(number)

for n in range(num_symbols):
    symbol = random.choice(symbols)
    password_list.append(symbol)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your random password is {password}")

