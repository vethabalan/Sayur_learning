#to pick the random word in my file
import random
#to display the color
from termcolor import colored

#this is uesd to start the game
print("welcome to wordle game")
print("guess the three letter word and press enter")
#this function is used to randomly pick any three letter word from my file
def display_random_word():
    #to open the file
    with open("word.txt") as f:
        #to read the file
        my_three_letter_word = f.read().splitlines()
        #to pick any one word from the file
        return random.choice(my_three_letter_word)
    
#the random word will stored in this variable
the_random_word = display_random_word()
#print(the_random_word)

def guessing_func(the_random_word):
    #user gets five attempts to guess the word
    for attempt in range ( 1,6):
        #user enter their guessed word and lower is used to accept all the 
        #words as lowercase letters
        guess = input("enter your guess : ").lower()
        
        #this for loop is used to run the attempts
        #this minimum length is used to identify the first alphabet in the given word
        #and run for next five orders
        for index in range (min(len(guess) , 5)):
            # if the guessed word is correct and in the correct position it prints the word
            if( guess[index] == the_random_word[index] ):
                # i use end function within the paranthesis because if it prints the word
                #and not to move on to the next line
                print(colored(guess[index] , 'green') , end = " ")  
            #if guessed word is in the wrong index it goes through this statement
            elif( guess[index] in the_random_word):
                print(colored(guess[index] , 'yellow') , end = " ")
            #if the whole word was wrong it goes through this statement
            else:
                print(colored(guess[index] , 'red') , end = " ")
                break
        #if we guess the whole word correctly it goes through this statement        
        if ( guess == the_random_word ):
            #this print function prints the message
            print(colored( "you won!" , 'blue') , end = " ")  
            break
guessing_func(the_random_word)

#asking the user to move on to next level
user_choice = input("do you want to move to the next level : " )
if(user_choice == "yes"):
    #this function is used to randomly pick any four letter word from my file
    def display_random_word():
        #to open the file
        with open("four_word.txt") as f:
            #to read the file
            my_four_letter_word = f.read().splitlines()
            #to pick any one word from the file
            return random.choice(my_four_letter_word)
    #the random word will stored in this variable
    the_random_word = display_random_word()
    print("guess the four letter word and press enter")
    guessing_func(the_random_word)
    #asking the user to move on to next level
    user_choice = input("do you want to move to the next level : " )

    #if "yes" it goes through this statement
    if(user_choice == "yes"):
        #this function is used to randomly pick any five letter word from my file
        def display_random_word():
            #to open the file
            with open("five_word.txt") as f:
                #to read the file
                my_five_letter_word = f.read().splitlines()
                #to pick any one word from the file
                return random.choice(my_five_letter_word)
        #the random word will stored in this variable
        the_random_word = display_random_word()
        print("guess the five letter word and press enter")
        guessing_func(the_random_word)
    elif(user_choice == "no"):
        print("game ended")

    
else:
    print("game ended")
    

"""
welcome to wordle game
guess the three letter word and press enter

enter your guess : any
a n y
enter your guess : ant
a n t  you won! 
do you want to move to the next level : yes


guess the four letter word and press enter
enter your guess : heal
h e a l  
you won! do you want to move to the next level : yes


guess the five letter word and press enter
enter your guess : needs
n e e d s  you won!

    """