#calculate the cost of snack for a customer
#assigning variables for available items and fixing the cost for each items
price_of_coffee = 100
price_of_vadai = 100
price_of_sandwich = 200
price_of_coke = 60
#assigning variable for discount value
discount = 20

#creating a menu for the customers
menu = ["1.coffee = 100" , "2.sandwich = 200" , "3.vadai = 100" , "4.coke = 60" ]
print(*menu, sep = "\n")

#creating variables for the input of items of the customers
coffee_quantity = int(input("coffee quantity: "))
vadai_quantity = int(input("vadai quantity: "))
sandwich_quantity = int(input("sandwich quantity: "))
coke_quantity = int(input("coke quantity: "))


#for coffee offer , if statement is created to check the quantity of sandwich or vadai is satisfies the condition
#why i'm apply the coke condition is because whether the customer buy one coke it automatically goes to elif statement
#this condition only satisfied for whether vadai or sandwich quantity is greater than the offer and also not all items are purchased

if( (( sandwich_quantity > 1 ) or ( vadai_quantity > 2 )) and (coke_quantity == 0)) :
    #assigning cost of coffee as 50
    
    coffee = 50
    
    #adding all the purchased item and store it as bill
    
    bill = (sandwich * sandwich_quantity) + (vadai * vadai_quantity) + (coffee * coffee_quantity) + (coke * coke_quantity)
    
    #printing the bill
    print("bill on offer for coffee: ",bill)
    
#this elif statement is for whether the customer buys each one of every item this condition will run
elif( ( sandwich_quantity >= 1) and ( coke_quantity >= 1 ) and ( vadai_quantity >= 1 ) and ( coffee_quantity >= 1) ):
    
    #adding all the purchased item and store it as bill
    bill = (sandwich * sandwich_quantity) + (vadai * vadai_quantity) + (coffee * coffee_quantity) + (coke * coke_quantity)
    
    #for this statement we need to discount 20% from the total bill amount
    #assign offer as variable to calculate the discount amount
    offer = (bill/100) * discount
    
    #subtract the discount from total bill amount 
    bill -= offer
    
    #print the final offer bill
    print("bill on offer for each one of item: ",bill)
    
#this elif condition satisfies only if the customer had purchase any items and not satisfies the above two statements
elif((sandwich_quantity >= 0 ) and (vadai_quantity >= 0) and (coffee_quantity >= 0) and ( coke_quantity >= 0)):
    
    ##adding all the purchased item and store it as bill
    bill = (sandwich * sandwich_quantity) + (vadai * vadai_quantity) + (coffee * coffee_quantity) + (coke * coke_quantity)
    
    #if the total amount of the above statement is greater than 1000 this statement will run
    if(bill > 1000):
        
        #for this statement we need to discount 20% from the total bill amount
        offer = (bill/100) * discount
        
        #subtract the discount from total bill amount
        bill -= offer
        
        #print the final offer bill
        print("discount for over 1000: ",bill)
        
    #else the above total bill is lesser than 1000 it prints the actual bill
    else:
        print("actual bill: ",bill)


print("Thank you")
