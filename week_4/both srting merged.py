"""
input two string . output is both string merged . 
example :
input1 = ABCD 
input2 = 1234

output = A1B2C3D4

"""
word_1 = input("enter the word_1 : ")
word_2 = input("enter the word_2 : ")
merged_string = " "
for index in range ( 0 , len(word_1)):
    merged_string += word_1[index] + word_2[index]
print("THE MERGED STRING : ",merged_string)

"""
enter the word_1 : ABCD
enter the word_2 : 1234
THE MERGED STRING : A1B2C3D4
"""