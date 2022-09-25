"""
Write a function that generates a random number that is always divisible by the input number.
For eg: If input is 5 , the random function should only generate the divisible of the input number.

"""
import random
divisible_number = int(input("enter the number : "))
number_range = int(input("enter the range : "))
def random_generator(divisible_number , number_range):
    for divisible in range ( 1 , number_range+1):
        random_number = random.randint(1, number_range + 1 )
        if( random_number % divisible_number == 0):
            print(random_number)
random_generator(divisible_number, number_range)

"""
TEST CASE: 1
enter the number : 7
enter the range : 50
28
49
21
21
28
21
    """