#getting input from the user
user_word = input("Enter the word : ")
#assigning first letter of the  finding alphabet and second letter of finding alphabet true
First_answer , Second_answer = True,True
#declare a function to get the finding letter and print the between letters
def between_chars(user_word):
        #getting input of the finding alphabet
                Finding_Alphabet = input("enter the letter: ")
                #applying for loop to go through each characters to find the first alphabet
                for check in range (0,len(user_word)):
                        #once the first alphabet is true it will go through this statement
                        if(user_word[check] == Finding_Alphabet):
                                #assigning the first alphabet in first letter
                                first_letter = check
                                #making the first answer true because the word contains first finding alphabet
                                First_answer = True
                                break
                        #else make the first answer as false
                        else:

                                First_answer = False
                        
                #reversing a for loop to find the last index of finding alphabet
                for check in range(len(user_word)-1,first_letter,-1):
                        #if the word contains a last letter of finding alphabet it will go through this statement
                        if(user_word[check] == Finding_Alphabet):
                                #assigning a variable to store the last index of finding alphabet
                                second_letter = check
                                #and making it as true
                                Second_answer = True
                                break
                        #else false
                        else:
                                Second_answer = False
                #if the word contains both the first and last letters of finding alphabet it'll run the statement
                if(First_answer == True and Second_answer == True):
                        #printing the words between those finding alphabets
                        print("The words between findind letter is : ",user_word[first_letter + 1 : second_letter])
                #else it goes through this statement
                else:

                        print("there is no second letter")

                        between_chars(user_word)
#calling the function
between_chars(user_word)
""" 
TEST CASE 1:
Enter the word : abcdbdfcgjc
enter the letter: a
there is no second letter
enter the letter: b      
The words between findind letter is :  cd

TEST CASE 2:
Enter the word : bcdfghc
enter the letter: b
there is no second letter
enter the letter: c
The words between findind letter is :  dfgh

TEST CASE 3:
Enter the word : abcdefa
enter the letter: a
The words between findind letter is :  bcdef
"""
