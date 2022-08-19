salesman_base_salary = 10000
commission_for_every_phone = 1000
extra_commission_for_every_phone = 100
minimum_sales = 5
average_sales = 9
maximum_sales = 13
maximum_commission = 15000
total_months_in_a_year = 12
double_the_extra_commission_for_after_ten_phones = 2
total_commission_gained = 0


for total_months_in_a_year in range (1,total_months_in_a_year + 1):
    month = int(input("enter the month: "))
    phone_sold_every_month = int(input("how many phones sold?: "))
    
    if( phone_sold_every_month > maximum_sales):
        print("you have reached your limit")
        
    elif( phone_sold_every_month <= minimum_sales):
        total_commission = ( phone_sold_every_month * commission_for_every_phone) 
        print(total_commission)
        total_commission_gained += total_commission

    elif( (phone_sold_every_month > minimum_sales ) and (phone_sold_every_month < average_sales ) ):
        average_sales -= minimum_sales
        total_commission = ( phone_sold_every_month * commission_for_every_phone)
        total_commission += ( average_sales ) * ( extra_commission_for_every_phone )
        print(total_commission)
        total_commission_gained += total_commission
        average_sales = 9

    elif((phone_sold_every_month >= average_sales ) and (phone_sold_every_month <= maximum_sales ) ):
        maximum_sales -= average_sales
        total_commission =  ( phone_sold_every_month * commission_for_every_phone)
        total_commission += ( maximum_sales ) * ( extra_commission_for_every_phone * double_the_extra_commission_for_after_ten_phones )
        total_commission += ( average_sales ) * ( extra_commission_for_every_phone )
       # total_commission += ( minimum_sales ) * ( extra_commission_for_every_phone)
        print(total_commission)
        total_commission_gained += total_commission
        maximum_sales = 12
        average_sales = 9 
          
    else:
        print("not a valid input")
        
print("total commission gained by the salesman: ",total_commission_gained)
average_salary_of_the_salesman = total_commission_gained / total_months_in_a_year
print("average_salary_of_the_salesman_in_one_year: ",average_salary_of_the_salesman)
print("monthly_salary_of_salesman: ",salesman_base_salary)