""" 
1. The cafe owner has his cafe's sales data in a file. The data is organized by day. It has 
 total amount of sales, and profit in each day of the month.
Find out which week the sales was high and which week it was low.

"""
#importing the csv module
import csv
#initailizing variable for import only the sales data from the file
Total_Sales = []
#initializing variables for import data from the file
week_1 = []
week_2 = []
week_3 = []
week_4 = []
#initializing variables for converting the string data types into integer data types
week_1_sales = []
week_2_sales = []
week_3_sales = []
week_4_sales = []
#initializing variables for calculating the total sales of every week
Total_week_1_sale = 0
Total_week_2_sale = 0
Total_week_3_sale = 0
Total_week_4_sale = 0

#opening the file and assigning a varible for the file
with open("CafeInput.csv",encoding="utf-8-sig") as csvfile:
    #assigning a variable to reading the file
    DataReader = csv.reader(csvfile)
    #assigning a variable to store all the data from the file into a list
    data = []
    #to skip the header
    skip = next(DataReader)
    #using for loop to import the data from the file
    for row in DataReader:
        data.append(row)
#using for loop for to import specific data from the list
for row in data:
    Total_Sales.append(row[1])

#using for loop to take data for specific week
for day in range (0,7):
    #taking the data from the list
    week_1.append(Total_Sales[day])
    #to convert the string into integer data type
    week_1_sales.append(int(week_1[day]))
    #calculating and week sales and storing it in a variable
    Total_week_1_sale += week_1_sales[day] 
#deleting the taken data from the main data
del Total_Sales[0:7]
#printing the week 1 daily sales
print("week 1 day sales: ",week_1_sales)
#printing the total sales of week 1
print("total sales of week 1 : ",Total_week_1_sale)

#using for loop to take data for specific week
for day in range (0,7):
    #taking the data from the list
    week_2.append(Total_Sales[day])
    #to convert the string into integer data type
    week_2_sales.append(int(week_2[day]))
    #calculating and week sales and storing it in a variable
    Total_week_2_sale += week_2_sales[day]
#deleting the taken data from the main data
del Total_Sales[0:7]
#printing the week 2 daily sales
print("week 2 day sales: ",week_2_sales)
#printing the total sales of week 2
print("total sales of week 2 : ",Total_week_2_sale)

#using for loop to take data for specific week
for day in range (0,7):
    #taking the data from the list
    week_3.append(Total_Sales[day])
    #to convert the string into integer data type
    week_3_sales.append(int(week_3[day]))
    #calculating and week sales and storing it in a variable
    Total_week_3_sale += week_3_sales[day]
#deleting the taken data from the main data
del Total_Sales[0:7]
#printing the week 3 daily sales
print("week 3 day sales: ",week_3_sales)
#printing the total sales of week 3
print("total sales of week 3: ",Total_week_3_sale)

#using for loop to take data for specific week
for day in range (0,7):
    #taking the data from the list
    week_4.append(Total_Sales[day])
    #to convert the string into integer data type
    week_4_sales.append(int(week_4[day]))
    #calculating and week sales and storing it in a variable
    Total_week_4_sale += week_4_sales[day]
#deleting the taken data from the main data
del Total_Sales[0:7]
#printing the week 4 daily sales
print("week 4 day sales: ",week_4_sales)
#printing the total sales of week 4
print("total sales of week 4 : ",Total_week_4_sale)

#using conditional statement to find the high sale week
if((Total_week_1_sale > Total_week_2_sale) and (Total_week_1_sale > Total_week_3_sale) and (Total_week_1_sale > Total_week_4_sale)):
    high_sale_week = "1"
elif ( (Total_week_2_sale > Total_week_1_sale) and (Total_week_2_sale > Total_week_3_sale) and (Total_week_2_sale > Total_week_4_sale)):
    high_sale_week = "2"
elif ( (Total_week_3_sale > Total_week_1_sale) and (Total_week_3_sale > Total_week_2_sale) and (Total_week_3_sale > Total_week_4_sale)):
    high_sale_week = "3"
else:
    high_sale_week = "4"

#using conditional statement to find the low sale week
if((Total_week_1_sale <  Total_week_2_sale) and (Total_week_1_sale < Total_week_3_sale) and (Total_week_1_sale < Total_week_4_sale)):
    low_sale_week = "1"
elif ( (Total_week_2_sale < Total_week_1_sale) and (Total_week_2_sale < Total_week_3_sale) and (Total_week_2_sale < Total_week_4_sale)):
    low_sale_week = "2"
elif ( (Total_week_3_sale < Total_week_1_sale) and (Total_week_3_sale < Total_week_2_sale) and (Total_week_3_sale < Total_week_4_sale)):
    low_sale_week = "3"
else:
    low_sale_week = "4"                

#creating a new csv file to display the output data                    
with open("OutputFile.csv","w") as csvfile:
    #initializing a variable to write the data
    WriteData = csv.writer(csvfile)
    #using the writing method to write the output data
    WriteData.writerow(("High Sale Week" , "Low Sale Week"))
    WriteData.writerow((high_sale_week,low_sale_week))
#to display the output
print(open("OutputFile.csv").read())
    