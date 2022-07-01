# This file contains the file 'input' function
"""
To add an input for the user to interact with (from the terminal)
To allow the the user interacting with the code we need to create a variable (which in this case it contains the name of the user typed in.)
The function `input` goes in the beginning, followed by a parenthesis.
"""

# Everything inside the quotes is considered a string (in a `print` function it will displayed in the terminal).
print("Hello, what is your name?")
name = input()  # This is the `input` function which is set to the variable `name`
print(name)     # This displays whatever the user set the variable to.


"""
Now to make the code a little more simple, we can use the `input` function and add a string to it.
To display we can the `print` function with a string.
"""

# This is a new line. `\n` creates a new line. It must be placed inside quotation marks.
print("\n")
name = input("What is your name? ")
print("Hello,", name)
