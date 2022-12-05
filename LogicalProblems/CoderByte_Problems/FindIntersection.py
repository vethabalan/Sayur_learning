""" 
Have the function FindIntersection(strArr) 
read the array of strings stored in strArr which will contain 2 elements: the first element will 
represent a list of comma-separated numbers sorted in ascending order, the second element will 
represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string 
containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, 
return the string false.

SAMPLE:

Input: ["1, 3, 4, 7, 13" , "1, 2, 4, 13, 15"]
Output: 1,4,13
"""
#first getting two seperate list
a = [ "1, 3, 4, 7, 13"]
b = [  "1, 2, 4, 13, 15"]
#intializing a list for input
input_lst = []
#initializing a variable for output
Intersection = []
#using loop for merge the two list
for i in range(len(a)):
    input_lst.append(*a)
    input_lst.append(*b)
print("Input list : ",input_lst)
#spliting the whole element into single element
lst1 = input_lst[0].split(",")
lst2 = input_lst[1].split(",")
print("After splitting : ",lst1)
print("After splitting : ",lst2)
#using loop for finding the same element in the two list using selection sort
for fixed_element in range(len(lst1)):
    for Unsort in range(len(lst2)):
        #if the index value is same between the two list it will execute the below statement
        if lst1[fixed_element] == lst2[Unsort]:
            #this statement will append the same element to the intersection list
            Intersection.append(lst1[fixed_element])
#printing the intersection list
print("InterSection : ",Intersection)

""" 
TEST CASE _ 1
Input list : [' 1,2,3,4,5 ', ' 1,7,3,9,5 ']
[' 1', '2', '3', '4', '5 ']
[' 1', '7', '3', '9', '5 ']
[' 1', '3', '5 ']

TEST CASE - 2
Input list : ['1, 3, 4, 7, 13', '1, 2, 4, 13, 15']
After splitting :  ['1', ' 3', ' 4', ' 7', ' 13']
After splitting :  ['1', ' 2', ' 4', ' 13', ' 15']
InterSection :  ['1', ' 4', ' 13']


"""

      
      

      