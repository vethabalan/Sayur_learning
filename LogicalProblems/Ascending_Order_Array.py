""" 
5. Sort an array with 3 elements in ascending order.
"""

Unsorted_Array = [3,2,1]
length_of_the_array = 3

for outer_element in range (0,length_of_the_array):
    for inner_element in range(outer_element + 1,length_of_the_array):
        if Unsorted_Array[outer_element] >= Unsorted_Array[inner_element]:
            Sorted_array = Unsorted_Array[outer_element]
            Unsorted_Array[outer_element] = Unsorted_Array[inner_element]
            Unsorted_Array[inner_element] = Sorted_array
First_largest_value = Unsorted_Array[2]       
Second_largest_value = Unsorted_Array[1]
print("Ascending Order : ",Unsorted_Array)
print("First Largest Value : ",First_largest_value)
print("Second Largest Value : ",Second_largest_value)

""" 
Test Case-1:
[1, 2, 3]
First Largest Value :  3
Second Largest Value :  2
"""