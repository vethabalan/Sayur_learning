""" 
4. Separate all even and odd numbers in one array into two different arrays. 
Find the max and min from each array. Do not use any built in functions.

"""

array_list = [15,9,7,5,8,6,4,3,2,1,13]
Even_list = []
Odd_list = []


for element in range(11):
    if array_list[element] % 2 != 0:
        Odd_list += [array_list[element]]
    else:
        Even_list += [array_list[element]]

for outer_element in range (0,len(Odd_list)):
    for inner_element in range(outer_element + 1,len(Odd_list)):
        if Odd_list[outer_element] <= Odd_list[inner_element]:
            temp = Odd_list[outer_element]
            Odd_list[outer_element] = Odd_list[inner_element]
            Odd_list[inner_element] = temp
            
for outer_element in range (0,len(Even_list)):
    for inner_element in range(outer_element + 1,len(Even_list)):
        if Even_list[outer_element] <= Even_list[inner_element]:
            temp = Even_list_list[outer_element]
            Even_list[outer_element] = Even_list[inner_element]
            Even_list[inner_element] = temp            

Odd_Maximum_Value = Odd_list[0]
Odd_Minimum_Value = Odd_list[len(Odd_list)-1]

Even_Maximum_Value = Even_list[0]
Even_Minimum_Value = Even_list[len(Even_list)-1]

print("Odd list : ",Odd_list)
print()
print("Even list : ",Even_list)
print()
print("Odd Max value : ",Odd_Maximum_Value)
print()
print("Odd Minimum Value : ",Odd_Minimum_Value)
print()
print("Even Maximum Value : ",Even_Maximum_Value)
print()
print("Even Minimum Value : ",Even_Minimum_Value)

""" 
Test Case-1:
 Odd list :  [9, 7, 5, 3, 1]

 Even list :  [8, 6, 4, 2]
Maximum value in the Odd list :  9

Minimum value in the Odd list :  1

Maximum Value in the Even List :  8

Minimum Value in the Even List :  2

Test Case-2:
Odd list :  [15, 13, 9, 7, 5, 3, 1]

Even list :  [8, 6, 4, 2]

Odd Max value :  15

Odd Minimum Value :  1

Even Maximum Value :  8

Even Minimum Value :  2

"""