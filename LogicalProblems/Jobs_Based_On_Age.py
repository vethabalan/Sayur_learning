""" 
3. Write a function that returns if a person is a child (age 12 or below), Teen (age 13-19),
adult (20-65) or senior citizen (above 65). (Function should not do anything more than this)
Get the user's birthyear as input.
Based on the user's age group, decide what jobs they can do.
Hint (have a list of jobs for different age groups).

"""
#Defining a function to identify the age of the user
def Age_Group_Identifier():
    #using conditional statement to identify the age group
    if(User_Age <= Age_Limit_For_Child):
        return "Child"
    elif(User_Age > Age_Limit_For_Child) and (User_Age <= Age_Limit_For_Teen):
        return "Teen"
    elif (User_Age >= Senior_Citizen):
        return "Senior Citizen"
    #if not any of the above returns false
    else:
        return False
#Getting input from the user
Birth_Year = int(input('Enter your Birth Year : '))
#assinging a value of present year to calculate the age
Present_Year = 2022
#initializing a variable to Store the user age
User_Age = Present_Year - Birth_Year
#assigning age limit 
Age_Limit_For_Child = 12
Age_Limit_For_Teen = 19
Senior_Citizen = 65
#assigning job list according to the age limit
Jobs_for_Children = ["YouTuber","Child Artist"]
Jobs_for_Adults = ["YouTuber","Waiter"]
Jobs_for_Seniors = ["Gardener","Tailor"]
#storing the ouput of the age group identifier in a variable
User = Age_Group_Identifier()

#defining a function to find the job for the user
def Job_Finder():
    #using conditional statement to find the jobs for the user
    if(User == "Child"):
        print('Jobs for Children Is : ',*Jobs_for_Children)
    elif(User == "Teen"):
        print('Jobs for TeenAgers Is : ',*Jobs_for_Adults)
    elif(User == "Senior Citizen"):
        print('Jobs for Senior Citizen Is : ',*Jobs_for_Seniors)
    #if the age is not in the above conditions it will execute else statement
    else:
        print("Age is Between 20 to 64")
#Calling the function
Job_Finder()

""" 
Test Case-1:
Enter your Birth Year : 2015
Jobs for Children Is :  YouTuber Child Artist

Test Case-2:
Enter your Birth Year : 2005
Jobs for TeenAgers Is :  YouTuber Waiter

Test Case-3:
Enter your Birth Year : 1945
Jobs for Senior Citizen Is :  Gardener Tailor

Test Case-4:
Enter your Birth Year : 2002
Age is Between 20 to 64

"""