#importing numpy module
import numpy as np
#Getting the Name of the user 
UserName = input('Enter Your Name : ')
#assigning empty list for storing the datas later
BreakFast_Food_List = []
Dinner_Food_List = []
Unique_BreakFast_List = []
Unique_Dinner_List = []
#assigning a list of weekdays to run the for loop
WeekDays = ['Monday','Tuesday','Wednesday','Thrusday','Friday']
#using for loop to ask the user each day an input of breakfast and dinner
for Element in range(len(WeekDays)):
    #Asking the input from the user 
    BreakFast = input('What do you like for BreakFast : ')
    Dinner = input('What do you like for Dinner : ') 
    #moving the input to the empty list using append method
    BreakFast_Food_List.append(BreakFast)
    Dinner_Food_List.append(Dinner)
#Using numpy's unique method to move the individual datas to the unique list
Unique_BreakFast_List = np.unique(BreakFast_Food_List).tolist()
Unique_Dinner_List = np.unique(Dinner_Food_List).tolist()
#printing the output
print(f'{UserName} likes {Unique_BreakFast_List} for BreakFast')   
print(f'{UserName} likes {Unique_Dinner_List} for Dinner')  

""" 
Test Case-1:
Enter Your Name : Ram
What do you like for BreakFast : Idly
What do you like for Dinner : Chapathi
What do you like for BreakFast : Dosai
What do you like for Dinner : Chapathi
What do you like for BreakFast : Idly
What do you like for Dinner : Poori
What do you like for BreakFast : Dosai
What do you like for Dinner : Aapam
What do you like for BreakFast : Pongal
What do you like for Dinner : Aapam
Ram likes ['Dosai', 'Idly', 'Pongal'] for BreakFast
Ram likes ['Aapam', 'Chapathi', 'Poori'] for Dinner

"""