""" 

Do not use any built in functions. Use for/while loops as needed.
You can hard code an array with 10 or more  elements (numbers or strings as needed).

1. Find the average of numbers in an array.
"""
#assigning a variable a storing in a list
Numbers = [ 10,20,30,40,50]
#initialize a variable to store the sum of the elements in the list
Sum = 0
#Assigning a variable to store the length of the list
Length_of_The_List = 5
#using for loop to sum the elements of the list
for element in range(Length_of_The_List):
    #adding each element and storing it in sum variable
    Sum += Numbers[element]
    #finding the average by dividing the sum of the list and length of the list
    Average = Sum / Length_of_The_List
#printing the output
print("Average is : ",Average)

""" 
Test Case-1:
Average is :  30.0
"""