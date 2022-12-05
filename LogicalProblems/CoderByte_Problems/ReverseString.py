""" 
Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
For example: if the input string is "Hello World and Coders" 
then your program should return the string sredoC dna dlroW olleH.

"""
#getting a string as input
InputString = input("enter the string : ")
#initializing a variable to store the output
ReverseString = " "
#initializing a variable to store the length
length = len(InputString)-1
#using the loop to iterate from downwards of the element
for reverse in range(length,-1,-1):
    #appending the index value in an empty string variable
    ReverseString += InputString[reverse]
#printing the output string
print("Output : ",ReverseString)

""" 
TEST CASE - 1
enter the string : Hello World
Output :   dlroW olleH

"""