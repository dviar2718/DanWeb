L = [100,42,-3]
print("Our List is {}".format(L))

for x in L:
    print("x is {}".format(x))
    if x > 50:
        print("Greater than 50")
    elif x > 40:
        print("Between 40 and 50")
    else:
        print("Less than 40")

"""
Our List is [100, 42, -3]
x is 100
Greater than 50
x is 42
Between 40 and 50
x is -3
Less than 40
"""