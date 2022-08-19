total_students = int(input("enter the total students: "))
female_students = int(input("how many female students: "))
online_class = 1
online_vote_count = 0
offline_class = 2
offline_vote_count = 0
mixed = 3
mixed_vote_count = 0
no_comment = 4
for female_student in range(1,female_students+ 1):
    student_choice = int(input("enter your choice: "))
    if(student_choice == no_comment):
        print("poll ended")
        break
    elif(student_choice == online_class):
        online_vote_count += online_class
    elif(student_choice == offline_class):
        offline_vote_count += offline_class
    elif(student_choice == mixed):
        mixed_vote_count += mixed
    else:
        print("not a valid input")
print("online_vote_count: ",online_vote_count)
percentage_of_online_class = ( online_vote_count/female_students ) * 100
print("percentage_of_online_class_among_female_students: ", percentage_of_online_class )

