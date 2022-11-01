"""
THere are two arrays of numbers. the numbers are sorted in ascending order. 
Find the numbers that are common in both arrays. 
Eg - array 1 = [1,3,7,9,13,14], array2 [1,2,7,13,15]. answer - [1,7,13]
"""
array_1 = [1,3,7,9,13,14,15] 
array_2 = [1,2,7,13,15,1,3]
same_element = []
for first_list in range(0,len(array_1)):
    for second_list in range(len(array_2)):
        if(array_1[first_list] == array_2[second_list]):
            #array_2[second_list] = array_1[first_list]
            #print(array_1[first_list])
            same_element.append(array_1[first_list])
            break
print(same_element)