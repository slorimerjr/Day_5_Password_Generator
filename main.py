#Password Generator Project
import random
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letters = ""
numbers = ""
symbols = ""

for letter in range(1, nr_letters + 1):
  letters += random.choice(letters_list)

for symbol in range(1, nr_symbols + 1):
  symbols += random.choice(symbols_list)

for number in range(1, nr_numbers + 1):
  numbers += random.choice(numbers_list)

password = letters + symbols + numbers

print(f"Here is your password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letters = ""
numbers = ""
symbols = ""
rand_pass = ""

for letter in range(1, nr_letters + 1):
  letters += random.choice(letters_list)

for symbol in range(1, nr_symbols + 1):
  symbols += random.choice(symbols_list)

for number in range(1, nr_numbers + 1):
  numbers += random.choice(numbers_list)

password = letters + numbers + symbols

pass_list = list(password)

final_pass = random.sample(pass_list, len(pass_list))

for elem in final_pass:
  rand_pass += elem

print(f"Your password is: {rand_pass}")