# sum_digits.py

print("WELCOME TO THE 'SUM DIGITS' PROGRAM!")
print("You provide two numbers.")
print("The program will compute their product.")
print("It will then compute the sum of the digits in the answer.")
print("Let's get started.")


def main():
    first_number = int(input("Please enter the first number: "))
    second_number = int(input("Please enter the second number: "))

    product = first_number * second_number

    print("The product is {0}".format(product))
    print("The first number contained {0} digits."
            .format(count_digits(first_number)))
    print("The second number contained {0} digits."
            .format(count_digits(second_number)))

    sum_of_digits = sum_digits(product)

    print("The sum of the digits in the product is {0}".format(sum_of_digits))
    print("Notice that {0}/9 is {1}".format(sum_of_digits, sum_of_digits/9))

# Function used to count the digits in a number
def count_digits(number):
    count = 0
    for digit in str(number):
        count = count + 1
    return count

# Function used to sum the digits in a number
def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum = sum + int(digit)
    return sum

# Start of the program
cont = "y"

while cont == "y":
    main()
    cont = input("Would you like to run the program again? y/n: ")
    print()
    cont = cont.lower()     #if 'n' is chosen, exits the module

# End of the program
print("Goodbye, thanks for using the sum digits program.")

"""
WELCOME TO THE 'SUM DIGITS' PROGRAM!
You provide two numbers.
The program will compute their product.
It will then compute the sum of the digits in the answer.
Let's get started.
Please enter the first number: 999999999
Please enter the second number: 444444444
The product is 444444443555555556
The first number contained 9 digits.
The second number contained 9 digits.
The sum of the digits in the product is 81
Notice that 81/9 is 9.0
Would you like to run the program again? y/n: y

Please enter the first number: 99999
Please enter the second number: 77777
The product is 7777622223
The first number contained 5 digits.
The second number contained 5 digits.
The sum of the digits in the product is 45
Notice that 45/9 is 5.0
Would you like to run the program again? y/n: n

Goodbye, thanks for using the sum digits program.
"""