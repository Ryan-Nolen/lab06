#Ryan Nolen
def menu():
	print("Menu")
	print("-------------")
	print("1. Encode")
	print("2. Decode")
	print("3. Quit")


def encode():
	list_pass = []
	for i in password:
		list_pass.append(int(i))
	for j in range(len(list_pass)):
		list_pass[j] = list_pass[j] + 3
	return "".join(str(value) for value in list_pass)


def decode():
	list_pass = []
	for i in encoded_pass:
		list_pass.append(int(i))
	for j in range(len(list_pass[j] - 3
	return "".join(str(value) for value in list_pass)


while True:
	menu()
	option = int(input("Please enter an option: "))
	if option == 1:
		password = input("Please enter your password to encode: ")
		encoded_pass = encode()
		print("Your password has been encoded and stored!")
	elif option == 2:
		decoded_pass = decode()
		print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}")
	elif option == 3:
		break
