#calculate the sales of cafe

list_of_items = [ "vadai" , "sandwich" , "coke" , "cake", "bread" ]
cost_of_items = [ 5 , 20 , 10 , 40 , 25 ]
supply_of_items = [10 , 10 , 10 , 10 , 10 ]
total_cost_of_items = 0
maximum_transaction = 10
total_sale_of_the_day=0
for quantity in range (0,len(list_of_items)):
    print(list_of_items[quantity] + " " + str(cost_of_items[quantity]) + " " + str(supply_of_items[quantity]))
for customer in range (0,maximum_transaction):
    for order in range(0,len(list_of_items)):
        customer_order = int(input("how many " + str(list_of_items[order]) + " you want = "))
        total_cost_of_items += (cost_of_items[order]) * (customer_order)
        supply_of_items[order] -= customer_order
    print(supply_of_items)
    print("customer "+str(customer + 1) + "buys " + str(total_cost_of_items) + "rs" )
    total_sale_of_the_day += total_cost_of_items
print("total sales of the day ",total_sale_of_the_day)