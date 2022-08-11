#wedding expenses

lunch_cost_per_person = int(input("cost per person for lunch: "))         #taking input for lunch cost per person
breakfast_cost_per_person = lunch_cost_per_person//2                      #calculating the breakfast cost per person by dividing with lunch cost per person by half
hall_cost_per_person = lunch_cost_per_person//3                           #calculating hall cost per person by dividing one third of the lunch cost per person
decoration_cost_per_person = hall_cost_per_person//2                      #calculating decoration cost per person by dividing with hall cost per person
parking_cost = decoration_cost_per_person//10                             #calculating the parking cost per person with one by tenth of decoration cost per person


#input of guest coming to the wedding
total_guest = int(input("how many guest: "))                              
total_lunch_cost = total_guest * lunch_cost_per_person                    #calculating total lunch cost per person with the input of guest
total_breakfast_cost = total_guest * breakfast_cost_per_person            #calculating total breakfast cost per person with the input of guest                     
total_hall_cost = total_guest * hall_cost_per_person                      #calculating total hall cost per person with the input of guest
total_decoration_cost = total_guest * decoration_cost_per_person          #calculating total decoration cost per person with the input of guest


#not all guests are coming by their own vechicles so we need to take it as a input
guest_coming_by_vehicles = int(input("guest comig by vechicles:"))         
total_parking_cost = guest_coming_by_vehicles * parking_cost              #then we calculate the parking cost per person with guest coming by vechicles

 #printing all the total cost of lunch,breakfast,hall,decoration,parking individually
print("total_lunch_cost:",total_lunch_cost)                               
print("total_breakfast_cost:",total_breakfast_cost)
print("total_hall_cost:",total_hall_cost)
print("total_decoration_cost:",total_decoration_cost)
print("total_parking_cost:",total_parking_cost)

#calculating total cost for the wedding by adding all the wedding expenses
total_cost_for_wedding = total_lunch_cost + total_breakfast_cost + total_hall_cost + total_decoration_cost + total_parking_cost

print("total_cost_for_wedding:",total_cost_for_wedding)

#we want know the savings of the bride to calculate whether she has to apply for loan
bride_savings = int(input("savings by bride:"))

#applying if condition to check the total cost of wedding is greater than the bride savings

if(total_cost_for_wedding > bride_savings):             #if wedding expense is higher than the savings we need to know the difference between total cost of wedding and bride savings  

    loan_needed = total_cost_for_wedding - bride_savings   #assign the value to the loan needed variable and print how much loan does she need?
    print("loan_needed:",loan_needed)
else:

    print("loan_not_needed")                             #if total cost is lesser than the savings print loan not needed