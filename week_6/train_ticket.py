"""
calculate the cost of train tickets.Single one way ticket from madurai to chennai or vice versa
is ruppees 1000,Adding a return ticket will cost ruppees 750 extra.Fmaily of four members or more get 20% offer
senior grade will get 50% offer.

"""
#calculate the cost of train tickets
print("Welcome to APK Railway station ")
print("********************************")
print("Train Ticket Details")
#assigning variables according to the question mentioned above
ticket_cost_per_person = 1000
return_ticket_cost_per_person = 750
one_way_and_return_ticket_cost_per_person = 1750
#to calculate the total ticket cost 
total_ticket_cost = 0
#to calculate the passenger count
passenger_count= 1
#using while loop until passenger enter ther choice no
while (passenger_count > 0):
    #geeting the details from the user
    name = input("enter the name : ")
    age = int(input("enter the age : "))
    gender = input("enter the gender : ")
    #geeting the details of arrival and departure
    print("where do you want to go ? ")
    arrival = input("enter your arrival : ")
    departure = input("enter your departure : ")
    #this statement runs if the passenger age is above 60
    if(age >= 60):
        #calculate the senior offer and subtract the value from the ticket cost
        senior_offer =  ticket_cost_per_person // 2
        ticket_cost_per_person -= senior_offer
    #asking the user if they want a return ticket
    print("do you want return ticket ? : ")
    answer = input("enter the answer : ")
    #this if statement runs if the user type yes
    if(answer == "y"):
        total_ticket_cost += return_ticket_cost_per_person
    #if no this statement will run
    else:
        pass
    #asking the user if they have to book another ticket
    print("do you want to buy another ticket? : " )
    choice = input("enter your choice : ")
    #if yes this statement counts the passenger
    if( choice == "y"):
        passenger_count += 1
    #if no this statement will calculate the final ticket cost and break
    elif( choice == "n"):
        total_ticket_cost += ticket_cost_per_person * passenger_count
        print("total passengers : ",passenger_count)
        print("total ticket cost : ",total_ticket_cost) 
        break 
#if the passenger count is above than three this statement will execute
if(passenger_count >= 4):
    #asking the user if they're all are family members
    print("all are family members ? ")
    answer = input("enter the answer : ")
    #if the answer is yes it goes through this statement and gets 20% offer
    if(answer == "y"):
        family_offer = total_ticket_cost / 20
        total_ticket_cost -= family_offer
        print("total ticket cost is : ",total_ticket_cost)
        #if they're not a family this statement calculate the actual ticket cost
    elif(answer == "n"):
        total_ticket_cost = ticket_cost_per_person * passenger_count
        print("total ticket cost is : ",total_ticket_cost)
        breakpoint()
print("*********HAPPY JOURNEY**********")
        
        #TEST CASE:
"""
Welcome to APK Railway station 
********************************
Train Ticket Details
enter the name : vetha
enter the age : 20
enter the gender : male

where do you want to go ? 
enter your arrival : madurai
enter your departure : chennai

do you want return ticket ? :
enter the answer : n

do you want to buy another ticket? : 
enter your choice : y

enter the name : balan
enter the age : 60
enter the gender : male

where do you want to go ? 
enter your arrival : chennai
enter your departure : madurai

do you want return ticket ? : 
enter the answer : y

do you want to buy another ticket? : 
enter your choice : n
total passengers :  2
total ticket cost :  1750
*********HAPPY JOURNEY**********
    """