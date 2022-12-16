""" 
2. Write a function that returns if a food is a healthy food or not. 
 Funtion will take one food item as input. It will return True or false. It will have a list 
 of healthy foods. Name the function appropriately.
 From the main code, ask the user about his/her breakfast. Print if it is a healthy breakfast or not.
 
"""
#Getting input from the user
Favorite_BreakFast = input('What do you like for breakfast : ')
#assigning a list of healthy foods
Healthy_Food_List = [ 'Green Veggies' , 'Oats' , 'Grain Porridge']
#Defining a function to check the food is healthy or not
def CheckYourFood (Food):
    #using a conditional statement to check the input food is in the list
    if Food in Healthy_Food_List:
        #returns true
        return True
    #returns false
    else:
        return False
#printing the output
print('Ouput : ',CheckYourFood(Favorite_BreakFast))

""" 
Test Case-1:
What do you like for breakfast : Oats
Ouput :  True

Test Case-2:
What do you like for breakfast : Pizza
Ouput :  False
"""