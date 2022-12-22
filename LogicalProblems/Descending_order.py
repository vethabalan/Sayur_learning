""" 
6. Sort and array with 10 elements in descending order. 
 (hint - you will be using two for loops. First find the largest number,
  then find the next largest number etc).
"""

Unsorted_Array = [ 7,6,5,9,1,4,3,2,8]
length_of_the_array = 9

for outer_element in range (0,length_of_the_array):
    for inner_element in range(outer_element + 1,length_of_the_array):
        if Unsorted_Array[outer_element] <= Unsorted_Array[inner_element]:
            Sorted_array = Unsorted_Array[outer_element]
            Unsorted_Array[outer_element] = Unsorted_Array[inner_element]
            Unsorted_Array[inner_element] = Sorted_array
First_largest_value = Unsorted_Array[0]       
Second_largest_value = Unsorted_Array[1]
print("Descending Order : ",Unsorted_Array)
print("First Largest Value : ",First_largest_value)
print("Second Largest Value : ",Second_largest_value)

"""
Test Case-1:
[9, 8, 7, 6, 5, 4, 3, 2, 1]
First Largest Value :  9
Second Largest Value :  8
"""