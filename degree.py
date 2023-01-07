#degree

mark_1 = int(input("enter mark_1: "))
mark_2 = int(input("enter mark_2: "))
mark_3 = int(input("enter mark_3: "))
mark_4 = int(input("enter mark_4: "))
mark_5 = int(input("enter mark_5: "))

#assigning maximum and minimum mark for each statement
max_mark=60
min_mark = 0
if((mark_1>=max_mark) and (mark_2>=max_mark) and (mark_3>=max_mark) and (mark_4>=max_mark) and (mark_5>=max_mark)):
    print("pass")

#assigning maximum and minimum mark for each statement    
    max_mark = 90
    min_mark = 40
elif((mark_1>=max_mark) and (mark_2>=max_mark) and (mark_3>=max_mark) and (mark_4>=min_mark) and (mark_5>=min_mark)):
    print("pass")

#assigning maximum and minimum mark for each statement
    max_mark = 75
    min_mark = 50

elif((mark_1 >=max_mark) and (mark_2 >= max_mark) and (mark_3 >= max_mark) and (mark_4 >= min_mark)and (mark_5 >= min_mark)):
    print("pass")
    
else:
    print("fail")
    
