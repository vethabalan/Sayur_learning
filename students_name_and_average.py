# calculate class average marks
# assigning a list to get the students name
total_students = int (input("total students: "))
list_of_students = []
mark = []
total_mark = 0
for total_student in range(0,total_students ):
    list_of_students.append(input("enter the student name: "))
    mark.append(int(input("what is your mark?: ")))
    total_mark += mark[total_student]
for index in range(0,len(list_of_students)):
    print(str(list_of_students[index]) + "scored" + str(mark[index]))
print("total mark = ",total_mark)
average_mark_of_class = total_mark/total_students
print("average mark of the class: ",average_mark_of_class)
