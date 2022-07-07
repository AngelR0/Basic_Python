# This file contains a little introduction to defining functions.

"""
Let's say we want to create a program that can be run in different files or called later.
We will need to create a function (`def`) to define the function.
Followed by the title of the function with open and close parenthesis and a colon.
Then we will add the body of the function by indenting it.
"""


def main():  # Defining function `main`
    # Indenting the body of the function
    print("Hello World!")
    name = input("What is your name? ")
    # This is another way to write and display a variable with a string.
    print("Nice to meet you " + name)


# An `if` statement is function to check a variable, hence the name `if`. If the variable (A) is variable (B), then execute
# This `if` statement asks if the 'name' of the file is (in our case) `__main__` it will run the function `main`
if __name__ == "__main__":
    # Must indent here as well
    main()

# This can be used as a its own program. Or can be used as a reusable module that can be called in different python programs.
