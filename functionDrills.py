'''
@author: amayamunoz
'''
from Tools.i18n.makelocalealias import print_differences

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subract_two_numbers(num1, num2):
    differenceOfNums = num2-num1
    return differenceOfNums
x = subract_two_numbers(9,5)
print(x)
#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def divide_multiply_add_four_numbers(num1,num2,num3,num4):
    productOfNums = num1 / num2 * num3 + num4
    return productOfNums
x = divide_multiply_add_four_numbers(4,2,77,10000)
print(x)
#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def check_two_numbers(num1,num2):
    if num1 == num2:
        return "True"
    else:
        return "False"
x = check_two_numbers(3,3)
print(x)
    
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def larger_number(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return None
x = larger_number(10,20)
print(x)
        
#5) Define a function that takes in two words and returns a string that contains both words combined.
def add_two_strings(string1, string2):
    sumOfStrings = string1 + string2
    return sumOfStrings
x = add_two_strings("Hi","World")
print(x)
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def check_three_numbers(num1,num2,num3):
    if num1 == num2 or num3:
        return "True"
    else: 
        return "False"
x = check_three_numbers(9,20,9)
print(x)
#7) Define a function that prints your name.
def my_name(string1):
    sumOfStrings = string1
    return sumOfStrings
x = my_name("Sophia")
print(x)
    
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def my_favorite_color(string1, string2):
    if string1 == string2:
        return "That's my favorite color1"
    else:
        return "That's not my favorite color. Try Again."
x = my_favorite_color("red", "yellow")
print(x)
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def equality_of_two_numbers(num1,num2):
    while num1 < num2:
        return num2
x = equality_of_two_numbers(0,5)
print(x)
 
#10) Create your own function that solves any problem you can think of.
def what_is_my_name(string1, string2):
    if string1 == string2:
        return "Yes, that's my name!"
    else:
        return "No, that's not my name."
x = what_is_my_name("Sophia", "Angela")
print(x)