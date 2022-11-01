#to display the menu
from tabulate import tabulate
#creating a list of menu
Menu = [["food_items","price_of_items"],
             ["vadai" ,"10"],[ "tea" ,"15"], ["chips","20" ]]
food_items = ["vadai" , "tea" , "chips"]
#creating  a list for cost
cost_of_items = [ 10,15,20 ]
#creating a list for supply
supply_of_items = [ 40,30,20 ]
#assigning variables for maximum transaction
max_transaction = 10
#assigning a variable to store the total sales of the cafe per day
total_sales = 0
#to know whether the shop is opened or closed
shop = input("type yes if shop is opened / type no if closed : ")
#if shop is closed it goes through this statement
if(shop == "no"):
    print("shop closed")
    exit()
#if opened it will execute
else:
    print("shop is opened")
    print("welcome")
#using tabulate i display the menu in a table
print(tabulate(Menu,headers = "firstrow",tablefmt="fancy_grid"))
#if customer is coming it will be true
customer = True
#this while is for checking the customer is coming
while(customer == True):
    #this for loop is run upto maximum transaction
    for customers in range(1,max_transaction+1):
        #this for loop is for customers to order the item they want
        for order in range(len(cost_of_items)):
            print("customer : ",customers)
            print("enter the food item : ")
            #getting the order from customer
            customer = input(food_items)
            #getting the quantity of the item from customer
            customer_quantity = int(input("enter the quantity : "))
            #calculating the order of the customer
            bill = customer_quantity * cost_of_items[order]
            #printing the customer bill
            print("customer bill : ",bill)
            #adding every customer bill to total sales
            total_sales += bill
            #decreasing the supply of items as customer buys
            supply_of_items[order] -= customer_quantity
            #if the customer asked quantity is less than the supply this condition execute
            if(customer_quantity > supply_of_items[order]):
                print("items is not available")
                break
            #asking the customer they want anything else
            user_choice = input("type yes if you want any other items / type no if done : ")
            #if no this will execute
            if(user_choice == "no"):
                    print("come and visit again")
                    break
            #if yes this will execute
            elif(user_choice == "yes"):
                    customer = input(food_items)
                    customer_quantity = int(input("enter the quantity : "))
                    bill = customer_quantity * cost_of_items[order]
                    print("cost : ",bill)
                    total_sales += bill
                    supply_of_items[order] -= customer_quantity
                    print(supply_of_items[order])
                    break
        #checking customer is are in or out
        customer = input(True or False)
        #asking the owner to continue the sales or not
        owner_choice = input("do you want to continue the sales: ")
        #if yes this condition will execute 
        if(owner_choice == "yes"):
            #checkimg the transaction is available
            if(max_transaction > max_transaction):
                print("maximum transaction has done")
                print(" cafe total sales of the day : ",total_sales)
        #atlast it displays the total sales and breaking the conditions
        else:
            print(" cafe total sales of the day : ",total_sales)
            break
    break
"""
TEST CASE:
type yes if shop is opened / type no if closed : yes
shop is opened
welcome
╒══════════════╤══════════════════╕
│ food_items   │   price_of_items │
╞══════════════╪══════════════════╡
│ vadai        │               10 │
├──────────────┼──────────────────┤
│ tea          │               15 │
├──────────────┼──────────────────┤
│ chips        │               20 │
╘══════════════╧══════════════════╛
customer :  1
enter the food item :
['vadai', 'tea', 'chips']vadai
enter the quantity : 10
customer bill :  100
type yes if you want any other items / type no if done : yes
['vadai', 'tea', 'chips']tea
enter the quantity : 5
cost : 50
25#remaining quantity
Truefalse
do you want to continue the sales: no
 cafe total sales of the day :  150

"""