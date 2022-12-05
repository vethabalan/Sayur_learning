""" 
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. 
If there are two or more words that are the same length, return the first word from the string with that length. 
Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

"""
#getting input 
InputString = input("enter the string : ")
#spliting the string into list
lststring = InputString.split()
#initializing a variable to check the length
maximum_length = 0
#using for loop to iterate through the elements
for element in lststring:
    #if the length of the element is higher than the maximum length it will execute
    if len(element) > maximum_length:
        #the length of the element is stored as the maximum length
        maximum_length = len(element)
        #the element will stored in this variable
        long_word = element
#printing the output
print("the longest word : ",long_word )


""" 
TEST CASE - 1
enter the string : i love code
the longest word :  love

TEST CASE -2 
enter the string : hello world welcome
the longest word :  welcome

"""
        
