"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
numl = askinteger("Give me a number", "Your Number") 

# Ask the user for the second number
num2 = askinteger("Give me another number", "Your second number") 

# Display the sum of the two numbers 
messagebox.showinfo('The sum', "the sum is ", )

# Keep the window open
window.mainloop()
