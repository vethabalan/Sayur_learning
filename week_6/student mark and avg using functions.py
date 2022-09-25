"""
write an app to calculate grades for student in each subject.mark > 90 is A,>80 is B,>70 is C,>=60 is D.Anything less than 60 is fail.
write a function that returns the grade for one subject for all the student in the class.Also,print the class average grade.
"""
#input of total students in the class
total_students = int(input("enter the total students : "))
#input of total subjects taken by the students
total_subjects = int(input("total subjects : "))
#assigning an empty list to store the total subjects of marks
marks = []
#fixing the max mark
maximum_mark = 100
#fixing the grade points mentioned above
A = 90
B = 80
C = 70 
D = 60
#to calculate the particular mark of one subject of the whole class
total_marks = 0
mark = 0
#defining a function to calculate the grade of each subject and average grade
def students_grade (mark):
    #this if statement wil not run if maximum mark is above than 100 it goes to else statement
    if(mark <= maximum_mark):
                if(mark >= A ):
                    print("the grade is A")
                elif(mark >= B ):
                    print("the grade is B")
                elif(mark >= C ):
                    print("the grade is C")
                elif(mark >= D ):
                    print("the grade is D")
                else:
                    print("Fail")
    else:
        print("invalid mark")
        #if invalid mark is entered it asks the user to enter the valid mark
        mark = int(input("enter the correct mark : "))
        #we call the the function to find the grade for the correct mark
        students_grade(mark)
#this nested for loop is used to get the input of students and their subjects
for subject in range ( 0,total_subjects ):
    print("subject" + str(subject + 1) )
    for index in range (0 , total_students):
            #marks are stored in the empty list
            marks.append(int(input("enter the mark of student " + str ( index + 1 )  + "scored : ")))
            #this mark variable is used for calculate each index grade
            mark = marks[index]
            #this call function runs upto the last index
            students_grade(mark)
            #every mark is get calculated and stored in total marks
            total_marks += mark  
#to find the average grade 
avg_grade = total_marks // len(marks)
print("avg class grade : ", avg_grade)
#the average grade is called to get the grade for average
students_grade (mark)

"""
test case:
enter the total students : 2
total subjects : 2
subject1
enter the mark of student 1scored : 102
invalid mark
enter the correct mark : 90
the grade is A
enter the mark of student 2scored : 90
the grade is A
subject2
enter the mark of student 1scored : 101
invalid mark
enter the correct mark : 90
the grade is A
enter the mark of student 2scored : 90
the grade is A
avg class grade :  96
the grade is A
"""