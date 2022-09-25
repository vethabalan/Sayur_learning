# convert digit into words

list_of_number = ["zero" ,"one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine"]

def number_to_word(num):

    if(num == 0):

        return " "

    else:
        small_ans = list_of_number[num % 10]

        ans = number_to_word(int(num / 10)) + small_ans + " "

    return ans

num = int(input())
print("input of number: ",num)
print("digit into word: ",end = " ")
print(number_to_word(num)) 