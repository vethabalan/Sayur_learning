""" 
1. Calculate the salary for the phone salesman. Base pay is Rs10000. 
Based on the years of experience of the saleman the basepay increses.
Rs 2000 will be added for each year of experience.
For every 10 phones sold, he gets 13% of the base pay as commission.

2. Same as above. For eacy day the salesman doesn't go to work, subtract Rs200 from the total pay.

3. Same as above, but there is a change in the way commission is calculated.
For the first 10 phones sold, commission is 13%, for the next 10 phones sold, it is 15%, 
and one percent increse for every 5 phones sold after that. 
(Hint -  write down the percent of commission for different number of phones sold and 
understand the problem,  before writing the  program)

 """
#Getting input from the SalesMan
Experience_Of_the_SalesMan = int(input('Year Of Experience : '))
#Getting the input of Leave taken by the SalesMan
Leave_Taken_by_The_SalesMan = int(input('Leave Days : '))
#Getting the Input of Phones Sold by the SalesMan
Phone_Sold_By_The_SalesMan = int(input('Phone Sold This Month : '))

#BasePay for all the SalesMan
Initial_BasePay_Of_SalesMan = 10000
#Salary Increment For Each Year
Increment_per_Year = 2000
#Loss Of Income For the SalesMan For One Day Leave
Pay_Cut_for_Leave_per_day = 200

#Assigning Variables for Each Phone Sold
Ten_Phones = 10
Twenty_Phones = 20
Twenty_Five_Phones = 25
Thirty_Phones = 30

#Assigning Variables for Commission Gained By the SalesMan
Commission_Gain_For_Ten_Phones_Sold = 0.13
Commission_Gain_For_Twenty_Phones_Sold = 0.15
Commission_Gain_For_Twenty_Five_Phones_Sold = 0.16

#Initializing a Variable for Increase Commission For Every Five Phones Sold After Twenty Five Phones
Phones_Need_To_Sale_for_One_Percent_Gain = 5

#Assigning a Variable to Store the individual Basepay of SalesMan
Actual_BasePay_Of_SalesMan = (Initial_BasePay_Of_SalesMan + ( Increment_per_Year * Experience_Of_the_SalesMan))
#Assigning a Variable to Store the Basepay Including Leave Cut 
Leave_Without_Pay_Of_The_SalesMan = (Actual_BasePay_Of_SalesMan - (Leave_Taken_by_The_SalesMan * Pay_Cut_for_Leave_per_day) )
#Assigned a Variable to Store the Final Salary of the SalesMan
Final_Pay_of_SalesMan = Leave_Without_Pay_Of_The_SalesMan

#This Condition Will Execute If Phones Sold are Above 10 and Below 15
if ( (Phone_Sold_By_The_SalesMan >= Ten_Phones) and (Phone_Sold_By_The_SalesMan < Twenty_Phones) ):
    #Assigning a Variable to Calculate the Commission for Above 10 Phones and below 10 Phones
    Commission_Gain = Final_Pay_of_SalesMan * Commission_Gain_For_Ten_Phones_Sold
    #Printing the Commission Gained by the SalesMan
    print("Commission For Phones Sold : ",Commission_Gain)
    #Adding the Commission amount with Final Pay Amount
    Final_Pay_of_SalesMan += Commission_Gain
    #Printing the Output
    print("Monthly Salary Of the SalesMan : ",Final_Pay_of_SalesMan)
    
#This Statement Will Execute If Phones Sold are Above 20 And Below 25    
elif (Phone_Sold_By_The_SalesMan >= Twenty_Phones) and (Phone_Sold_By_The_SalesMan < Twenty_Five_Phones):
    #Assigning a Variable to Calculate the Commission for Above 20 Phones and Below 25 Phones
    Commission_Gain = Final_Pay_of_SalesMan * Commission_Gain_For_Twenty_Phones_Sold
    #Printing the Commission Gained by the SalesMan
    print("Commission For Phones Sold : ",Commission_Gain)
    #Adding the Commission amount with Final Pay Amount
    Final_Pay_of_SalesMan += Commission_Gain
    #Printing the Output
    print("Monthly Salary Of the SalesMan : ",Final_Pay_of_SalesMan)
    
#This Statement Will Execute If Phones Sold are Above 25     
elif (Phone_Sold_By_The_SalesMan >= Twenty_Five_Phones):
    #This Statement Will Execute If Phones Sold are Above 25 And Below 30    
    if ( (Phone_Sold_By_The_SalesMan >= 25) and (Phone_Sold_By_The_SalesMan < Thirty_Phones) ):
        #Assigning a Variable to Calculate the Commission for Above 25 Phones and Below 30 Phones
        Commission_Gain = Commission_Gain_For_Twenty_Five_Phones_Sold * Final_Pay_of_SalesMan
        #Printing the Commission Gained by the SalesMan
        print("Commission For Phones Sold : ",Commission_Gain)
        #Adding the Commission amount with Final Pay Amount
        Final_Pay_of_SalesMan += Commission_Gain
        #Printing the Output
        print("Monthly Salary Of the SalesMan : ",Final_Pay_of_SalesMan)
        
    #This Statement Will Execute When Phones are Sold More than 29
    else:
        #Assigning a Variable to Calculate How Much Phones are Sold after 25 
        Commission_Calculation = Phone_Sold_By_The_SalesMan - Twenty_Five_Phones
        #With the above Variable Dividing the Phone need to be Sold to increase the Commission
        Commission_Increase = Commission_Calculation // Phones_Need_To_Sale_for_One_Percent_Gain
        #Assigning a variable and dividing the above value with 100 and adding with commission for twenty five phones
        Commission_Gain_After_Twenty_Five_Phones = Commission_Gain_For_Twenty_Five_Phones_Sold + (Commission_Increase / 100)
        #Printing the Commission Gained by the SalesMan
        print("Commission For Phones Sold : ",Commission_Gain_After_Twenty_Five_Phones)
        #Assigning the Variable to store the commission amount for Phone sold more than 29
        Commission_Gain = Final_Pay_of_SalesMan * Commission_Gain_After_Twenty_Five_Phones
        #Adding the Commission amount with Final Pay Amount
        Final_Pay_of_SalesMan += Commission_Gain
        #Printing the Output
        print("Monthly Salary Of the SalesMan : ",Final_Pay_of_SalesMan)
        
#This Statement Will Execute When Phones Sold are Below 10   
else:
    #Printing the Output
    print("Monthly Salary Of the SalesMan : ",Final_Pay_of_SalesMan)
"""   
Test Case - 1 :
    Year Of Experience : 2
    Leave Days : 1
    Phone Sold This Month : 14
    Commission For Phones Sold :  1794.0     
    Monthly Salary Of the SalesMan :  15594.0
    
Test Case - 2 :
    Year Of Experience : 2
    Leave Days : 1
    Phone Sold This Month : 24
    Commission For Phones Sold :  2070.0
    Monthly Salary Of the SalesMan :  15870.0
    
Test Case - 3 :
    Year Of Experience : 2
    Leave Days : 1
    Phone Sold This Month : 34
    Commission For Phones Sold :  0.17
    Monthly Salary Of the SalesMan :  16146.0
    
Test Case - 4 :
    Year Of Experience : 2
    Leave Days : 1
    Phone Sold This Month : 44
    Commission For Phones Sold :  0.19
    Monthly Salary Of the SalesMan :  16422.0
    
"""