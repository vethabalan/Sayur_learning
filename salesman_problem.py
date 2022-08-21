# calculate the salesman average salary and base salary

#assigning variable for salesman base salary
salesman_base_salary = 10000
#his commission for every phone he sells
commission_for_every_phone = 1000
#extra commission for over five phones 
extra_commission_for_every_phone = 100
#these three variables are used to calculate the extra commisssion for every five phones he sells
minimum_sales = 5
#in average sales he earns extra 100 over commission
average_sales = 9
#in maximum sales he earns extra 200 over commission
maximum_sales = 13
#his maximum earning is 25000 include base salary
maximum_commission = 15000
#to calculate the average for one year
total_months_in_a_year = 12
#this variable is used to double the extra commission after ten phones
double_the_extra_commission_for_after_ten_phones = 2
#to calculate the total commission in one year
total_commission_gained = 0

#run the for loop upto 12 months
for total_months_in_a_year in range (1,total_months_in_a_year + 1):
    #entering the month one by one
    month = int(input("enter the month: "))
    #input of phones he sold every month
    phone_sold_every_month = int(input("how many phones sold?: "))
    
    #he only sale 13 phone per month or else his commission will above than 15000
    if( phone_sold_every_month > maximum_sales):
        print("you have reached your limit")
    
    #this condition will satisfy only when the phones are sold less than the minimum sales    
    elif( phone_sold_every_month <= minimum_sales):
        total_commission = ( phone_sold_every_month * commission_for_every_phone) 
        print(total_commission)
        #total commission is added to total commission gained to calculate overall commission
        total_commission_gained += total_commission
    
    #this condition is for 6 to 9 phones to calculate the extra commission
    elif( (phone_sold_every_month > minimum_sales ) and (phone_sold_every_month < average_sales ) ):
        #to calculate 100 for over 5 phones and less than 10 phones 
        average_sales -= minimum_sales
        total_commission = ( phone_sold_every_month * commission_for_every_phone)
        total_commission += ( average_sales ) * ( extra_commission_for_every_phone )
        print(total_commission)
        total_commission_gained += total_commission
        #apply the original value at the end of the statement
        average_sales = 9
    #this condition is for 10 to 13 phones to calculate the extra commission
    elif((phone_sold_every_month >= average_sales ) and (phone_sold_every_month <= maximum_sales ) ):
        #to calculate extra commission 100 double time for over 10 phones
        maximum_sales -= average_sales
        total_commission =  ( phone_sold_every_month * commission_for_every_phone)
        total_commission += ( maximum_sales ) * ( extra_commission_for_every_phone * double_the_extra_commission_for_after_ten_phones )
        total_commission += ( average_sales ) * ( extra_commission_for_every_phone )
        print(total_commission)
        total_commission_gained += total_commission
        #apply the original value at the end of the statement
        maximum_sales = 12
        average_sales = 9 
          
    else:
        print("not a valid input")
#adding all the commission and printing the total commission for one year        
print("total commission gained by the salesman: ",total_commission_gained)
#to calculate the average commission of the salesman per month
average_salary_of_the_salesman = total_commission_gained / total_months_in_a_year
#printing the average salary and base salary of the salesman
print("average_salary_of_the_salesman_in_one_year: ",average_salary_of_the_salesman)
print("monthly_salary_of_salesman: ",salesman_base_salary)