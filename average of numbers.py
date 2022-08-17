#average of number

#assign a variable called "total_number"and ask the user to enter how many number does he wants
total_number = int(input("enter how many numbers do you want: "))

#assign a variable called "sum" and assign a value as 0 to calculate the given number
sum = 0

#assign a for loop to run the n numbers one by one
for total_number in range(1,total_number+1):
    #assign a variable  "number" to allow the user to enter the number one by one
    number = int(input("enter the number: "))
    #as by the question if user enter the number "0" the program needs to stop so i assign a variable called invalid_number and assign the given value
    invalid_number = 0
    #if the user enter the invalid number it breaks the condition and stop running
    if(number == invalid_number):
        print("input stopped")
        break
    #otherwise it goes the else statement and calculate the number upto total number of the user
    else:
        sum += number
#finally it prints the average of total_number by dividing the "sum" and "total number"
print("average of number: ",sum/total_number)
