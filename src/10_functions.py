# is_even should return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


def is_even(givenNum):
    if (givenNum % 2 == 0):
        print("Even!")
    else:
        print("Odd")


is_even(num)
