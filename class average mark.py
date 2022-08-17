# Calculate the gpa of marks
#assign a variable called "student" to get the input of total students in the class
student = int(input("how many students in the class: "))
#assign a variable called "subject" to get the input of subjects taken by the students
subject = int(input("how many subject should students take: "))
#to calculate the total score assign a variable called "total"
total = 0
#to calculate the gpa assign a variable called "gpa"
gpa = 0
#to calculate the gpa of all students
total_gpa = 0
#to calculate the average of the class
average_mark = 0
#assign an outer for loop to allow the students one by one
for student in range(1,student+1):
    #assign an inner for loop to get the subjects one by one
    for subject in range(1,subject+1):
        #to get the marks assign a variable called "score"
        score = int(input("enter the score: "))
        print("student- ",student,"subject_ ",subject,"score- ",score)
        #to get the total score obtained by the student
        total += score
        gpa = total/subject
    #print the student's individual gpa
    print("student gpa: ",gpa)
    total_gpa += gpa
    total = 0
    gpa = 0
#to calculate the average mark of the class
average_mark=total_gpa/subject
print("average mark of class : ",average_mark)


        
