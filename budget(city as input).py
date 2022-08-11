city = input("enter the city:")                        #I take city as an input
if(city=="chennai"):                                   #If city is chennai it will enter into the statement
    onion=(int(input("onion rate:")))         #Getting all values in run time and print how much customer can buy with his budget
    tomato=(int(input("tomato rate:")))
    budget=(int(input("enter the budget:")))
    print("onion",budget/onion)
    print("tomato",budget/tomato)
    print("petrol expense",3/budget*budget)
    
elif(city=="madurai"):                             # if customer is in madurai it will go through this statement
    onion=(int(input("onion rate:")))
    tomato=(int(input("tomato rate:")))
    budget=(int(input("enter the budget:")))       # Getting all the values in run time and do the calculation and print the result
    print("onion",budget/onion)
    print("tomato",budget/tomato)
    print("petrol expense",3/budget*budget)
    
elif(city=="trichy"):                             # if customer is in madurai it will go through this statement
    onion=(int(input("onion rate:")))
    tomato=(int(input("tomato rate:")))
    budget=(int(input("enter the budget:")))     # Getting all the values in run time and do the calculation and print the result
    print("onion",budget/onion)
    print("tomato",budget/tomato)
    print("petrol expense",3/budget*budget)
    
    
else:
    print("invalid input")                        #if none of the city is entered it prints invalid input   