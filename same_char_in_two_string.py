#print same characters in two different string
first_string = input("enter the word 1 : ")
second_string = input("enter the word 2 : ")
new_string = []
for first_word in range( 0, len(first_string )):
    for second_word in range ( 0,len (second_string)):
        if( ( first_string[first_word]) == (second_string[second_word]) ):
            new_string.append(first_string[first_word])
print(new_string)