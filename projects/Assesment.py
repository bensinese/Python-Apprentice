# 1. Create 3 variables, 1 of each string, int, and Boolean

# 2. Write a loop that pritnts the numbers 1-100 exept for numbers that are divisible by 7

#3. Write a for loop that prints every other letter of the string you created in the 1st task


# 4.a create a function that takes in 2 arguements, both integers, and returns the sum of those two arguements

# 4.b call the function from task 4.a

my_str = "string"
num = 10
sigma = False

for x in range(1,101):
    if x % 7 == 0:
        print("")
    else:
        print(x)



 
 
 
 for x in my_str:
    print(my_str[x])


from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
num1 = simpledialog.askfloat("Give me a number", "Your Number") 

# Ask the user for the second number
num2 = simpledialog.askfloat("Give me another number", "Your second number") 

# Display the sum of the two numbers 
messagebox.showinfo("num1 + num2", str(num1 + num2))
# Keep the window open
window.mainloop()




for i in range(100)









 
