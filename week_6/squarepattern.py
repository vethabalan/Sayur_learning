"""
write a function that displays a square box with "*" . input is width of the square
"""
width = int(input("enter your width you want : "))
def square (width):
    for outer_loop in range(0 , width):
        for inner_loop in range( 0 , width):
            print(" *" , end = " ")
        print()
square(width)
"""
output:
    
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 
 """