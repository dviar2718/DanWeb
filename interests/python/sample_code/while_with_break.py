while True:
	print("Enter a multiple of 7 to exit.")
	response = input()
	if int(response) % 7 == 0:
		break

print('Goodbye.')

"""
Enter a multiple of 7 to exit.
12
Enter a multiple of 7 to exit.
45
Enter a multiple of 7 to exit.
14
Goodbye.
"""