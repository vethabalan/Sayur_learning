#calculate the percentage of online class

#input of total students in a variable 
total_students = int(input("enter the total students: "))
#assigning a variable to take the input of female students
female_students = int(input("how many female students: "))
#voting has to be in number so assigning a value 1 for online class
online_class = 1
#to count the vote for online class
online_vote_count = 0
#assigning value 2 for offline class
offline_class = 2
#to count the vote for offline class
offline_vote_count = 0
#assigning value as 3 for mixed
mixed = 3
#to count the vote for mixed class
mixed_vote_count = 0
#assigning value as 4 for no opinion
no_comment = 4
#maximum vote is 10 as by the question
maximum_vote = 10
#run the for loop upto maximum no.of votes
for female_student in range(1,maximum_vote + 1):
    #input of vote by the students
    student_choice = int(input("enter your choice: "))
    #if anyone says no opinion it stop running
    if(student_choice == no_comment):
        print("poll ended")
        break
    #if student vote for online class this statement will run
    elif(student_choice == online_class):
        #it is used to calculate the online voting count
        online_vote_count += online_class
    #this statement will run for offline class
    elif(student_choice == offline_class):
        #it is used to calculate the offline voting count
        offline_vote_count += offline_class
    #this statement will run for mixed class
    elif(student_choice == mixed):
         #it is used to calculate the mixed voting count
        mixed_vote_count += mixed
    #if any student enter an invalid number it goes through else statement
    else:
        print("not a valid input")
#to print the total online vote count
print("online_vote_count: ",online_vote_count)
#calculating the percentage of online class
percentage_of_online_class = ( online_vote_count / maximum_vote ) * 100
#printing the percentage of online class
print("percentage_of_online_class_among_female_students: ", percentage_of_online_class )

