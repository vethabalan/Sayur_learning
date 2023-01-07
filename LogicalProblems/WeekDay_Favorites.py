import numpy as np
#Getting UserName as Input
UserName = input('Enter Your Name : ')
#Initializing the WeekDays Into a List Variable
WeekDays = ['Monday','Tuesday','Wednesday','Thrusday','Friday']
Favorite_Food_For_BreakFast = []
Food_List = []
#using for loops to print the output 
for Days in range(len(WeekDays)):
    #Getting the food list for weekdays from user
    Food = input("What do you like for BreakFast : ")
    #Initializing a variable to store the food list of the user for weekdays aftr splitting
    Food_List.append(Food)
#Getting the unique elements from the above list using numpy
Favorite_Food_For_BreakFast = np.unique(Food_List).tolist()
#printing the output
print(f'{UserName} likes {Favorite_Food_For_BreakFast} for breakfast')

""" 
Test Case-1:
Enter Your Name : Ram
What do you like for BreakFast : Idly
What do you like for BreakFast : Dosai
What do you like for BreakFast : Pongal
What do you like for BreakFast : Poori
What do you like for BreakFast : Aapam
Ram likes ['Aapam', 'Dosai', 'Idly', 'Pongal', 'Poori'] for breakfast
"""