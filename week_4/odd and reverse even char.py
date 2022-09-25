"""
input a string . print all the index that are in odd index.
example : abcd output : bd
print all the characters that are in even index in reverse order
example - input : abcd output - ca
"""
word = input(" enter the word : ")
for odd_char in range (0, len(word) ):
    if(odd_char % 2 != 0):
        print("the odd character is : ",word[odd_char] )
for even_char in range ( len(word)-1 , -1 , -1):
    if(even_char % 2 == 0 ):
        print("the even character is : ",word[even_char] )
print()
"""
        
enter the word : abcd
the odd character is :  b
the odd character is :  d
the even character is :  c
the even character is :  a
        
        """