"""
input a string.print first and last char , add a comma , the print second and last but first char and so on.
input = abcd1234
output = a4 , b3 , c2 , d1
"""
word = input ("enter the word : ")
reverse_order = len(word) - 1
output = ""
for char in range ( 0 , len(word)):
    if(word[char] >= 'A' and word[char] <= 'Z' or word[char] >= 'a' and word[char] <= 'z'):
        print (word[char] + word[reverse_order] , end = " ")
    reverse_order -= 1
print()

"""
enter the word : abcd1234
a4 b3 c2 d1 

enter the word : vetha12345
v5 e4 t3 h2 a1 

"""