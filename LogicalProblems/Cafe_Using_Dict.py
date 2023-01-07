""" 
purpose : to find the efficient method to run the code.
you have a cafe.cafe has a manager 
first input
ask the manger how many dishes they have 
each dishes has how much quantities?
second data
today sales of the cafe for each dishes
third input
To owner
what information do you want?
how much quantities sold for a specific dish or remaining quantity of the dish?

"""
# #initializing a variable and store all the details of the cafe in a dictionary
# Cafe_dishes_and_quantities = { 'vadai':{'quantity' : 50 , 'total sales ': 250 , 'remaining quantity' : 5},
#                             'tea':{'quantity' : 50, 'total sales ': 250 , 'remaining quantity' : '2 litres'},
#                             'idly':{'quantity' : 50, 'total sales ': 500 , 'remaining quantity' : 0},
#                             'dosai':{'quantity' : 50, 'total sales ': 1200 , 'remaining quantity' : 9},
#                             'poori':{'quantity' : 50, 'total sales ': 1250 , 'remaining quantity' : 14},
#                             'pongal':{'quantity' : 50, 'total sales ': 1250 , 'remaining quantity' : 14}}
#creating a empty dictionary
Cafe_dishes_and_quantities = {}
#input of total number of dishes available
Total_cafe_items = int(input('enter the total dishes in the cafe : '))

#using for loop to create a dynamic dictionary
for key in range(Total_cafe_items):
    #all inputs for the dictionary
    Dish = input('enter the dish : ')
    Total_quantity = int(input('enter the total quantity : '))
    Total_sales = int(input('enter the total sales of the dish : '))
    Remaining_quantity = int(input('enter the remaining quantity of the dish : '))
    #updating the dictionary
    Cafe_dishes_and_quantities.update({Dish : {'Total_quantity' : Total_quantity,'Total_sales':Total_sales,'Remaining_quantity':Remaining_quantity}})
#printing the dictionary
print(Cafe_dishes_and_quantities)

#initiailizing a variable for the owner and giving a boolean value
owner = True

#using while loop to run the program until the owner get his information
while owner == True:
    #get the input from owner
    Owner_question = input('Which information do you Want : ')
    
    #this condition will execute for today available dishes
    if Owner_question == 'i want the details of today dishes':
        print(Cafe_dishes_and_quantities.keys())
        
     #this condition will execute for total quantity of the dishes   
    elif Owner_question == 'i want the dish quantity':
        #getting the specific dishes
        dish = input('which dish quantity do you want? : ')
        #assigning a variable for empty list
        dishes = []
        #splitting the specific dishes and store it in the empty list
        dishes = dish.split(',')
        #using for loop to get the specific details of the dishes
        for item in dishes:
            #if the dish is in the cafe it will execute
            if  item in Cafe_dishes_and_quantities:
                print('Total quantity of the',item,': ',Cafe_dishes_and_quantities[item]['Total_quantity'])
            #else this will execute
            else:
                print('entered dish is not sell today')
                continue
        
    #this condition is for the total sales   
    elif Owner_question == 'i want the total sales':
        dish = input('which dish sales do you want? : ')
        dishes = []
        dishes = dish.split(',')
        for item in dishes:
            if  item in Cafe_dishes_and_quantities:
                print('total sales of the', item ,':',Cafe_dishes_and_quantities[item]['Total_sales'])
            else:
                print('entered dish is not sell today')
                continue
        
    #this condition is for the remaining quantity  
    elif Owner_question == 'i want the details of remaining quantity':
        dish = input('which dish remaining quantity do you want? : ')
        dishes = []
        dishes = dish.split(',')
        for item in dishes:
            if  item in Cafe_dishes_and_quantities:
                print('remaining quantity of the', item ,': ',Cafe_dishes_and_quantities[item]['Remaining_quantity'])
            else:
                print('entered dish is not sell today')
                continue
            
    #if the owner gets enough information assigning owner variable as false    
    else:
        owner = False


""" 
TEST CASE-1 : 

Which information do you Want : i want the details of remaining quantity
which dish remaining quantity do you want? : vadai,tea,dosai,poori
remaining quantity of the vadai :  5
remaining quantity of the tea :  2 litres
remaining quantity of the dosai :  9
remaining quantity of the poori :  14
Which information do you Want : none

TEST CASE-2 : 

Which information do you Want : i want the total sales
which dish sales do you want? : tea,vadai,poori
total sales of the tea : 250
total sales of the vadai : 250
total sales of the poori : 1250
Which information do you Want : i want the dish quantity
which dish quantity do you want? : dosai,idly,pongal
Total quantity of the dosai :  50
Total quantity of the idly :  50
Total quantity of the pongal :  50
Which information do you Want : none



DYNAMIC DICTIONARY : 

TEST CASE-1:
enter the total dishes in the cafe : 2
enter the dish : tea
enter the total quantity : 20
enter the total sales of the dish : 200
enter the remaining quantity of the dish : 2

enter the dish : dosai  
enter the total quantity : 50
enter the total sales of the dish : 1250
enter the remaining quantity of the dish : 4

{'tea': {'Total_quantity': 20, 'Total_sales': 200, 'Remaining_quantity': 2}, 'dosai': {'Total_quantity': 50, 'Total_sales': 1250, 'Remaining_quantity': 4}}

Which information do you Want : i want the total sales
which dish sales do you want? : dosai,tea
total sales of the dosai : 1250
total sales of the tea : 200

Which information do you Want : i want the details of remaining quantity
which dish remaining quantity do you want? : tea,dosai
remaining quantity of the tea :  2
remaining quantity of the dosai :  4

Which information do you Want : i want the details of today dishes
dict_keys(['tea', 'dosai'])

Which information do you Want : i want the dish quantity
which dish quantity do you want? : tea,dosai
Total quantity of the tea :  20
Total quantity of the dosai :  50

Which information do you Want : none


"""