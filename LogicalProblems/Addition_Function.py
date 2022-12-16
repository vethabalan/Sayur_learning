""" 
1. Write a function to add two numbers. Get user input (2 numbers) and use the function to add the numbers.
Print the result from the main code.
Hint - Funtion will take two input parameters and return one value.

"""
#Getting two numbers as input
First_Number = int(input("Enter Number One : "))
Second_Number = int(input("Enter Number Two : "))
#Defining a function to sum the inputs 
def Addition (Number_1,Number_2):
    #initializing a variable and adding two numbers
    Answer = First_Number + Second_Number
    #returning the answer to the function
    return Answer
#calling the function and printing the function
print("The Sum Of Adding Two Numbers is : ",Addition(First_Number,Second_Number))

""" 
Test Case - 1:

Enter Number One : 5
Enter Number Two : 5
The Sum Of Adding Two Numbers is :  10

"""
    