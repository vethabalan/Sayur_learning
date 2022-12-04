import math
minute_hand = int(input("minute_hand : "))
hour_hand = int(input("hour_hand : "))
total_degree_of_clock = 360
total_minutes_in_an_Hour = 60
Total_hours_in_a_clock = 12
if( hour_hand < 0 or minute_hand < 0 or hour_hand > 12 or minute_hand > 60):
    print("not a valid input")
if(hour_hand == 12):
    hour_hand = 1
if (minute_hand == 60) :
    minute_hand = 0 
    #hour_hand += 1
    if(hour_hand > 12):
        hour_hand -= 12
if( minute_hand <= 60 and (hour_hand >= 1 and hour_hand <= 12)):
#     big_hand = (total_degree_of_clock / total_minutes_in_an_Hour) * big_hand
#     small_hand = ( total_degree_of_clock / Total_hours_in_a_clock ) * small_hand + ((big_hand/total_minutes_in_an_Hour) * (total_degree_of_clock/Total_hours_in_a_clock))
#     degree = ( small_hand / big_hand  ) * 360
#     Angle = abs(big_hand - small_hand)
    big_hand = 6 * minute_hand
    small_hand = 0.5 * ( hour_hand * total_minutes_in_an_Hour + minute_hand) 
    Angle = abs(big_hand - small_hand)
    Angle = min( 360 - Angle , Angle)
print("Angle :",Angle) 

""" 
Test Case - 1
    minute_hand : 60
    hour_hand : 4
    Angle : 120.0
    
    Test Case - 2
    minute_hand : 30
    hour_hand : 12
    Angle : 135.0
    
"""