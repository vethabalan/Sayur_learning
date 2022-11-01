""".vscode\
    sort the numbers in descending order
    """
#getting an array
My_List = [1,2,3,4,5]
#using selection sort running a nested for loop
#outer loop will keep the first element fixed
for outer_index in range(0,len(My_List)):
    #the inner loop will get compared with the outer loop element
    for inner_index in range(0, len(My_List)):
        #this condition will execute when first element is greater than than the second element
        # outer index = 2 > inner index = 1
        if ( My_List[outer_index] > My_List[inner_index]):
            #the first element is swapped to a temproary varialble 
            # 2 assigned to temp
            temp = My_List[outer_index]
            #the bigger element will stored in the outer index
            # 1 will assigned to next index
            My_List[outer_index] = My_List[inner_index]
            #the temproary variable is stored to the inner index
            #2 will assigned to first index
            My_List[inner_index] = temp
print(My_List)
"""
TEST CASE 1:
[1, 2, 3, 4, 5]
[2, 1, 3, 4, 5]
[3, 2, 1, 4, 5]
[4, 3, 2, 1, 5]
[5, 4, 3, 2, 1]
[5, 4, 3, 2, 1]
"""