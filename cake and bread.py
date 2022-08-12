# Calculate the profit of the bakery

#assigning variables for total quantity of cake and bread and getting the values
total_quantity_of_cake = int(input("total quantity of cake: "))
total_quantity_of_bread = int(input("total quantity of bread: "))

#assigning variables for cost price of the bread and cake and giving them values
cost_price_of_the_cake = int(input("cost price of the cake: "))
cost_price_of_the_bread = int(input("cost price of the bread: "))

#assigning variables for the total count of employees and input value for salary per day and calculate total salary for the employees and store it in a variable for later process
no_of_employees = int(input("employees working in the bakery: "))
employee_salary_per_day = int(input("salary of employee per day: "))
total_salary_for_employees = no_of_employees * employee_salary_per_day


#assign a variable to calculate the total cost for the bakery per day
total_cost_price_for_bakery_per_day = (total_quantity_of_cake*cost_price_of_the_cake) + (total_quantity_of_bread*cost_price_of_the_bread)
print("total cost price for bakery per day:",total_cost_price_for_bakery_per_day)


#assigning a variable to declare the selling price of the cake and bread 
selling_price_of_cake = int(input("selling price of the cake:"))
selling_price_of_bread = int(input("selling price of the bread:"))

#assign total selling price as 0 because we need to sum the cake and bread selling price with total selling price and assign them into it
total_selling_price = 0


#assign customer as variable to input the no.of.customers coming to the bakery per day
customers = int(input("customers coming to bakery per day: "))


#i assign a for loop to iterate through every customer one by one
for i in range(1,customers):

#using an if condition to check the quantity of cake and bread is not 0 
    if(total_quantity_of_cake>=0 or total_quantity_of_bread>=0):

#after customer enter into the shop employee asking the customer whether the customer want cake or bread
        print("employee")
        print("do you want cake or bread:")

#let the customer to choose what he/she wants?
        choice = input("cake or bread or both:")

#if the customer wants only cake it goes through this statement
        if(choice=="cake"):
#checking the cake is available or not
            if(total_quantity_of_cake > 0):
                cake = int(input("how many cakes do you want: "))                             #entering how many cake customer wants
                total_selling_price = total_selling_price + (cake*selling_price_of_cake)      #calculating the total cost for cake selling price
                total_quantity_of_cake = total_quantity_of_cake - cake                        #decrementing the cake quantity after customer buys
                print("cakes available: ",total_quantity_of_cake)                             #printing the available cake quantity

##if the customer wants only bread it goes through this statement
        elif(choice=="bread"):

#checking the bread is available or not
            if(total_quantity_of_bread > 0):                       
                bread = int(input("how many bread do you want: "))                             #entering how many bread customer wants
                total_selling_price = total_selling_price + (bread*selling_price_of_bread)     #calculating the total cost for bread selling price
                total_quantity_of_bread = total_quantity_of_bread - bread                      #decrementing the bread quantity after customer buys
                print("bread available: ",total_quantity_of_bread)                             #printing the available bread quantity
                

#if some customer want both cake and bread it goes through this statement
        elif(choice=="both"):
            if(total_quantity_of_cake>0 and total_quantity_of_bread>0):                        #using if condition to check the available quantity of cake and bread
                cake = int(input("how many cakes do you want: "))                              #entering how many cake customer wants
                bread = int(input("how many bread do you want: "))                             #entering how many bread customer wants
                

#calculating the total selling price of cake and bread and store it in the assigned variable
                total_selling_price = total_selling_price + (cake*selling_price_of_cake) + (bread*selling_price_of_bread)
                total_quantity_of_cake = total_quantity_of_cake - cake                         #decrementing the available cake quantity               
                total_quantity_of_bread = total_quantity_of_bread - bread                      #decrementing the available bread quantity
                print("cakes available: ",total_quantity_of_cake)                              #printing the available cake quantity      
                print("bread available: ",total_quantity_of_bread)                             #printing the available bread quantity

#if some customer wants other sweet items it goes through else statement
        else:
            print("item is not available")

#this else is used for stop the customer when products are sold out
    else:
        print("sold out of products")
        break
    
#giving salary to the employees from the selling price and print the total selling price
total_selling_price = total_selling_price - total_salary_for_employees
print("total_selling_price:",total_selling_price)

#printing the total cost price for the bakery per day
print("total_cost_price_for_bakery_per_day:",total_cost_price_for_bakery_per_day)

#assign a variable name "profit" and finding the difference between total selling price and total cost price for bakery per day
profit = total_selling_price - total_cost_price_for_bakery_per_day

#assign a variable name "loss" and finding the difference between total cost price for bakery per day and total selling price 
loss = total_cost_price_for_bakery_per_day - total_selling_price

#if profit is greater than loss it prints the profit 
if(profit>loss):
    print("profit:",profit)

#if profit is lesser than loss it prints loss     
else:
    print("loss:",loss)

        
